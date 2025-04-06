import random 
def game():
  print("you are playing game ")
  score = random.randint(1,89)

  with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore != ""):
      hiscore = int(hiscore)
    else :
      hiscore = 0  

  print(f"your scpre is : {score}")
  if(score > hiscore):
    with open("hiscore.txt" , "w") as f:
      f.write(str(score))
  return score    
game()      

# import random 
# def game():
#   print("you are playing th game..")
#   score = random.randint(1,79)

#   with open("hiscore.txt") as f:
#     hiscore = f.read()
#     if(hiscore != ""):
#       hiscore = int(hiscore)

#     else :
#      hiscore=0  

#   print(f"your score : {score}")
#   if(score > hiscore):
#      with open("hiscore.txt" , "w") as f:
#       f.write(str(score))
  
#   return score


# game()