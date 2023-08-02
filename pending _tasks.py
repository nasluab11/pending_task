#DICTIONARY
'''''''''
# Q1
my_dict = {'name': 'John', 'age': 25, 'address': 'New York'}

# Q2
my_dict['phone'] = '1234567890'

# Q3
del my_dict['address']

# Q4
print("Age:", my_dict['age'])

# Q5
print("Phone key exists:", 'phone' in my_dict)

#SET
# Q1
my_set = {1, 2, 3, 4, 5}

# Q2
my_set.add(6)

# Q3
my_set.remove(3)

# Q4
print("Length of the set:", len(my_set))

# Q5
new_set = my_set.union({6, 7, 8})
print("Union of the sets:", new_set)

#TUPLE
# Q1
my_tuple = (1, 2, 3, 4)

# Q2
print("Length of the tuple:", len(my_tuple))

# Q3
new_tuple = my_tuple + (5, 6)

# Q4
print("First two values of the new tuple:", new_tuple[:2])

# Q5
if 4 in my_tuple:
    print("Value 4 exists in the tuple.")
else:
    print("Value 4 does not exist in the tuple.")

'''
#Topic : functions and its types of attributes
'''''''''
num1 = float(input("entr the number :"))
num2 = float(input("enter your second number :"))
print("1.Addistion\n2.Substraction\n3.Multiplication\n4.Division")
result = int(input("enter your selection"))
if result == 1:
    check = num1 + num2
    print("result:",check)
elif result == 2:
    check = num1 - num2
    print("result:", check)
elif result == 3:
    check = num1 * num2
    print("result:", check)
elif result == 4:
    if num2 == 0:
        print("division / 0 is not possible")
    else:
        check = num1 / num2
        print("result:", check)
else:
    print("you entered the wrong value")


#EXERCISE 2
def custom_function(required_arg, optional_arg1=10, optional_arg2=None):
    if optional_arg2 is None:
        print("Sum of the first two arguments:", required_arg + optional_arg1)
    else:
        print("Product of all three arguments:", required_arg * optional_arg1 * optional_arg2)

# Testing the function
custom_function(5)               
custom_function(3, 6)             
custom_function(2, 3, 4)          

#EXERCISE 3
def sum_even_numbers(*args):
    even_sum = sum(num for num in args if num % 2 == 0)
    print("Sum of even numbers:", even_sum)

# Testing the function
sum_even_numbers(1, 2, 3, 4, 5)        
sum_even_numbers(7, 9, 11)               
sum_even_numbers(2, 4, 6, 8, 10)         

#EXERCISE 4
def custom_product(required_arg1, required_arg2, optional_arg=1, *args):
    product_required_args = required_arg1 * required_arg2
    product_optional_arg = product_required_args * optional_arg
    product_arbitrary_args = product_optional_arg * product_list(list(args))
    print("Final product:", product_arbitrary_args)

# Helper function to calculate the product of all elements in a list
def product_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Testing the function
custom_product(2, 3, 5, 4, 2, 1)    
custom_product(1, 1)              
custom_product(3, 4, 2)           
#EXERCISE 5
def filter_strings_by_length(lst):
    return [string for string in lst if len(string) >= 5]

# Testing the function
strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
filtered_list = filter_strings_by_length(strings_list)
print(filtered_list)   

#EXERCISE 6
def filter_strings_by_vowel(lst):
    vowels = "aeiouAEIOU"
    return [string for string in lst if any(char in vowels for char in string)]

# Testing the function
strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
filtered_list = filter_strings_by_vowel(strings_list)
print(filtered_list)  


#Topic : Recursion, lambda, eval and filter

#exercise 1
def sum_recursive(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])

# Testing the function
numbers_list = [1, 2, 3, 4, 5]
result = sum_recursive(numbers_list)
print("Sum using recursion:", result)

#exercise 2
is_even = lambda x: x % 2 == 0

# Testing the lambda function
print(is_even(4))
print(is_even(5))

#exercise 3
add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

# Testing the lambda functions
print(add_15(5))
print(multiply(3, 4))

#exercise 4
expression = "3 * 5 + 2"
result = eval(expression)
print("Result of the expression:", result)

#exercise 5
expression = "5 > 2 and 3 < 4"
result = eval(expression)
print("Result of the logical expression:", result)

#exercise 6
expression = "[x * 2 for x in range(5)]"
result = eval(expression)
print("Result of the Python expression:", result)

#exercise 7
def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

char_list = ['a', 'b', 'e', 'g', 'i', 'o', 'p', 'u']
vowels_list = list(filter(is_vowel, char_list))
print("Vowels:", vowels_list)

#exercise 8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers_list = list(filter(is_prime, numbers_list))
print("Prime numbers:", prime_numbers_list)

#exercise 9
def greater_than_5(string):
    return len(string) > 5

strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
filtered_list = list(filter(greater_than_5, strings_list))
print("Strings with length greater than 5:", filtered_list)   
'''

