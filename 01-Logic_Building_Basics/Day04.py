#s1= "SpiDerMAN !s @ gOOD PERSON"
#function to convert string to lowercase
'''def convert_to_lower(s1):
      return s1.lower()

s1=input("Enter a string: ")
print(convert_to_lower(s1))'''

#without using inbuilt function
def convert_to_lower(s1):
  s2=""
  for i in s1:
    if ord(i)>=65 and ord(i)<=90:
      s2+=chr(ord(i)+32)
    else:
      s2+=i
  return s2

'''s1=input("Enter a string: ")
print(convert_to_lower(s1))

#function to convert string to uppercase
def convert_to_upper(s1):
      s2=""
      for i in s1:
            if ord(i)>=97 and ord(i)<=122:
                  s2+=chr(ord(i)-32)
            else:
                  s2+=i
      return s2

s1=input("Enter a string: ")
print(convert_to_upper(s1))'''

#function to convert string to title case
def convert_to_title(s1):
      convert_to_lower(s1)
      s2=""
      '''for i in range(len(s1)):
            if i==0 and ord(s1[i])>=97 and ord(s1[i])<=122:
                  s2+=chr(ord(s1[i])-32)
            elif s1[i-1]==" " and ord(s1[i])>=97 and ord(s1[i])<=122:
                  s2+=chr(ord(s1[i])-32)
            else:
                  s2+=s1[i]
      return s2'''

'''s1=input("Enter a string: ")
print(convert_to_title(s1))'''

#print(s1.title())

'''def convert_to_title(s1):
      s2=""
      for i in s1:
            if ord(i)>=65 and ord(i)<=90:
                  s2+=chr(ord(i)+32)
            else:
                  s2+=i

      s3=""
      for i in range(len(s2)):
            if i==0 and ord(s2[i])>=97 and ord(s2[i])<=122:
                  s3+=chr(ord(s2[i])-32)
            elif s2[i-1]==" " and ord(s2[i])>=97 and ord(s2[i])<=122:
                  s3+=chr(ord(s2[i])-32)
            else:
                  s3+=s2[i]
      return s3

s1=input("Enter a string: ")
print(convert_to_title(s1))

print(s1.title())'''


#or can be written as
'''def convert_to_title(s1):
      print(s1)
      s2=""
      for i in range(len(s1)):
            if i==0 or ("0"<=s1[i-1]<="9") or (not("A"<=s1[i-1]<="Z")) and (not("a"<=s1[i-1]<="z")):
                  if "a"<=s1[i]<="z":
                        s2+=chr(ord(s1[i])-32)
                  else:
                        s2+=s1[i]
            else:
                  if "A"<=s1[i]<="Z":
                        s2+=chr(ord(s1[i])+32)
                  else:
                        s2+=s1[i]
      return s2

s1=input("Enter a string: ")
print(convert_to_title(s1))'''


#function to convert swap case
'''def convert_to_swap(s1):
      s2=""
      for i in s1:
            if "A"<=i<="Z":
                  s2+=chr(ord(i)+32)
            elif "a"<=i<="z":
                  s2+=chr(ord(i)-32)
            else:
                  s2+=i
      return s2

s1=input("Enter a string: ")
print(convert_to_swap(s1))'''


#function to reverse a string
'''def reverse_string(s1):
      s2=""
      for i in range(len(s1)-1,-1,-1):
            s2+=s1[i]
      return s2'''

#function to reverse a string without using inbuilt function
'''def reverse_string(s1):
      s2=""
      for i in s1:
            s2=i+s2
      return s2

s1=input("Enter a string: ")
print(reverse_string(s1))'''


#function to reverse words in a string
'''def reverse_words(s1):
      s2=""
      for i in s1:
            if i==" ":
                  s2+=" "
            else:
                  s2=i+s2
      return s2

s1=input("Enter a string: ")
print(reverse_words(s1))'''


#function to reverse words in a string without using inbuilt function
'''def reverse_words(s1):
      s2=""
      for i in s1:
            if i==" ":
                  s2=" "+s2
            else:
                  s2=i+s2
      return s2

s1=input("Enter a string: ")
print(reverse_words(s1))'''

#function to reverse words in a string without using inbuilt function
'''def reverse_words(s1):
      for words in s1:
            s2=""
            for i in words:
                  s2=i+s2
            print(s2,end=" ")



s1=input("Enter a string: ").split()
reverse_words(s1)'''

#in one line
#print(" ".join([i[::-1] for i in s1.split()]))
'''
or

l1=s1.split()
l2=[]
for i in l1:
      l2.append(i[::-1])
      print(" ".join(l2))
      
or
s2=" ".join(s1.split()[::-1])

or
s2=" ".join([i[::-1] for i in s1.split()])'''

#or
'''s1=input("Enter a string: ")
s2=""
s3=""
for i in s1:
      if i==" ":
            s2+=" "+s3
            s3=""
      else:
            s3=i+s3
s2+=" "+s3
print(s2)'''


#complex
'''s2=""
s3=""
for i in s1:
      if i!=" ":
            s3=i+s3
      else:
            s2+=s3+i
            s3=""

else:
      if s3!=" ":
            s2+=s3
print(s2)'''


#take an user input like "ab" now try to print the combinations of the string like "ab","ba"
#eg if user input is "abc" then output should be "abc","acb","bac","bca","cab","cba"

#function to print all combinations of a string
'''def combinations(s1):
      for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                  print(s1[i]+s1[j],end=" ")
      print()

s1=input("Enter a string: ")
combinations(s1)'''

#function to print all combinations of a string
'''def combinations(s1):
      val = len(s1)
      for i in range(1, val+1):
            for j in range(val-i+1):
                  print(s1[j:j+i],end=" ")
      print()

s1=input("Enter a string: ")
combinations(s1)'''

#string combinations eg if user input is "abc" then output should be "abc","acb","bac","bca","cab","cba"
'''def combinations(s1):
      for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                  print(s1[i]+s1[j],end=" ")
      print()     

s1=input("Enter a string: ")
combinations(s1)'''

#