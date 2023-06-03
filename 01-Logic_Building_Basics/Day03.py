# Number Series

# print first n even numbers for given value of n
n = int(input())
count = 0
val = 0
while count < 5:
      if val%2==0:
            print(val,end=" ")
            count+=1
      val+=1
print()

#print without 0
n = int(input())
count = 0
val = 1
while count < 5:
      if val%2==0:
            print(val,end=" ")
            count+=1
      val+=1
print()


#with for loop
n = int(input())
for i in range(1,n*2+1):
      if i%2==0:
            print(i,end=" ")
print()


#or just mul by 2
n = int(input())
for i in range(n):
      print(i*2,end=" ")
print()

#first n odd numbers
n = int(input())
for i in range(n):
      print(i*2+1,end=" ")
print()

#print one even number and one odd number
n = int(input())
val = 1
for i in range(n):
      if i%2==0:
            print(val*2,end=" ")
            val+=1
      else:
            print(i,end=" ")

#or
n = int(input())
for i in range(n):
      if i%2==0:print(i+2,end=" ")
      else:print(i,end=" ")
print()


#add odd numbers to previous num eg: 2,5,10,17,26
n = int(input())
for i in range(1,n+1):
      print(i**(2)+1,end=" ")
print()


#eg: 0,7,26,63,124
n = int(input())
for i in range(1,n+1):
      print((i**3)-1,end=" ")
print()


#0,1,1,2,3,5,8,13,21,34,55,89,144
n = int(input())
a,b = 0,1
for i in range(n):
      print(a,end=" ")
      a,b = b,a+b


# fibonocci series using recursion
def f1(n,a=0,b=1):
      if n >0:
            print(a,end=" ")
            f1(n-1,b,a+b)
f1(8)

#or
def f1(n,a=0,b=1):
      print(a,end=" ")
      if n >1:
            f1(n-1,b,a+b)
f1(8)


#fibonocci series in reverse order using recursion
def f1(n,a=0,b=1):
      if n >0:
            f1(n-1,b,a+b)
            print(a,end=" ")
print()
f1(8)


#when n is 5 find first 5 even numbers using recursion
def f1(n,a=0):
      if n >0:
            print(a,end=" ")
            f1(n-1,a+2)
f1(5)


#or
def f1(n):
      if n>0:
            f1(n-1)
            print(n*2,end=" ")
f1(5)
print()

#in reverse order
def f1(n):
      if n>0:
            print((n-1)*2,end=" ")
            f1(n-1)
f1(5)
print()


#when n is 5 find first 5 odd numbers using recursion
def f1(n,a=1):
      if n >0:
            print(a,end=" ")
            f1(n-1,a+2)
f1(5)


#this will always retun 1
def fun(n):
    if n<0:
        return 1
    return fun(n-1)
print(fun(5)) #tracing the code will show that it will always return 1, because it will never reach the base case


def fun(n):
    if n<0:
        print(1)
    return fun(n-1)
fun(5)##this will give error and print 1 infinite times till recursion limit is reached


#find the number of odd and even numbers in a given number
n = int(input())
odd = 0
even = 0
while n>0:
      rem = n%10
      if rem%2==0:
            even+=1
      else:
            odd+=1
      n//=10
print("odd:",odd,"even:",even)


#find the max and min digit in a given number
n = int(input())
max = 0
min = 9
while n>0:
      rem = n%10
      if rem>max:
            max = rem
      if rem<min:
            min = rem
      n//=10
print("max:",max,"min:",min)


#print the given number in reverse order
n = int(input())
while n>0:
      rem = n%10
      print(rem,end="")
      n//=10
print()


#find the given number is prime or not
#using for loop
n = int(input())
if n==1:
      print("not prime")
for i in range(2,n):
      if n%i==0:
            print("not prime")
            break
      else:
            print("prime")
            break

#using recursion
def f1(n,i=2):
      if n<i:
            return " not a prime"
      if i<n:
            if n%i==0:
                  return "not prime"
            else:
                  f1(n,i+1)
      else:
            return "prime" 
            
#or
def f1(n,i=2):
      if n<i:
            return " not a prime"
      if i<n:
            if n%i==0:
                  return "not prime"
            return f1(n,i+1)
      else:
            return "prime"
print(f1(int(input())))


#print first n prime numbers
n = int(input())
count = 0
val = 2
while count < n:
      for i in range(2,val):
            if val%i==0:
                  break
      else:
            print(val,end=" ")
            count+=1
      val+=1
print()

#or
n = int(input())
l1 = []
val = 2
while len(l1) < n:
      for i in range(2,val):
            if val%i==0:
                  break
      else:
            l1.append(val)
      val+=1
print(*l1)#if we give without * it will print as list


# find the factorial of a given number
n = int(input())
fact = 1
for i in range(1,n+1):#or with (n,1,-1)
      fact*=i
print(fact)


#factorial using recursion
def f1(n):
      if n==0:
            return 1
      return n*f1(n-1)
print(f1(int(input())))

def f1(n):
      if n<2:
            return 1
      return n*f1(n-1)
print(f1(int(input())))

#or
def f1(n,fact=1):
      if n>1:
            return f1(n-1,fact*n)
      return fact
print(f1(int(input())))