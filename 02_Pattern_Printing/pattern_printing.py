# PATTERN PROGRAMING

1. print based * on the rows based on given input
```python
'''eg: n =3 ->o/p:
*
*
*'''
n = int(input())
for i in range(n):
      print("*")
```

2. now * in coloumns with space
```python
'''eg:n=3
o/p: * * *'''
for i in range(n):
      print("*", end=" ") 
```


3. print * in both coloumns and rows
```python
'''eg: n=3
o/p:
* * *
* * *
* * *'''
for i in range(n):
      for i in range(n):
            print("*",end=" ")
      print()

#or 
for i in range(n):
      print("* "*n)
```

4. if we want to print the letters from string then
```python
s1 = "Dinesh"
for i in range(n):
      print(f"{s1[i]} "*n)
```

5. if we want each letter in each column means
```python
'''eg:THOR
o/p:
T H O R
T H O R
T H O R'''
s2 = "THOR"
for i in range(n):
      for i in s2:
            print(i,end=" ")
      print()
```


6. print alphabets in given format
```python
'''eg:n=3
A B C
D E F
G H I'''
n = int(input())
val =ord("A")
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()
```

7. print repeated alphabets and change alphabets for every row as below
```python
'''eg: n=3
A A A
B B B
C C C'''
n = int(input())
val =ord("A")
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
      val +=1
      if val > ord("Z"):
                  val = ord("A")
      print()

#change values for every column and print same o/p for every row
'''eg: n=4
o/p:
A B C D
A B C D
A B C D
A B C D'''
n = int(input())
for i in range(n):
      val =ord("A")
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()
```


8. if a value is 5 the letters should start from E and go on
```python
'''eg: n=3 -> 3 rows and 3 columns
o/p:
C D E
F G H
I J K

eg:n=100 -> 100 rows and 100 columns
o/p: V W X Y Z ....'''
n = int(input())
res = n
while res>=26:
      res-=26
val =ord("A")+ (res-1)
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()

#or
n = int(input())
val =ord("A")+ (n-1)
while val>=ord("Z"):
      val-=26
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()
```

9. print * for odd and @ for even values of j/ column
```python
'''eg: n=4
o/p:
@ * @ *
@ * @ *
@ * @ *
@ * @ *
'''
n = int(input())
symbol =["*","@"]
for i in range(n):
      for j in range(n):
            print(symbol[j%2],end=" ")
      print()

#or
n = int(input())
for i in range(n):
      for j in range(n):
            print("*" if j%2==0 else "@",end=" ")
      print()
```

10. for every rows now if the row is odd then print * and if the row is even then print @
```python
'''
n = 4
@ @ @ @
* * * *
@ @ @ @
* * * *'''
n = int(input())
for i in range(n):
      for j in range(n):
            print("*" if i%2==0 else "@",end=" ")
      print()
```

11. mix of caps and small letters
```python
'''eg: n=4
A b C d
E f G h
I j K l
M n O P'''
n = int(input())
val = ord("A")
for i in range(n):
      for j in range(n):
            if val%2==0:
                  newval=val+ 32
                  print(chr(newval),end=" ")
            else:
                  print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()

#or
n = int(input())
val = ord("A")
for i in range(n):
      for j in range(n):
            print(chr(val) if j%2==0 else chr(val+32),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()
```

12. print * and @ wise versa
```python
'''eg: n=3
* @ *
@ * @
* @ * '''
n = int(input())
l1 = ["*","@"]
val =0
for i in range(1,n+1):
      for j in range(1,n+1):
            print(l1[val],end=" ")
            val+=1
            if val>1:
                  val=0
      print()

#or
n = int(input())
White=True
for i in range(1,n+1):
      for j in range(1,n+1):
            print("*"if White==True else "@", end=" ")
            White = not White
      print()
```

