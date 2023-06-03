#create string combinations:
# eg: if ab then its ba
# eg: if abc then its abc acb bca bac cab cba

#eg: if abcd then abcd then its abcd acdb adbc abdc 

def word_combinations(s1):
      if len(s1) == 1:
            return s1
      else:
            return [s1[i] + p for i in range(len(s1)) for p in word_combinations(s1[:i] + s1[i+1:])]
s1=input("Enter the string: ")
print(word_combinations(s1))



#eg: if abcd then its abcd acdb adbc abdc bacd badc bdac bcad cbad cbda cdab cdba dbac dbca dcba dcab dacb dab
#eg: if abc then its abc acb bac bca cab cba
#eg: if ab then its ab ba
#eg: if a then its a
#eg: if "" then its ""
#eg: if 123 then its 123 132 213 231 312 321

#eg: if abcd then its abcd acdb adbc abdc bacd badc bdac bcad cbad cbda cdab cdba dbac dbca dcba dcab dacb dab

#withoput using recursion:

def word_combinations(s1):
      if len(s1) == 1:
            return s1
      else:
            return [s1[i] + p for i in range(len(s1)) for p in word_combinations(s1[:i] + s1[i+1:])]