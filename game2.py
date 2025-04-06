import random
n = random.randint(1,100)
a = -1
guess =0

while(a != n):
  guess += 1
  a = int(input("guess a number : "))
  if(a>n):
    print("lower no. pls ")
  else :
    print("higher number pleas : ")

print(f"you have guessed the number {n} correctly in {guess} attempts ")     