13. print values for every columns
```python
'''eg: n=4
1 2 3 4
5 6 7 8
9 1 2 3
3 4 5 6`'''
n = int(input())
val =1
for i in range(n):
      for j in range(n):
            print(val, end=" ")
            val+=1
            if val >9:
                  val =1
      print()
```


14. print values -> 1 to 99 as 01 to 09 everything 2 digits
```python
'''eg:n =4
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16'''
n = int(input())
val =1
for i in range(n):
      for j in range(n):
            print(f"0{val}" if val<10 else val , end=" ")
            val +=1
            if val >99:
                  val =1
      print()
```

15. Print the following pattern
```python
'''
* * * * *
* C B A *
* D C B *
* E D C *
* * * * *'''
n=int(input())
val = ord("A")+n//2-1
for i in range(n):
      a = val
      for j in range(n):
            if j==0 or j==n-1 or i==0 or i==n-1:
                  print("*", end=" ")
            else:
                  print(chr(val),end=" ")#here in first loop val is 66 but during 2nd its increased to 67 so now val start printing from C
                  val -=1
                  if val< ord("A"):
                        val = ord("Z")
      print()
      val=a+1
      if val>ord("Z"):
            val= ord("A")
```


16. by using functions fun(n) print the following pattern
```python
'''
A B C D E
B       F
C       G
D       H
E F G H I'''
def fun1(n):
      val = ord("A")
      for i in range(n):
            a = val
            for j in range(n):
                  if j==0 or j==n-1 or i==0 or i==n-1:
                        print(chr(val), end=" ")
                  else:
                        print(" ",end=" ")
                  val+=1
                  if val> ord("z"):
                        val = ord("A")
            print()
            val=a+1

n = int(input())
fun1(n)
```


17. reverse of above
```python
'''
E D C B A
F       B
G       C
H       D
I H G F E'''
#by using functions fun(n)
def fun1(n):
      val = ord("A")+n-1
      for i in range(n):
            a = val
            for j in range(n):
                  if j==0 or j==n-1 or i==0 or i==n-1:
                        print(chr(val), end=" ")
                  else:
                        print(" ",end=" ")
                  val-=1
                  if val< ord("A"):
                        val = ord("Z")
            print()
            val=a+1
            if val>ord("Z"):
                  val= ord("A")

n = int(input())
fun1(n)
```

18. print the following pattern for n =5
```python
'''
* * * * * 
*   a   *
* b c d *
*   e   *
* * * * *'''
n = int(input())
val =ord("a")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    elif i==n//2 or j==n//2:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()
```


19. print the following pattern for n =5
```python
'''
* * a * * 
*   b   *
c d e f g
*   h   *
* * i * *
'''
n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()
```


20. print the following pattern for n =5
```python
'''
* * A * * 
*   B   *
a b C d e
*   D   *
* * E * *'''
#but this will work till 26 coz a-z is 26
n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
        print(chr(val+i),end=" ")
        val+=1
    elif i==n//2:
      print(chr(a+j),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()


#or
n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
      if i==j:
        a+=1
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()
```


21. instead small if every letter is caps then
```python
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if j==n//2:
      if i==j:
        a+=1
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()
```

22. print the following pattern for n =5
```python
'''
* * * * *
* *     *
*   *   *
*     * *
* * * * *'''
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()
```


23. print the following pattern for n =5
```python
'''
* * * * *
*     * *
*   *   *
* *     *
* * * * *'''
n = int(input())
val =n-1
for i in range(n):
  for j in range(n):
    if j==val:
      print("*",end=" ")
      val-=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()

#or
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1 or i+j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()
```


24. print the following pattern for n =5
```python
'''
*
* *
* * *
* * * *
* * * * *'''
n = int(input())
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()

# or
n = int(input())
for i in range(1,n+1):
  print("* "*i)

#or
n = int(input())
for i in range(n):
  for j in range(n):
      if i>=j:
            print("*",end=" ")
  print()
```


25. instead start print characters from A
```python
n = int(input())
val = ord("A")
for i in range(n):
  for j in range(i+1):
    print(chr(val),end=" ")
  val+=1
  print()

# or
val = ord("A")
for i in range(1,n+1):
  print(f"{chr(val)} "*i)
  val +=1
```


26. print the following pattern for n =5
```python
'''
A
B A
C B A
D C B A
E D C B A'''
n = int(input())
val = ord("A")
for i in range(n):
  a=val
  for j in range(i+1):
    print(chr(val),end=" ")
    val-=1
  val=a+1
  print()

#or this goes for certain value only
n = int(input())
for i in range(n):
  val = ord("A")+i
  for j in range(i+1):
    print(chr(val),end=" ")
    val-=1
  print()

#or
n = int(input())
for i in range(n):
  val = ord("A")+i
  while val >ord("z"):
      val -=26
  for j in range(i+1):
    print(chr(val),end=" ")
    val-=1
  print()
```

27. print the following pattern for n=5
``` Python
'''
E D C B A
J I H G F
O N M L K 
T S R Q P
Y X W V U
'''
n = int(input())
val = ord("A")+(n-1)
for i in range(n):
  a=val+(n-1)
  for j in range(n):
    print(chr(val),end=" ")
    val-=1
  val=a+1
  print()
```

28. print the following pattern for n=5
``` Python
'''
A B C D E
J I H G F
K L M N O
T S R Q P
U V W X Y'''
n = int(input())
val = ord("A")
for i in range(1,n+1):
  for j in range(n):
    if i%2==1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(chr(val),end=" ")
      if j==n-1:
        val+=1
      else:val-=1
  val+=(n-1)
  print()
```

29. print the following pattern for n=5
``` Python
'''
A J K T U
B I L S v
C H M R W
D G N Q X
E F O P y'''
```


30. print the following pattern for n=5
``` Python
'''
        *
      * *
    * * *
  * * * *
