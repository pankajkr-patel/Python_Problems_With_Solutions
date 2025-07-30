
# 1. Print numbers from 1 to 10
for i in range(1 , 11):
      print(i, end=" ")

# 2. Print even numbers between 1 and 20

# mathod :1
for i in range(2,21,2):
      print(i , end=" ")
# mathod :2
for i in range(1,21):
      if i%2==0:
            print(i , end=" ")

# 3. Calculate the sum of numbers from 1 to 100
sum=0
for i in range(1,101):
      sum+=i
print("total :- ",sum)

# 4. Print each character of a string
text = "Pankaj Patel"
for char in text:
      print(char, end=" ")

# 5. Print multiplication table of a number
num=int(input("Enter any number :- "))
for i in range(1,11):
      print(num,"x",i,"=",num*i)


# 6. Count vowels in a string
text="HellO World"
newtext=text.lower()
vowel='aeiou'
count=0
for char in newtext:
      if char in vowel:
            count+=1
print("Vowels :- ",count)

# 7. Check if a number is prime
num=int(input("Enter Number :- "))
if num<=1:
      print("Not Prime Number")
else:
      for i in range(2,num):
            if num%i==0:
                  print("It`s Not Prime Number")
                  break
      else:
                  print("Prime Number")


# *********************** While Loop *****************************
# 8. Print Table using while loop
num=int(input("Enter the Number :- "))
i=1
while i<=10:
      print(num,"x",i,"=",num*i)
      i+=1

#9. Print 1 to 10
i=1
while i<=10:
      print(i)
      i+=1

# 10. Sum of First N Natural Numbers
total_sum=0
num=int(input("Enter Number :- "))
i=1
while i<=num:
      total_sum= total_sum+i
      i+=1
print(total_sum)

# 11. Print Even Numbers Between 1 and 50
i=1
while i<=50:
      if i%2==0:
            print(i)
      i+=1

# 12. Factorial of a Number 
num=int(input("Enter Number :- "))
i=1
factorial=1
if i<0:
      print("Invalid Number, Please enter Positive Number")
else:
      while i<=num:
            factorial=factorial*i
            i+=1
      print("factorial of",num,"is", factorial)

# 13. Print this
# *
# **
# ***
# ****
# *****

for i in range(1,6):
      for j in range(1,i+1):
            print("*",end=" ")
      print()


# 14. Print This 
# *****
# ****
# ***
# **
# *
for i in range(1,6):
      for j in range(6,i,-1):
            print("*" , end=" ")
      print()

# 15. Print This
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
      for j in range(1,i+1):
            print(j , end=" ")
      print()

# 16. Print This
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
      for j in range(1,i+1):
            print(i , end=" ")
      print()

#  17. Print this     
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,6):
      for j in range(5,i,-1):
            print(" ", end=" ")
      for k in range(i):
            print("*",end=" ")
      print()



