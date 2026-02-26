# def greet( ):
#     print("good morning")
# greet()
# greet()
# greet()
# greet()

# def marriage(boy,girl):
#     print(f"boy is {boy}")
#     print(f"girl is {girl}")
#     print(f"{boy} married {girl} ")
# marriage("manjunath" , "shwetha")

# def marriage(Girl , boy="Boy"):
#     print(f"{boy} marries {girl}")
# marriage("rose")

# def tables(num):
#     for i in range(1,11):
#         print(f"{num}X{i}={num*i}")
# tables(25)
# tables(19)

# def func(num):
#     return int(str(num)*5)
# a=100
# b=a+func(5)
# print(b)

# def add(*num):
#     return sum(num)
# print(add(1,2,3))

# l="this is a computer"
# print(l.split())

#key word argument
# def display_info(name,age):
#     print(f"name is {name} and age is {age}")
# display_info(name="poorvith" , age=18.5)

# def total_sun(*num):
#     result=0
#     for i in num:
#         result+=i
#     return result
# print(total_sun(1,2,3,4))

# def student_info(**kwargs):
#     for key , values in kwargs.items():
#         print(f"{key} ;{values}")
# student_info(name="poorvith" , age=19 , course="python")

# add=lambda x : 2**x
# print(add(3))                             

# def add (x,y):
#     print(x+y)
# add(2,3)
# add(3,5)

# def check(num):
#     if num%2==0:
#         print(f"{num} is even ")
#     else:
#         print(f"{num} is odd")
# check(7)
# check(8)

# def largest(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         print(f"{num1} is largest")
#     elif num2>num1 and num2>num3:
#         print(f"{num2} is largest")
#     else:
#         print(f"{num3} is largest")
# largest(9,6,10)
  
# def square(num):
#     print(f"square of the given num is {num**2}")
# square(25)

# double = lambda x : x**2
# print(double(25))

# def greet(name):
#     print(f"good morning {name}")
# greet("poorvith")

# def list_elements(elements):
#     print(sum(elements))
# list_elements([2,3,4,5])

# def add(*elements):
#     return sum(elements)
# print(add(1,2,3,4))

# a = lambda elements : sum(elements)
# print(a([1,2,3,4]))

# def vowels_count(string):
#     count=0
#     for i in string:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#             count+=1
#             return count
# print(vowels_count("aeiou"))

# def count_vowels(string):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in string:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels("poorvith"))

# def factorial(num):
#     result=1
#     for i in range(1,num+1):
#         result*=i
#     return result
# print(factorial(5))
    
# def reverse(string):
#     return string[::-1]
# print(reverse("eye"))

# def reverse_string(string):
#     print(string[::-1])
# reverse_string("poorvith")


# def palindrome(string):
#     if string==string[::-1]:
#         print(f"{string} is a palindrome")
#     else:
#         print(f"{string} is not a palindrome")
# palindrome("eye")
# palindrome("sky")

# def prime(num):
#     if num>1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")

# prime(11)
# prime(21)


# def num(fabonacci):
#     a,b=0,1
#     for i in range (1,fabonacci+1):
#         print(a , end=" ")
#         a,b=b,a+b
# num(10)
    
        

# def cal(num1,num2,operator):
#     if operator == "+":
#         return num1+num2
#     elif operator == "-":
#         return num1-num2
#     elif operator == "*":
#         return num1*num2
#     elif operator == "/" and num2!=0:
#         return num1/num2
#     else:
#         return "answer is not defined"
# print(cal(10,5,"+"))



# def count(upper,lower):
#     u_c=0
#     l_c=0
#     for char in upper:
#         if char.isupper():
#             u_c+=1
#     for char in lower:
#         if char.islower():
#             l_c+=1
#     return u_c,l_c
# print(count("POORvit","poorvith"))

# def num(number):
#     total=0
#     for i in range (1,number+1):
#         total+=i
#     return total
# print(num(1234))
  

# def num(number):
#     total=0
#     while number>0:
#         digit=number%10
#         total+=digit
#         numbr//=10
#     return total
# print(num(1234))


# def average(*num):
#     if len(num)==0:
#         return 0
#     else:
#         return sum(num)/len(num)
# print(average(10,20,30))
# num=10,20,30
# print(sum(num))
# print(len(num))
# print(sum(num)/len(num))

# def operation(num1,num2,operator):
#     if operator=="+":
#         return num1+num2
#     elif operator == "-":
#         return num1-num2
#     elif operator == "*":
#         return num1*num2
#     elif operator =="/":
#         if num2!=0:
#             return num1/num2
#         else:
#             return "ans is N.D"
#     elif operator =="//":
#         if num2!=0:
#             return num1//num2
#         else:
#             return "ans is N.D"
#     elif operator == "%":
#         if num2!=0:
#             return num1%num2
#         else:
#             return "ans is N.D"
#     else:
#         return "invaild operator"
# print(operation(10,9,"//"))
# print(operation(560,600,"//"))

# def letter(string):
#     u_c=0
#     l_c=0
#     for char in string:
#         if char.isupper():
#             u_c+=1
#         elif char.islower():
#             l_c+=1
#     return u_c,l_c
# print(letter("POORvith"))


# def duplicate(num1,num2,num3,num4):
#     if num1==num2 or num1==num3 or num1==num4:
#         return num2,num3,num4
#     elif num2==num1 or num2==num3 or num2==num4:
#         return num1,num3,num4
#     elif num3==num1 or num3==num2 or num3==num4:
#         return num1,num2,num4
#     elif num4==num1 or num4==num2 or num4==num3:
#         return num1,num2,num3
# print(duplicate(3,3,3,2))
# print(duplicate.pop(3,1,1))
      
# def duplicate(list):
#     result=[]
#     for item in list:
#         if item not in result:
#             result.append(item)
#     return result
# print(duplicate([1,2,3,4,5,1,2,3,4,5]))

# a=lambda x:x**3
# print(a(2))

# def compute(a,b):
#     return a**2+b**2+2*a*b
# print(compute(2,3))

# compute=lambda a,b : a**2+b**2+2*a*b
# print(compute(2,3))

# def abssolte(num):
#     if num < 0:
#         return -num
#     else:
#         return num
# print(abssolte(-5))
# print(abssolte(10))

# absolute=lambda num : -num if num < 0 else num
# print(absolute(-5))
# print(absolute(10))

# def is_multiple (num1,num2):
#     if num1%num2==0:
#         return True
#     else:
#         return False
# print(is_multiple(10,5))
# print(is_multiple(10,3))



# is_multiple=lambda num1,num2 : True if num1%num2==0 else False
# print(is_multiple(10,5))
# print(is_multiple(10,3))
# Write a function to convert Celsius to Fahrenheit.
# def faranheit(celcius):
#     return (celcius*9/5)+32
# print(faranheit(37)) 


# Create a function that returns area of a circle using radius.
# def area(radius):
#     return 3.14*radius**2
# print(area(1))
