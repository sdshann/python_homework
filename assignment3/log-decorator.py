#Task 1
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {list(args) if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        return result
    return wrapper

@logger_decorator
def hello():
    print("Hello World!")

@logger_decorator
def positional(*args):
    return True

@logger_decorator
def keyword(**kwargs):
    return logger_decorator


hello()
positional(1, 2, 3)
keyword(first_name="Samantha", last_name="Shannon")