#Topic : map, reduce, generators and decorators
'''
# Exercise 1: Convert List of Strings to Uppercase using map()
strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
uppercase_strings = list(map(str.upper, strings_list))

# Exercise 2: Square Each Number in a List using map()
numbers_list = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers_list))

# Exercise 3: Calculate Length of Each String in a List using map()
strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
length_of_strings = list(map(len, strings_list))

# Exercise 4: Calculate Sum of Elements in a List using reduce()
from functools import reduce

numbers_list = [1, 2, 3, 4, 5]
sum_of_elements = reduce(lambda x, y: x + y, numbers_list)

# Exercise 5: Calculate Product of Elements in a List using reduce()
from functools import reduce

numbers_list = [1, 2, 3, 4, 5]
product_of_elements = reduce(lambda x, y: x * y, numbers_list)

# Exercise 6: Find Maximum Element in a List using reduce()
from functools import reduce

numbers_list = [2, 6, 1, 9, 4, 7]
maximum_element = reduce(lambda x, y: x if x > y else y, numbers_list)

# Exercise 7: Generator Function for Yielding Words in a String
def word_generator(s):
    for word in s.split():
        yield word

# Exercise 8: Generator Function for Yielding Only Even Numbers
def even_numbers_generator(numbers_list):
    for num in numbers_list:
        if num % 2 == 0:
            yield num

# Exercise 9: Generator Function for Yielding Strings Starting with a Vowel
def vowel_strings_generator(strings_list):
    vowels = "aeiouAEIOU"
    for string in strings_list:
        if string[0] in vowels:
            yield string

# Exercise 10: Decorator Function for Measuring Execution Time
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution Time:", end_time - start_time, "seconds")
        return result
    return wrapper

# Exercise 11: Decorator Function for Logging Arguments and Return Value
def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Return Value:", result)
        return result
    return wrapper

# Testing the functions and generators
if __name__ == "__main__":
    print("Exercise 1:", uppercase_strings)
    print("Exercise 2:", squared_numbers)
    print("Exercise 3:", length_of_strings)
    print("Exercise 4:", sum_of_elements)
    print("Exercise 5:", product_of_elements)
    print("Exercise 6:", maximum_element)

    sentence = "Write a generator function"
    gen = word_generator(sentence)
    print("Exercise 7:", list(gen))

    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gen = even_numbers_generator(numbers_list)
    print("Exercise 8:", list(gen))

    strings_list = ["apple", "banana", "grapes", "orange", "kiwi", "mango"]
    gen = vowel_strings_generator(strings_list)
    print("Exercise 9:", list(gen))

    @execution_time_decorator
    def example_function():
        time.sleep(2)

    example_function()

    @log_arguments_and_return
    def example_function(a, b, c=3):
        return a + b + c

    example_function(1, 2, c=4)

'''
#Topic : File handling
'''
# Exercise 1: Read and Display File Contents
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")
# Exercise 2: Count Number of Lines in a File
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        print("Number of lines:", num_lines)

# Exercise 3: Write Some Text to a File
def write_text_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# Exercise 4: Append Text to a File
def append_text_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

# Exercise 5: Copy Contents from One File to Another
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        destination.write(source.read())

# Exercise 6: Count Total Number of Words in a File
def count_words(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        words = contents.split()
        num_words = len(words)
        print("Total number of words:", num_words)

# Exercise 7: Count Occurrences of a Specific Word in a File
def count_word_occurrences(file_path, word):
    with open(file_path, 'r') as file:
        contents = file.read()
        occurrences = contents.lower().count(word.lower())
        print("Number of occurrences of the word '{}': {}".format(word, occurrences))

# Exercise 8: Count Number of Unique Words in a File
def count_unique_words(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        words = contents.split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        print("Number of unique words:", num_unique_words)

# Testing the functions
# Exercise 1: Read and Display File Contents
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

    # Exercise 2
    file_path = 'example.txt'
    count_lines(file_path)

    # Exercise 3
    file_path = 'new_file.txt'
    text = "Hello, this is a new file!"
    write_text_to_file(file_path, text)

    # Exercise 4
    file_path = 'existing_file.txt'
    text = "\nThis text is appended."
    append_text_to_file(file_path, text)

    # Exercise 5
    source_file = 'source.txt'
    destination_file = 'destination.txt'
    copy_file(source_file, destination_file)

    # Exercise 6
    file_path = 'example.txt'
    count_words(file_path)

    # Exercise 7
    file_path = 'example.txt'
    word = 'Python'
    count_word_occurrences(file_path, word)

    # Exercise 8
    file_path = 'example.txt'
    count_unique_words(file_path)
'''
#Topic : Exception Handling
'''''''''
# Exercise 1: Convert Input String to Integer with Exception Handling
def string_to_integer(input_string):
    try:
        integer_value = int(input_string)
        print("Converted integer:", integer_value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Testing the function
input_string = input("Enter a string: ")
string_to_integer(input_string)


# Exercise 2: Check for Negative Integers in a List with Exception Handling
def check_negative_integers(input_list):
    try:
        if any(num < 0 for num in input_list):
            raise ValueError("Negative integers are not allowed.")
        print("All integers are non-negative.")
    except ValueError as e:
        print(e)

# Testing the function
input_list = [1, 2, -3, 4, 5]
check_negative_integers(input_list)


# Exercise 3: Compute Average of Integers with Exception Handling
def compute_average(input_list):
    try:
        total_sum = sum(input_list)
        total_count = len(input_list)
        average = total_sum / total_count
        print("Average:", average)
    except ZeroDivisionError:
        print("The list is empty.")
    except TypeError:
        print("Please enter a list of integers.")
    finally:
        print("Program has finished running.")

# Testing the function
input_list = [1, 2, 3, 4, 5]
compute_average(input_list)

try:
    input_list = []
    compute_average(input_list)
finally:
    print("Program has finished running.")


# Exercise 4: Write to File with Exception Handling
def write_to_file(file_name, text):
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        print("Welcome message written to file:", file_name)
    except Exception as e:
        print("An error occurred:", str(e))

# Testing the function
file_name = input("Enter the filename: ")
welcome_message = "Hello, welcome to the file handling exercise!"
write_to_file(file_name, welcome_message)

'''
#Topic : object oriented programming
'''''''''
# Exercise 1: University Course Catalog

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, " \
               f"Credit Hours: {self.credit_hours}, Required for Major: {self.required_for_major}"


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, " \
               f"Credit Hours: {self.credit_hours}, Elective Type: {self.elective_type}"


# Testing the classes
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
print(core_course)

elective_course = ElectiveCourse("ART202", "Art History", 4, "liberal arts")
print(elective_course)


# Exercise 2: Shape and Rectangle

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Testing the classes
rectangle = Rectangle(5, 7)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())


# Exercise 3: Vehicle, Car, and Motorcycle

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def description(self):
        return super().description() + f", Number of Doors: {self.num_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def description(self):
        return super().description() + f", Has Sidecar: {self.has_sidecar}"


# Testing the classes
car = Car("Toyota", "Corolla", 2022, 4)
print(car.description())

motorcycle = Motorcycle("Harley Davidson", "Road King", 2021, False)
print(motorcycle.description())