* * * * *'''
n=int(input())
for i in range(1,n+1):
  for j in range(n):
    if j<n-i:
      print(" ",end=" ")
    else:
      print("*", end=" ")
  print()

#or
n=int(input())
for i in range(1,n+1):
  for j in range(n):
    if i+j>=n-1:
      print("*",end=" ")
    else:
      print(" ", end=" ")
  print()

#using single for loop
n=int(input())
for i in range(1,n+1):
  print(" "*(n-i),end=" ")
  print("*"*(i))

# or
n=int(input())
for i in range(n):
  print(" "*(n-i-1),end=" ")
  print("*"*(i+1))
```

> note: even single mistake could make it equlatrial triangle
``` Python
#equlatrial triangle
n=int(input())
for i in range(n):
  print(" "*(n-i-1)+"* "*(i+1))
```


31. print the following pattern for n=5
``` Python
'''
        A
      B A
    C B A
  D C B A
E D C B A'''
n=int(input())
val=ord("A")
for i in range(1,n+1):
  a=val
  for j in range(n):
    if j<n-i:
      print(" ",end=" ")
    else:
      print(chr(val), end=" ")
      val-=1
      if val >ord("Z"):
            val=ord("A")
  val=a+1
  print()
```

32. print the following pattern for n=5
``` Python
'''
E D C D A
J I H G F
O N M L K
T S R Q P
Y X W V U'''
n=int(input())
val=ord("A")+(n-1)
while val>ord("Z"):
  val-=26
for i in range(n):
  a=val
  for j in range(n):
    print(chr(val),end=" ")
    val-=1
    if val <ord("A"):
      val=ord("Z")
  val=a+(n)
  if val >ord("Z"):
    val=ord("A")
  print()
```

33. print the following pattern for n=5
``` Python
'''
        A
      C B
    F E D
  J I H G
