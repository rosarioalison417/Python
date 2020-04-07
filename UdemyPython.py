# 
# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("The config is: "+ self.cpu + self.ram)
#
# c1 = Computer('i7','16')         # --------->define c1 as Computer object
# c2 = Computer('i5','8')
#
# c1.config()     # -------->c1 object is passed as self to  config
# c2.config()

# class Employee:
#     def __init__(self, name, desig, tenure):
#         self.name = name
#         self.desig = desig
#         self.tenure = tenure
#
#     def EmpRetention(self):
#         if(self.tenure <= 5 and self.tenure >8):
#             print("Employee " +self.name +"is a Loyal Emp")
#         elif(self.tenure <= 8):
#             print("Employee "+self.name+ " is a Very loyal")
#         else:
#             print("Employee "+self.name+ " is a Newer Employee")
#
# e1 = Employee('Brian', 'BA', 4)
# e2 = Employee('Stacy', 'Sr.Dev', 12)
# e3 = Employee('Jane', 'Dev', 6)
#
# e1.EmpRetention()
# e2.EmpRetention()
# e3.EmpRetention()
import math
class RealImag:
    def __init__(self, real = 0, imag = 0):
        self.__real = real      # ------------> '__' DoubleUnderscore is used to declare private  variables
        self.__imag = imag

    def setReal(self,value):
        if type(value) not in (int, float):
            raise Exception(' Real part is not a number')
        self.__real = value
    def setImag(self,value):
        if type(value) not in (int, float):
            raise Exception('Imag part is not a number')
        self.__imag = value
    def getReal(self):
        return self.__real

    def getImag(self):
        return self.__imag

    def getModulus(self):
        return math.sqrt(self.getReal() + self.getReal() * self.getImag() * self.getImag())

    def getPhi(self):
        return math.atan2(self.getImag(), self.getReal())

c1 = RealImag(-3,4)

# c1.setReal([2,3,4,5])
# c1.setImag(3.5)
print(c1.getModulus())
print(c1.getPhi())
