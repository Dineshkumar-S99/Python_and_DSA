#Swapping the Values

#get input name and say Good Morning + name
name = input("Enter your name: ")
print(f"Good Morning \n{name}")


#swap two values - will take temp variable to store
a=int(input("Enter a value a:"))
b=int(input("Enter a value b:"))
print(f"a:{a} \nb:{b}")
temp=b
b=a
a=temp
print(f"a:{a} \nb:{b}")

#using pointers
a,b=b,a
print(f"a:{a} \nb:{b}")


#with out using above methods
a=int(input("Enter a value a:"))
b=int(input("Enter a value b:"))
a=a+b
b=a-b
a =a-b
print(f"a:{a} \nb:{b}")

#without using + and -
a=int(input("Enter a value a:"))
b=int(input("Enter a value b:"))
a=a*b
b=a//b
a =a//b
print(f"a:{a} \nb:{b}")

#without using any arithmetic operators
#can use bitwise operator use xor operator
a=int(input("Enter a value a:"))
b=int(input("Enter a value b:"))
a=a^b
b=a^b
a =a^b
print(f"a:{a} \nb:{b}")