O N M L K'''
n=int(input())
val=ord("A")
for i in range(1,n+1):
  a=val
  for j in range(n):
    if j<n-i:
      print(" ",end=" ")
    else:
      print(chr(val),end=" ")
      val-=1
      if val<ord("A"):
        val=ord("Z")
  val=a+(i+1)
  while val>ord("Z"):
    val-=26
  print()
```


34. print the following pattern for n=5
``` Python
'''
* * * * *
* * * *
* * * 
* *
*''' #by defining a function called r270
def r270(n):
  for i in range(n):
    for j in range(n):
      if j<n-i:
        print("*",end=" ")
      else:#can give else or no need
        print(" ",end=" ")
    print()
r270(int(input()))

#or
def r270(n):
  for i in range(n):
    print("* "*(n-i))
r270(int(input()))

#or
def r270(n):
  for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
r270(int(input()))
```

35. print the following pattern for n=5
``` Python
'''
A F J M O
B G K N
C H L
D I
E'''
def f1(n):
  val=ord("A")
  for i in range(n):
    a=val
    for j in range(n):
      if j<n-i:
        print(chr(val),end=" ")
        val= val+(n-j)
    val = a+1
    print()
f1(int(input()))
```


36. print the following pattern for n=5
``` Python
'''
A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y'''
def f1(n):
  val=ord("A")
  for i in range(n):
    a=val
    for j in range(n):
      print(chr(val),end=" ")
      val+=n
    val = a+1
    print()
f1(int(input()))
```


37. print the following pattern for n=5
``` Python
'''
E J O T Y
D I N S X
C H M R W
B G L Q V
A F K P U'''
n = int(input())
val=ord("A")+(n-1)
count = n
for i in range(n):
  a = val
  c1=count
  for j in range(n):
    print(chr(val),end=" ")
    c1-=1
    val+=c1
  print()
  val = a+1
```

38. print the following pattern for n=5
``` Python
'''
E I L N O
D H K M
C G J
B F
A'''
n = int(input())
val=ord("A")+(n-1)
count = n
for i in range(n):
  a = val
  c1=count
  for j in range(n-i):
    print(chr(val),end=" ")
    c1-=1
    val+=c1
  print()
  val = a-1
```

39. print the following pattern for n=5
``` Python
'''
* * * * *
  * * * *
    * * *
      * *
        *'''
def f1(n):
  for i in range(n):
    for j in range(n):
      #if i<=j:
      if j>=i:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()
f1(int(input()))

#or
for i in range(n):
        print(("  "*i)+("* "(n-i)),end=" ")
'''if given only one space in print normal print then it will show like cone'''
```


40. Print an NP - Non Prymid for n=5
``` Python
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n= int(input())
space = (n-1)
star=0
for i in range(1,n+1):
  print(("  "*space)+("* "*(i+star))+("  "*space))
  star+=1
  space-=1

#or
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print("*",end=" ")
    else:print(" ",end=" ")
  for j in range(i):
    print("*",end=" ")
  print()

#or 
for i in range(n):
  for j in range(n+i):
    if i+j>=n-1:
      print("*",end=" ")
    else:print(" ",end=" ")
  print()


#or
for i in range(n):
  print(("  "*(n-i-1))+("* "*(2*i+1)))
```


41. print the following pattern for n=5
``` Python
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *'''
n=int(input())
for i in range(n):
  for j in range(n):
    if j>=i:
      print("*",end=" ")
    else:print(" ",end=" ")
  for j in range(n-1-i):
    print("*",end=" ")
  print()

#or
n=int(input())
for i in range(n):
  for j in range(2*n-1):
    if j>=i:
      print("*",end=" ")
    else:print(" ",end=" ")
  print()
```

42. print the following pattern for n=5
``` Python
'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1'''
n=int(input())
for i in range(n):
  val =1
  for j in range(n):
    if i+j>=n-1:
      print(val,end=" ")
      if j<n-1:
        val+=1
      else:
        val-=1
    else:print(" ",end=" ")
  for j in range(i):
    print(val,end=" ")
    val-=1
  print()
```

43. print the following pattern for n=5
``` Python
'''
        A
      B C D
    E F G H I
  J K L M N O P
Q R S T U V W X Y'''
val=ord("A")
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=" ")
      val+=1
    else:print(" ",end=" ")
    if val>ord("Z"):
      val =ord("A")
  for j in range(i):
    print(chr(val),end=" ")
    val+=1
    if val>ord("Z"):
      val =ord("A")
  print()
