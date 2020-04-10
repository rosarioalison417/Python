# ##################### IMPORTANT ######################
# TO RUN A SCRIPT: Command+I
# COMMAND PALETTE: CMD+SHIFT+P
# To comment a line: Command+/
#
# ###################### CONDITIONS ######################
#
# if 5 < 7:
#     if 6 > 5:
#         print("6>5")
# print("5<7")
#
# passerby_speech = "Hello"
# if passerby_speech == "Hello":
#     print("Hi")
# elif passerby_speech == "Hi":
#     print("Hello")
# else:
#     print("Hey")
#
# a = 3 if 3**2 > 9 else 14   -----------> Ternary operations
# print(a)
#
# ###################### LOOPS ######################
#
# range(start, stop, step)   --------------> used in loops
# below code is equivalent to for(i=0, i<=10, i++)
# for i in range(2,10):
#     print(i)
#
# string = "String Traversal"
# for i in range(len(string)):
#     print(string[i])
# for i in string:
#     print(i)
#
# condition = 10
#
# while condition != 0:
#     print(condition)
#     condition = condition - 1
#
# ###################### FUNCTIONS ######################
#
# def function():
#     return "This function returns"
# result = function
#
# print(result)
#
# def multiVal():
#     return "This is a result, ", 2
# print(multiVal())
#
# def par(a, b):
#     c = a+b
#     return c
# result = par(10, 2)
# print(result)
#
# def default_param(a = 3, b = 4, c = 5):  -------> Parameters pass by value
#     return a+b+c
# result = default_param()
# print(result)
#
# ###################### SCOPE OF A PARAMTER ######################
#
# def scope(a):
#     a= a+1
#     print(a)
#     return a
# scope(5)
# print(a)     --------> a is outside its scope
#
# def outer(a):
#     def inner(b):
#         print("Inner done")
#         return b * a
#     a = inner(a)
#     print("Outer done")
#     return(a)
# print(outer(4))
#
#
# def p(a):
#     def q(b):
#         def r(c):
#             print("R done")
#             return a*b*c
#         print("Q done")
#         return r
#     print("P done")
#     return q
# print(p(4)(5)(2))     ----------->p=4, q=5, r=2
#
# ###################### RECURSIVE FUNCTIONS ######################
#
# def factorial(n):
#     if n == 1:
#         return 1;
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
#
# def sum(n):   -------> Normal recursive funtion
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)
#
# def tail_sum(n, accumulator = 0):  ----> recursive tail function with repeating paramter "Accumulator"
#     if n == 0:
#         return accumulator
#     else:
#         return tail_sum(n-1, accumulator+n)
# print(sum(10))
# print(tail_sum(10))
#
# Lambda function
# f = lambda c: lambda a, b: lambda d: (c * (a + b)) % d
# print(f(5)(4,3)(2))
#
# ###################### EXCEPTION HANDLING ######################
#
# i = 5/0
# print(i)
# file = open("file","r")
#
#
# try:
#     a= 5/0
# except Exception as e:
#     print(e)
#
# try:
#     n = int(input("Enter an Int: "))
# except ValueError:
#     print("This is not an integer")
#
# print("ENter your name: ")
# x = input()
# print('Hello')
# sum = 0
# file = open("File.txt", "r")
# try:
#     for numbers in file:
#         sum = sum + 1
#         print(sum)
# except FileNotFoundError:
#     print("The file dne")
#
# a=1
# def RaiseException(a):
#     if type(a) != type('a'):
#         raise ValueError("This is a string")
# try:
#     RaiseException(a)
# except ValueError as e:
#     print(e)
#
# def TestCase(a, b):
#     assert a < b, "a is greater than b"
# try:
#     TestCase(2, 1)
# except AssertionError as e:
#     print(e)
#
# ###################### DATA I/O ##################################
#
# age = 1
# age = input("How old are you: ")
# print(age)
#
# FILE MANAGEMENT
# open(filename, access, buffering)
#
# file = open("/Users/alisonrosario/Desktop/Python/File.txt", "r")
# # print(file.read())
# # file.seek(2)
# # print(file.tell())
# # for line in file:
# #     print(line)
# print("File Name: " + file.name)
# print("is closed: " + str(file.close))
# file.close()
#
# # try:
# file = open("/Users/alisonrosario/Desktop/Python/File.txt", "w+")
# file.write("Hello File. I am string")
# file.seek(0)
# file.write("This")
# file.seek(0)
# print(file.read())
# file.close()
# except IOError:
#     print("There is an IOError in the code")
#
# ##################### DATA STRUCTURES #############################
#
# ###################### TUPLE - sequence of immutable objects ######################
#
# tup = (1, 'abc', 2, 'cde')
# tup1 = 3, 'efg', True
# tup2 = 'A'  # ----> This works too: tup = ('A', )
#
# print(tup[0])
# print(tup[0:2])
#
# try:
#     tup[3] = 5    # ------> Adding like this doesn't work, refer below block of code for valid code
# except Exception as e:
#     print(e)
#
# tup = tup[0:3] + (5, )  # ----------> Operations applicable on strings can be performed on tuples
# print('A' in tup2)   # -------> Checks if A is in tup2
# print(tup)
#
# for x in ('a', 'b', 'c'):    # ------> Defined a tuple in for loop
#     print(x)
#
# def multipleResult():
#     return (1, 2, 'a')
# print(multipleResult())  # ------> Returns the tuple defined in the function
#
# print((1, 2, 3) == (1, 2))  # ----->Checks if tuples are equal
#
# print(len(tup))
# print(max(tup1))  # ---> Returns the biggest element in the tuples
# print(min(tup1))  # ---> Returns the smallest element in the tuples
#
# ################## LISTS ##############################
#
# list1 = [1, 'abc', (2,3)]
# print(list1)
#
# list1 = list1 + ['4']
# print(list1)
#
# print(list1 * 2)            # ---------> Prints the list elements twice
# print(2 in list1)           # -------> Checks if 2 is in the list
# print(list1 == [1, 'abc'])   # -------> Checks if list1 is equal to the other list
# print(list1[:2])             # ------> Returns 1st 2 elements in the list
#
# list1.append(6)             # --------> Can be used to append the element at the end of the list
# list1[len(list1):] = [7]    # --------> Can be used to append the element at the end of the list (2nd way to add an element)
# print(list1)
#
#
# ####### map(funtion, iterables)  ----> function is applied on the iterables ############
# print(list(map(lambda x: x**2 + 3*x + 1, [1,2,3,4])))
#
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]     # ------> ERROR IN THIS, PLS FIX!
#
# result = list(map(round, circle_areas, range(1,7))
# print(round_circle)
#
# #######filter(funtion, iterables) ----> filters the iterables that are true according to the function ############
# print(list(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])))
#
# ################# reduce() - CHECK ON THIS #######################
# from functools import reduce
# print(functools.reduce(lambda x, y: x * y, [1,2,3,4]))
#
#
# ############## DICTIONARY #######################################
#
# my_dict = {'Key' : 'Value', ('K', 'E', 'Y') : 5}  # -----> Dictionaries use key : value pairs
# my_dict1 = {x: x + 1 for x in range(10)}
#
# print(my_dict)
# print(my_dict['Key'])   # -------> Prints the value for 'Key'
# print(my_dict1[2])
# print(my_dict.keys())   # -------> returns all the keys in the dictionary
# print(my_dict.values()) # -------> returns all the values in the dictionary
# my_dict[1] = 3      # ------> Adds Key = 1 and Value = 3 to my_dict
# del my_dict[1]      # ------> Deletes the Key = 1 and its corresponding value in the dictionary
# my_dict.clear()     # ------> Clears entire dictionary
# print(my_dict)
#
# ########## SHALLOW COPIES : ####################################
# #####Two copies of a data structure, share the same set of elements
#
# my_dictionary = {'Item' : 'Shirt', 'Size' : 'Medium', 'Price' : '$50'}
# my_dictionary1 = my_dictionary  # -----------> copies my_dictionary content to my_dictionary1
# print(my_dictionary)
# my_dictionary1['Size'] = 'Small'
# print(my_dictionary1)
#
# ################## SETS ######################################
# ####### Operations ----> | : Union ; ^ : Intersection ; - : Difference
#
# my_set = set(['one', 'two', 'three', 'one'])
# my_set1 = set(['two', 'three', 'four'])
#
# a = my_set1 - my_set
# print(a)
# print(a >= my_set1)   # ---------> Checks if 'a' has elements >= my_set1
# print(my_set1 ^ my_set)
# print(my_set | my_set1)
# my_set.add('five')      # --------> Add an element in the set
# print(my_set)
#
# print(set.union(my_set, my_set1))           # -------> These do the same thing as the symbols defined above
# print(set.intersection(my_set, my_set1))
# print(set.difference(my_set, my_set1))
#
#
# #################### MODULES AND PACKAGES ##################################
#
# import Package as Alias         # ---------> Import Package with an Alias name
# Alias.AnyFuncInPackage()        # ---------> Alias = Package
#
# from Package import funtion       # --------> Import a specific function from Package
# function()
#
# dir(Package)        # ---------> Returns all the functions in the Package
#
# ___init__       # ---------> ___init__ (3 _ in the beginning, 2 in the end) is used define a package; keep this file in each folder of the package
#
# import copy
#
# my_dictionary = {'Key' : 'Value', ('K','E', 'Y') : 5}     # ------> The deepcopy problem (refer Dictionaries above)
# my_dictionary1 = copy.deepcopy(my_dictionary)
# my_dictionary[1] = 1
#
# print(my_dictionary)
# print(my_dictionary1)
#
# import math as m   #------> math package
# print(dir(m))
#
# import cmath as cm  #------> complex math package
# print(dir(cm))
#
# import random as ran #------> random package
# print(dir(ran))
#
# import sys as s     # -------> System package
# print(dir(s))
#
# print(m.cos(m.pi))
# print(m.exp(1))
# print(m.ceil(1.6))
# print(cm.sqrt(4))
# print(cm.polar(complex(0, 1)))
#
# print(ran.sample([1,2,3,4,5], 3))   # ------> Generates random elements from the list in the blocks of 3
#
# print(s.version)
# print(s.path)
#
# ################################## OBJECT ORIENTED PROGRAMMING ######################################
#
# ########## Class : A collection of attributes that are defined for any objects
# ########## data members, methods
#
# class Complex:                              # --------> Class defined
#     'this class simulates complex numbers'  # --------> description of the class
#     def __init__(self,real, imag):          # --------> constructor class/ Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
#     # 'self' paramter is a ref to the current instance of the class, and is used to access variables that belong to the class
#
#         if(type(real) not in (int, float)) or type(imag) not in (int, float):  # -------> If arg are not int of float, raise error
#             raise Exception('Arguments are not numbers')
#         self.real = real
#         self.imag = imag
#
# # c = Complex(1,1)                          # ---------> Valid Arguments
# # print(c.real, c.imag)
#
# try:
#     c = Complex((1,2,3), [1,2,3])           # ----------> Invalid arguments
#     print(c.real, c.imag)
# except Exception as e:
#     print(e)
#
#
# class Emp:
#     'This class defines Emp heirarchy'
#     def __init__(self, name, designation):
#         # if(type(name) not in (string)) or type(designation) not in (string):
#         #     raise Exception('Arguments are not string')
#         self.name = name
#         self.designation = designation
#
#     def EmpDetails(self, tenure, salary):
#         # name = n.name
#         # des = des.designation
#         print("Name is: " +self.name +"\nDesignation is: " +self.designation + "\nTenure: " +tenure +" years" + "\nSalary is: "+salary)
#
# e1 = Emp("Alison", "Python Developer")
# e1.EmpDetails('3', '$100,000')
#
# ######################################### INHERITANCE ###############################################
# class Vehicle:                                      # ---------> This is the base class / Abstract class
#     def __init__(self,VIN,weight,manufacturer):
#         self.vin_number= VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#
#
#     # def __del__(self):                              # ---------> This is the destructor method
#     #     number_of_vehicles -= 1
#
#     def getWeight(self):
#         return self.weight
#     def getManufacturer(self):
#         return self.manufacturer
#     def vehicleType(self):
#         pass
#
# class Car(Vehicle):
#     number_of_vehicles = 0                          # ---------> This a shared variable (like a static variable in C/C++)
#     def __init__(self, VIN, weight, manufacturer, seats):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#         self.seats = seats
#         print("In init")
#         global number_of_vehicles
#         number_of_vehicles = number_of_vehicles + 1                     # ---------> 1 is added for every instantiation
#
#     def numberOfSeats(self):
#         return self.seats
#
#     def vehicleType(self):
#         return 'Car'
#
# class Truck(Vehicle):
#     def __init__(self, VIN, weight, capacity, seats):
#         self.vin_number = VIN
#         self.weight = weight
#         self.capacity = capacity
#         self.seats = seats
#
#     def transportCapacity(self):
#         return self.seats
#
#     def vehicleType(self):
#         return 'Truck'
#
# a = Car('ABC1', 1000, 'BMW', 4)
# b = Truck('BCD', 1000, 'MAN', 10000)
# c = Car('DEF3', 4000, 'Ford', 4)
# d = Truck('EFG4', 11000, 'Mercedes', 15000)
#
# # del c
#
# for v in [a,b,c,d]:
#     print(a.getWeight(), b.transportCapacity(), c.vehicleType(), d.vehicleType())
# print(Vehicle.number_of_vehicles)
#
#
# ########################### DATA VISUALIZATION #############################
#                         ## Check out PLOTLY library ###
#
# import matplotlib.pyplot as plt
#
# fig = plt.figure("Histogram")
# ax = fig.add_subplot(1,1,1)
# ax.hist([21,12,23,35,45,60,33,22,56,34,28,40,41], bins = 7, facecolor = 'g', normed = True)
# # ----> When creating a histogram:
#     # 1st parameter: list of nos within a certain range - the list in this case
#     # 2nd parameter: no of bins to be created
#     # 3rd parameter: facecolor allows you to set the color of the histogram
#     # 4th parameter: density(normed) - all the data is normalaised (between 0 and 1); it is false by default
#
# plt.title("Distribution")
# plt.xlabel("Range")
# plt.ylabel("Amount")
# plt.show()
#
#
#
#
# fig2 = plt.figure('Box-plot')
# ax1 = fig2.add_subplot(1,1,1)
# ax1.boxplot([21,12,23,35,45,60,33,22,56,34,28,40,41])
# plt.show()
#
#
#
# fig3 = plt.figure('Bar')
# ax2 = fig3.add_subplot(1,1,1)
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_title('Bars')
# ax2.bar([0,1,2,3],[5,10,15,5],[1,1,1.3,1], color = ['b','r'])
#     # When creating a bar diagram:
#         # 1st param: Values are around x axis
#         # 2nd param: Values are around y axis
#         # 3rd param: values are the width of the bars in the graph
#         # 4th param: used to set the color of the bar
# plt.show()
#
#
#
# fig4 = plt.figure('Line')
# ax3 = fig4.add_subplot(1,1,1)
# ax3.set_xlim([-2,10])
# ax3.set_ylim([0,6])
# ax3.set_xlabel('X')
# ax3.set_ylabel('Y')
# ax3.set_title("Lines")
# ax3.plot([-1,2,4,7,8],[5,2,3,4,3], 'r')
# plt.show()
#
#
#
# data = {'Player' : ['Wade', 'James', 'Kobe', 'Curry'],   # --------> Create a dictionary to store values and ease of use
#         'First' : [10, 10, 8, 12],
#         'Second' : [12, 8, 13, 8],
#         'Third' : [15, 12, 8, 8],
#         'Fourth': [18, 20, 15, 8]}
#
# fig5 = plt.figure('Stacked Bar')
# ax4 = fig5.add_subplot(1,1,1)
# bar_width = 0.5
# bars = [i + 1 for i in range(len(data["First"]))]
# ticks = [i + (bar_width/2) for i in bars]
# ax4.bar(bars,
#         data['First'],
#         width = bar_width,
#         label = 'First_Quater',
#         color = '#AA5439')
#
# ax4.bar(bars,
#         data["Second"],
#         width = bar_width,
#         bottom = data['First'],
#         label = 'Second Quarter',
#         color = '#FFD600')
#
# ax4.bar(bars,
#         data["Third"],
#         width = bar_width,
#         bottom = [i+j for i, j in zip(data['First'],data['Second'])],
#         label = 'Third Quarter',
#         color = '#FF9200')
#
# ax4.bar(bars,
#         data["Fourth"],
#         width = bar_width,
#         bottom = [i+j+k for i, j, k in zip(data['First'], data['Second'],data['Third'])],
#         label = 'Third Quarter',
#         color = 'r')
#
# plt.xticks(ticks, data['Player'])
# ax4.set_xlabel("Total")
# ax4.set_ylabel("Player")
# plt.legend(loc = 'Upper right')
# plt.xlim([min(ticks) - bar_width, max(ticks) + bar_width])
# plt.show()
#
#
#
# fig6 = plt.figure('Scatter')
# ax5 = fig6.add_subplot(1,1,1)
# ax5.scatter([-1,0,2,3,5], [2,1,3,0.5,4],[120,200,300,150,30],['r','g','b','#BB5500'])
#     #When creating scatter plots:
#         #1st parameter: X-axis
#         #2nd parameter: Y-axis
#         #3rd parameter: width of the plots (optional)
#         #4th parameter: color of the plots (optional)
# plt.show()
#
# fig7 = plt.figure("Pie")
# ax6 = fig7.add_subplot(1,1,1)
# sizes = [50, 50, 44, 36]
# labels = ['Wade', 'James', 'Kobe', 'Curry']
# explode = (0.1, 0, 0, 0)                    # -------> accentuates the pie portion
# colors = ['red', 'purple', 'yellow', 'blue']
# plt.pie(sizes, explode, labels = labels, colors=colors,autopct='%1.1f%%', shadow = True, startangle = 140)
# plt.axis('equal')
# plt.show()
#
#
#
# ############# PANDAS LIBRARY #############################
#
# import pandas as pd
# df = pd.read_csv('/Users/alisonrosario/Desktop/Python/AirPassengers.csv')
# print(df['AirPassengers'])
# print(df['Time'][135])
#
# names = ["Wade", 'James','Kobe', 'Curry']
# total = [55,50,44,36]
# data_set = list(zip(names,total))
# data_frame = pd.DataFrame(data = data_set, columns = ['Names', "Total"])
# data_frame.to_csv('points.csv', index = True, header = True)
#
#
# ################## NUMPY LIBRARY ##########################
#
# import numpy as np
#
# a1 = np.array([2,1,3,4])                    # -----> 1D array
# a2 = np.array([[1,2,1],[2,1,2],[1,2,3]])    # -----> 2D array
# a3 = np.array([[[1,1,1],[2,2,2]], [[3,3,3],[4,4,4]], [[5,5,5],[6,6,6]]])    # ----> 3D array
#
# a4 = np.arange(10,50,10)        # -------> 1st par: start value; 2nd par: ending value; 3rd par: the jump in between values
# a5 = np.arange(15)
# a6 = np.arange(10,20)
# a7 = np.arange(0.3,2,0.2)
#
# a8 = np.linspace(3, 8, 9)       # -------> linspace() automatically displays nos. from 3 to 8 in 9 steps, though the actual int diff is 5, it calculates how to print it in 9 steps itself
#
# o1 = np.ones((2,2,2))           # -------> ones() creates n-dimensional array of 1s (A 3D array in this case)
# o2 = np.zeros((2,2))            # -------> zeros() creates n-dimensional array of 0s (A 2D array in this case)
#
# e1 = np.empty((3,4))            # -------> returns a 3x4 array with random elements
# e2 = np.eye(3)                  # -------> returns an array with 1s in its diagonals (3x3 in this case)
#
# r1 = np.random.random((5,5))    # -------> returns a 5x5 array with random nos
# # print(r1)
#
# print(a3.ndim)                  # --------> returns dimensions of a3
# print(a2.shape)
# print(a2.size)                  # -------> retruns
# print(e2.dtype)                 # -------> retruns data type (float)
# print(a3.itemsize)              # -------> returns itemsize (8 bytes)
# print(a1.reshape(2,-1))
