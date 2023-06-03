'''ODD or EVEN'''

num = int(input("enter a number: "))
if num%2: print("odd") #here the values other than 0 is True so executes next block
else: print("even")

#In Single Line
print("odd" if num%2 else "even")#if true before block executes else next part executes

#find even or odd without % operator
num = int(input("enter a number: "))
res = num//2
if num == res*2:
      print("Even")
else:
      print("odd")

# using bitwise or
num = int(input("enter a number: "))
print("odd" if num|1==num else "even")

#using bitwise and
num = int(input("enter a number: "))
print("odd" if num&1 else "even")


#using list and index
num = int(input("enter a number: "))
list1 =["even","odd"]
print(list1[num%2])

num = int(input("enter a number: "))


'''note 1 will be added in right shift for empty spaces '''

#try to find even or odd using left and right shift