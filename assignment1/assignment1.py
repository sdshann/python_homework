#Task 1
from unittest import result


def hello():
    return("Hello!")

print(hello())

#Task 2
def greet(name):
    return("Hello, " + name + "!")

print(greet("Gia"))

#Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
#Task 4
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    except TypeError:
        return f"You can't convert {value} into a {type}."
    
print(data_type_conversion("5", "int"))
print(data_type_conversion("5.5", "float"))
print(data_type_conversion(7, "str"))
print(data_type_conversion("Hello", "int"))

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

#Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

#Task 7
def student_scores(positional_parameter, **kwargs):
    if positional_parameter == "mean":
        return sum(kwargs.values()) / len(kwargs.values())
    elif positional_parameter == "best":
        return max(kwargs, key=kwargs.get)
    

#Task 8
def titleize(string):
    words = string.split()
    result = []
    for index, word in enumerate(words):
        if index == 0:
            result.append(word.capitalize())
        elif index == len(words) - 1:
            result.append(word.capitalize())
        elif word in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

#Task 10
def pig_latin(string):
    words = string.split()
    result = []
    for word in words:
        if word[0] in ["a", "e", "i", "o", "u"]:
            result.append(word + "ay")
        elif word[0:2] == "qu":
            result.append(word[2:] + word[0:2] + "ay")
        else:
            count = 0
            while word[count] not in ["a", "e", "i", "o", "u"]:
                if word[count:count+2] == "qu":
                    count += 2
                else:
                    count += 1
            result.append(word[count:] + word[:count] + "ay")
    return " ".join(result)
        