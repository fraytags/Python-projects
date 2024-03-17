"""Extra Challenge: Longest Value
Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}"""


def longest_value(di: dict) -> str:
    """This function returns the first longest value of the dictionnary"""
    max = ""
    for v in fruits.values():
        if len(max) < len(v):
            max = v
    return max


fruits = {"fruit": "apple", "color": "green", "city": "gggggg"}
# print(longest_value(fruits))


"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9."""


def convert_add(li: list) -> int:
    new_li = []
    for l in li:
        new_li.append(int(l))
    sum = 0
    for n in new_li:
        sum = n + sum
    return sum


# res = convert_add(["5", "6", "8", "9"])
# print(res)


"""Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']"""


def check_duplicates(li=list) -> str:
    """This function checks for duplicates in a list of string"""
    for i in range(len(li)):
        for j in range(1, (len(li) - 1)):
            return li[i]
            print(j)
        else:
            print(i)
            print("no duplicates")


fruits = ["apple", "orange", "banana", "coco"]


# print(check_duplicates(fruits))


"""Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says ‘yes’. If
the student is not in school, the dictionary says ‘no’. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3.
register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}
Extra Challenge: Lowercase Names
names = ["kerry", "dickson", "John", "Mary",
"carol", "Rose", "adam"]
You are"""


def register_check(di: dict) -> int:
    present = 0
    for k, v in di.items():
        if v == "yes":
            present = present + 1
    return present


register = {
    "Marion": "yes",
    "Nicolas": "yes",
    "Antoine": "yes",
    "Rémi": "no",
    "thomas": "no",
    "Anabelle": "yes",
}
# print(register_check(register))


"""Extra Challenge: Lowercase Names
names = ["kerry", "dickson", "John", "Mary",
"carol", "Rose", "adam"]
You are given a list of names above. This list is made up of names
of lowercase and uppercase letters. Your task is to write a code
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted
alphabetically in descending order. Using the list above, your
code should return:
('kerry', 'dickson', 'carol', 'adam')"""


def lower_case_names(di: dict) -> tuple:
    pass


"""Write a function called only_floats, which takes two
parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is a float, and returns 0 if neither
argument is a float. If you pass (12.1, 23) as an argument, your
function should return a 1."""


def only_floats(x, y) -> int:
    x = str(x)
    y = str(y)
    if "." in x and "." in y:
        return 2
    elif "." in x or "." in y:
        return 1
    else:
        return 0


#
# print(only_floats(15, 16))


"""Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, should return zero (0)
words2 = ["Love", "Hate"]"""


def word_index(li: list) -> int:
    len_li = []
    for i in range(len(li)):
        len_li.append(len(li[i]))
    if len_li[:1] is not len_li[:-1]:
        return max(len_li)
    else:
        return 0


# word_list = ["Antoine", "Antoine", "Antoine"]
#
# print(word_index(word_list))


"""Create a function called my_discount. The function takes no
arguments but asks the user to input the price and the
discount (percentage) of the product. Once the user inputs the
price and discount, it calculates the price after the discount.
The function should return the price after the discount. For
example, if the user enters 150 as price and 15% as the discount,
your function should return 127.5."""


def my_discount():
    price = float(input("Please enter the price : "))
    discount = float(input("Please enter the discount : "))
    new_price = price - (price * discount / 100)
    return new_price


# print(my_discount())


"""Extra Challenge: Tuple of Student Sex
You work for a school and your boss wants to know how many
female and male students are enrolled in the school. The school
has saved the students in a list. Your task is to write a code that
will count how many males and females are in the list. Here is a
list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
Your code should return a list of tuples. The list above should
return:
[(‘Male’,7), (‘female’,6)]"""


def stud_sex(lis_stu: list) -> tuple:
    j = 0
    i = 0

    for s in lis_stu:
        if s.lower() == "male":
            i = i + 1
        elif s.lower() == "female":
            j = j + 1
    return [("Male", i), ("female", j)]


stu = [
    "Male",
    "Female",
    "female",
    "male",
    "male",
    "male",
    "female",
    "male",
    "Female",
    "Male",
    "Female",
    "Male",
    "female",
    "male",
    "female",
    "female",
]

# print(stud_sex(stu))


"""Write a function called user_name that generates a username
from the user’s email. The code should ask the user to input an
email and the code should return everything before the @ sign
as their user name. For example, if someone enters
ben@gmail.com, the code should return ben as their user
name."""


def username_generator() -> str:

    mail = input("What is your mail ?")
    name = mail.split("@")
    return name[0]


# username_generator()


"""Extra Challenge: Zero Both ends
Write a function called zeroed code that takes a list of numbers
as an argument. The code should zero (0) the first and the last
number in the list. For example, if the input is [2, 5, 7, 8, 9],
your code should return [0, 5, 7, 8, 0]."""


def zero_both_end(li: list) -> list:
    li[0] = 0
    li[len(li) - 1] = 0
    return li


# li = [2, 5, 7, 8, 9]
# print(zero_both_end(li))


