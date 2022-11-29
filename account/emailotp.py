# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# dict = {}
# dict.update(dic1)
# dict.update(dic2)
# dict.update(dic3)
# print(dict)

# Write a Python script to check whether a given key already
# exists in a dictionary
# dict = {"name": "mithilesh", "roll": "101", "hobby": "singing"}
# print(dict['name'])

# def check_key(x):
#     d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     if x in d:
#         print("The key present in dictionary:")
#     else:
#         print("Keynot presentin dictionary:")


# check_key(100)
# check_key(10)
# check_key(10)
# check_key(10)
# Write a Python script to print a dictionary where the keys
# are numbers between 1 and 15 (both included)
# and the values are square of keys.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
# 10: 100, 11: 121,
# 12: 144, 13: 169, 14: 196, 15: 225}
# for x in range(1, 16):
#     dict = {x: x*x}
#     dict1 = {}
#     dict1.update(dict)
# print(dict1)
# Write a Python script to merge two Python dictionaries.
# dict1 = {"name": "mitrhilesh", "roll": 101}
# dic2 = {"school": "zila school", "city": "Raxaul"}
# dict3 = {}
# dict3.update(dict1)
# dict3.update(dic2)
# print(dict3)
# Write a Python program to
# iterate over dictionaries using for loops.
# dict = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500,
#         6: 600, 7: 700, 8: 800, 9: 900, 10: 1000}
# for x in dict:
#     print("the key of given dictinary is:", x,
#           "and the corresponding values of the dictionary is=", dict[x])
# Write a Python program to sum
# all the items in a dictionary
# dict = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500,
#         6: 600, 7: 700, 8: 800, 9: 900, 10: 1000}
# sum = 0
# for x in dict.values():
#     sum = sum+x
#     print(sum)
# Write a Python program to
# multiply all the items in a dictionary
# dict = {1: 10, 2: 20}
# total = 1
# for x in dict.values():
#     total = total*x
# print(total)
# Write a Python program to remove a key from a dictionary
# dict = {'a': 10, 'b': 20, 'c': 30}
# print(dict)
# for x in dict:
#     print(x)
# if x in dict:
#     del dict['x']

# print(dict)
# list1 = [10, 20, 30, 40]
# list1.split()
#list2 = [50, 60, 70, 80]
# print(list1)
# Write a Python program to get the maximum
# and minimum value in a dictionary
# my_dict = {'x': 500, 'y': 5874, 'z': 560}
# max_value = max(my_dict.keys(), key=lambda k: my_dict[k])
# min_value = min(my_dict.keys(), key=lambda k: my_dict[k])
# print("The maximum value=", my_dict[max_value],
#       "The minimum value is =", my_dict[min_value])
# Write a Python program to get
# a dictionary from an object's fields
# class dictObj(object):
#     def __init__(self):
#         self.x = "red"
#         self.y = "green"
#         self.z = "white"

#     # def do_nothing(self):
#     #     pass


# test = dictObj()
# print(test.__dict__)

# class MyDict(object):
#     def __init__(self):
#         self.x = "mithilesh"
#         self.y = "simran"
#         self.z = "shaweta"


# ss = MyDict()
# print(ss.__dict__)
# Write a Python program to
# remove duplicates from Dictionary
# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 50, 7: 40, 8: 20}
# result = {}
# for key, value in dict.items():
#     if value not in result.values():
#         result[key] = value
# print(result)
# employee = {}
# for i in range(3):
#     name = input("Enter name of the employee:")
#     salary = int(input("Enter employee salary:"))
#     employee[name] = salary
# print(employee)
# Write a Python program to
# check a dictionary is empty or not.
# dict = eval(input("enter dictionary:"))
# if dict.values() == None:
#     print("Dictionary is empty:")
# else:
#     print("Dictionary is not empty:")
# Write a Python program to combine
# two dictionary adding values
# for common keys. Go to the editor
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# d = Counter(d1)+Counter(d2)
# print(d)
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# Write a Python program to print all unique values in a dictionary
# L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#      {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print("original list is:", L)
# unique_value = set(val for dic in L for val in dic.values())
# print(unique_value)
# def l(x, y): return x*y


# print(l(10, 2))
# def s(x):
#     return x+50


# print(s(50))
# def d(s):
#     return s*10


# print(d(12))
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Social sciences', 82)]
# print("original list:", subject_marks)
# subject_marks.sort(key=lambda x: x[1])
# print("Sorted list:", subject_marks)
# Write a Python program to square
# and cube every number
# in a given list of
# integers using Lambda.
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = list(map(lambda x: x*x, l))
# l2 = list(map(lambda x: x*x*x, l))
# print(l1)
# print(l2)
# def s(x): return True if x.starts_with("P") else False


# print(s("Python"))
# import datetime
# now=datetime.datetime.now()
# s = "mithilesh"
# print(len(s))
# token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTE0MTExLCJpYXQiOjE2NjAxMTA1MTEsImp0aSI6IjBhNjdiNjI0MGMyMDQ3NThhYzM5OTY3ODc1NjlkZTFlIiwidXNlcl9pZCI6M30.CkO5iD9EfY_DmqZ3Ca6nlYUeaIAOXa29k4mP6SCfdyI"
# def user_token()
from __future__ import print_function
import email
import random
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
s = "shailesh"
# output=shaile$h
# ch = s[0]
# s1 = s.replace(ch, "$")
# s2 = ch+s1[1:]
# print(s2)
# ss = "paramanand"
# ch1 = ss[0]
# ch = ss[1]
# ss1 = ss.replace(ch, "*")
# ss2 = ch1 + ch+ss1[2:]
# print(ss2)

# a = 100
# b = "Nikhil"
# fgfgsfgdfgf=10
# def =90
# if=20


def sendmail(data):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    subject = "This is your One Time Password ,Do not share with anyone !"
    sender = {"name": "Tinssle Team", "email": "mithilesh@foreantech.com"}
    replyTo = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
    to = [{"email": data['to'], }]
    html_content = '<html><body><h1>This is your One Time Password Provide at Login time!!!</h1><br/><p>' + \
        data['body']+'</p></body></html>'

    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