```

44. print the following pattern for n=5
``` Python
'''
        A
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
'''
n=int(input())
val=ord("A")
for i in range(n):
  a= val
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=" ")
      if j<n-1:
        val-=1
    else:print(" ",end=" ")
    if val<ord("A"):
      val =ord("Z")
  for j in range(i):
    val+=1
    print(chr(val),end=" ")
    if val>ord("Z"):
      val =ord("A")
  print()
  val =a+1
```

45. for n=5 print the following pattern
``` Python
'''
    *    
  * * *  
* * * * *'''
n=int(input())
for i in range(n):
  for j in range(i+1):
    if i+j>=n-1:
      print("*",end=" ")
    else:print(" ",end=" ")
  print()

#or
for i in range(n//2+1):
  for j in range(n//2+1+i):
    if i+j>=n//2:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
```

46. print the following pattern for n=5
``` Python
'''
* * * * *
  * * *
    *'''
n = int(input())
for i in range(n):
  for j in range(n-i):
    if j>=i:#or i<=j
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#or 
for i in range(n):
  for j in range(2*n-1-i):
    if i<=j:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
```

47. print the following pattern for n=5
``` Python
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=int(input())
l1=[]
for i in range(n):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+l1[-2::-1]))

#or
n=int(input())
l1=[]
for i in range(n):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+list(reversed(l1[:-1]))))

#or
n=int(input())
l1=["  "*(n-i-1)+"* "*(2*i+1)for i in range(n)]
print("\n".join(l1+l1[-2::-1]))
```

48. print the following pattern for n=5
``` Python
'''
        *
      * * *
    * * * * *
  * * * * * * *
P Y S P I D E R S
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=int(input())
l1=[]
for i in range(n):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+["P Y S P I D E R S"]+l1[-2::-1]))
```

49. print the following pattern for n=5
``` Python
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
P Y S P I D E R S
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *'''
n=int(input())
l1=[]
for i in range(n):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+["P Y S P I D E R S"]+l1[::-1]))