"""Write a function called string_range that takes a single
number and returns a string of its range. The string characters
should be separated by dots(.) For example, if you pass 6 as
an argument, your function should return ‘0.1.2.3.4.5’."""


def string_range(i: int) -> list:
    tab = list(j for j in range(i))
    nt = []
    for t in tab:
        nt.append(f"{str(t)}.")
    return nt


# ta = string_range(10)
# print(ta)
# for t in ta:
#     print(type(t))
#
# for t in ta:
#     print(type(t))


"""Extra Challenge: Dictionary of names
You are given a list of names, and you are asked to write a code
that returns all the names that start with ‘S’. Your code should
return a dictionary of all the names that start with S and how
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
Your code should return: {“Sasha”: 1, “Sera”: 2}"""


def dic_names(li: list) -> dict:
    tab_s = []
    for l in li:
        if str(l).startswith("S"):
            tab_s.append(l)
        else:
            pass
    num = 0
    j = 0

    for i in range(len(tab_s) - 1):
        for j in range(1, len(tab_s) - 1):
            if tab_s[j] == tab_s[i]:
                num = num + 1
                print(f"{tab_s[j]} : {num}")
            else:
                pass

    names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani"]


# dic_names(t)


"""Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the
difference between the largest even number in the list and the
smallest odd number in the list. For example, if you pass
[1,2,4,6] as an argument the function should return 6 -1= 5."""


def odd_even(li: list) -> list:
    odds = []
    evens = []

    for l in li:
        if l % 2 == 0:
            evens.append(l)
        elif l % 2 != 0:
            odds.append(l)
    return max(evens) - min(odds)


l = [1, 2, 4, 6]
# print(odd_even(l))

"""Write a function called prime_numbers. This function asks a
user to enter a number (integer) as an argument and returns a
list of all the prime numbers within its range. For example, if user
enters 10, your code should return [2, 3, 5, 7] as prime numbers."""


def prime_numbers() -> list:
    num = int(input("Enter a number : "))
    ta = []
    for t in range(1, num + 1):
        if t % 2 == 0:
            pass
        else:
            ta.append(t)
    return ta


# print(prime_numbers())


"""Create a function called biggest_odd that takes a string of
numbers and returns the biggest odd number in the list. For
example, if you pass ‘23569’ as an argument, your function
should return 9. Use list comprehension."""


def biggest_odd(num: str) -> int:
    toints = []
    for n in num:
        toints.append(int(n))
    odds = []
    for toint in toints:
        if toint % 2 != 0:
            odds.append(toint)
    ma = max(odds)
    return ma


# print(biggest_odd("5886665"))


"""Write a function called zeros_last. This function takes a list as
argument. If a list has zeros (0), it will move them to the front of
the list and maintain the order of the other numbers in the list.
If there are no Zeros in the list, the function should return the
original list sorted in ascending order. For example, if you pass
[1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
your code should return [1, 2, 4, 6, 7]."""


def zeros_last(lis : list) -> list:
    for l in lis:
        if l == 0:
            lis.remove(l)
            lis.append(0)
        if not 0 in lis:
            lis.sort()
    return lis


"""Write a function called hide_password that takes no
parameters. The function takes an input (a password) from a
user and returns a hidden password. For example, if the user
enters ‘hello’ as a password the function should return ‘****’ as
a password and tell the user that the password is 4 characters
long."""


def hide_password() -> str:

    password = input("What is your password ? ")
    res = "*" * len(password)
    return res


"""Your new company has a list of figures saved in a list. The issue
is that these numbers have no separator. The numbers are
saved in the following format:
[1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each of the
numbers in the list into a string. Your code should then add a
comma on each number as a thousand separator for
readability. When you run your code on the above list, your
output should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
Write a function called convert_numbers that will take one
argument, a list of numbers above."""


def convert_numbers(li: list) -> list:
    pass


"""Write a function called equal_strings. The function takes two
strings as arguments and compares them. If the strings are equal
(if they have the same characters and have equal length), it
should return True, if they are not, it should return False. For
example, ‘love’ and ‘evol’ should return True."""


def equal_strings(st1, st2: str) -> bool:

    if st1.lower() == st2.lower():
        return True
    else:
        return False


# print(equal_strings("Antoine", "Antoine"))


"""Write a function called swap_values. This function takes a list
of numbers and swaps the first element with the last element.
For example, if you pass [2, 4,67, 7] as a parameter, your
function should return
[7, 4, 67, 2]."""


def swap_values(li: list) -> list:
    first = li[0]
    last = li[len(li) - 1]

    li.append()


"""Write a function called count_dots. This function takes a
string separated by dots as a parameter and counts how many
dots are in the string. For example, ‘h.e.l.p.’ should return 4
dots, and ‘he.lp.’ should return 2 dots."""


def count_dots(strin: str) -> str:
    d = 0
    lis = list(strin)
    for li in lis:
        if li == ".":
            d = d + 1
        else:
            pass
    return d


# print(count_dots("h.e.l.p...."))