#try this
n=int(input())
l1=[]
for i in range(n-1):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+["P Y S P I D E R S"]+l1[::-1]))
```

50. print the following pattern for n=5
``` Python
'''
      *
    * * *
  * * * * *
* * * * * * *
S P I D E R S
* * * * * * *
  * * * * *
    * * *
      *
'''
n=int(input())
l1=[]
for i in range(n):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+["S P I D E R S"]+l1[::-1]))
```

51. print the following pattern for n=5
``` Python
'''
        *
      * * *
    * * * * *
      * * *
        *
'''
n=int(input())
l1=[]
for i in range(n//2+1):
  l1.append("  "*(n-i-1)+"* "*(2*i+1))
print("\n".join(l1+l1[-2::-1]))

#or
n=int(input())
l1=[]
for i in range(n//2+1):
  l1.append("  "*(n//2-i)+"* "*(2*i+1))
print("\n".join(l1+l1[-2::-1]))
```

52. print the following pattern for n=5
``` Python
'''
        *
      *   *
    *       *
      *   *
        *
        '''

n = int(input())
for i in range(n):
  for j in range(n):
    if i+j==(n//2) or j-i==(n//2) or i-j==(n//2) or i+j==n+(n//2)-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
```

53. print the East Pyramid for n =5
``` Python
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''
n =int(input())
l1=[]
for i in range(1,n+1):
  l1.append("* "*i)
print("\n".join(l1+l1[-2::-1]))

#without list
n =int(input())
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()
for i in range(n-1):
  for j in range(n-i-1):
    print("*",end=" ")
  print()

#with two for loop
n =int(input())
for i in range(2*n-1):
  for j in range(n):
    if i>=j and i+j<=2*n-2:
      print("*",end=" ")
  print()

#using one for loop
n =int(input())
for i in range(2*n-1):
  if i<n-1:
    print("* "*(i+1))
  else:
    print("* "*(2*n-1-i))

#or
n=int(input())
a=1
for i in range(2*n-1):
  print("* "*a)
  if i<n-1:a+=1
  else:a-=1
```

54. print the following pattern for n=5
``` Python
'''
*
* *
* * *
* *
*
'''
n =int(input())
l1=[]
for i in range(1,((n+1)//2)+1):
  l1.append("* "*i)
print("\n".join(l1+l1[-2::-1]))

#without list using loops
n =int(input())
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#with one for loop
n =int(input())
for i in range(n):
  if i<=n//2:
    print("* "*(i+1))
  else:
    print("* "*(n-i))

#or
n=int(input())
a=1
for i in range(n):
  print("* "*a)
  if i<n//2:a+=1
  else:a-=1
```


> some own exapmles trials
``` Python
n =int(input())
val = ord("A")
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()

#2
n =int(input())
for i in range(n):
  val = ord("A")
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()

#3
n =int(input())
val=ord("A")+n-1
for i in range(n):
  a = val
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val-=1
    else:
      print(" ",end=" ")
  val =a-1
  print()

#4
n=int(input())
a=1
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(a,end=" ")
      a+=1
  print()

#5
n=int(input())
val=ord("A") 
for i in range(n):
  a = val
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
    else:
      print(" ",end=" ")
  val +=1
  print()
```

55. print the following pattern for n=5
``` Python
'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1'''
n =int(input())
val = 1
for i in range(2*n-1):
  a = val
  for j in range(n):
    if i>=j and i+j<=2*n-2:
      print(val,end=" ")
      val-=1
  if i<n-1:
    val = a+1
  else:
    val = a-1
  print()
```

56. print the following pattern for n=5
``` Python
'''
01
02 03
04 05 06
07 08
09
'''
n=int(input())
a=1
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(f"0{a}",end=" ")
      a+=1
  print()
```

57. print the following pattern for n=5
``` Python
#SPIDERMAN
'''
S
P I
D E R
M A
N'''
n=int(input())
S = "SPIDERMAN"
a = 0
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(S[a],end=" ")
      a+=1
  print()
```

58. print the following pattern for n=5
``` Python
'''
A
1 B
C 2 D
3 E
F
'''
n = int(input())
a = 0
num = 1
val = ord("A")
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1 and a%2==0:
      print(chr(val),end=" ")
      val+=1
    elif i>=j and i+j<=n-1 and a%2!=0:
      print(num,end=" ")
      num+=1
    else:
      print(" ",end=" ")
    a +=1
  print()
```

59. print the following pattern for n=5
``` Python
'''
A
B A
C B A
B A
A'''
n=int(input())
a = 1
val = ord("A")
for i in range(n):
  a = val
  for j in range(n//2+1):
    if i>=j and i+j<=n-1:
        print(chr(val),end=" ")
        val-=1
  print()
  if i<n//2:
    val = a+1
  else:
    val = a-1
```

60. print the following pattern West Pyramid for n=5
``` Python
'''
when n =5
        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *'''
#using list
n =int(input())
l1=[]
for i in range(1,n+1):
  l1.append("  "*(n-i)+"* "*i)
print("\n".join(l1+l1[-2::-1]))

#without using list and print by using for loop
n =int(input())
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
for i in range(1,n):
  for j in range(n):
    if i<=j:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#using two for loops
n =int(input())
for i in range(2*n-1):
  for j in range(n):
    if i+j>=n-1 and i-j<=n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#without using list and just with single for loop
n =int(input())
a=1
for i in range(2*n-1):
  print("  "*(n-a)+"* "*a)
  if i<n-1:
    a+=1
  else:
    a-=1
```


>note: single change in space will make it diamond
``` Python
'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *'''
n =int(input())
a=1
for i in range(2*n-1):
  print(" "*(n-a)+"* "*a)
  if i<n-1:
    a+=1
  else:
    a-=1
```


61. print the following pattern for n=5
``` Python
'''
    *
  * *
* * *
  * *
    *'''
n =int(input())
for i in range(n):
  for j in range(n//2+1):
    if i+j>=n//2 and i-j<=n//2:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  ```