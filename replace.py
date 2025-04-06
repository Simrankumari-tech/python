word = "donkey"

with open("replace.txt" , "r") as  f :
 content = f.read()

contentnew = content.replace(word ,"#####" ) 

with open("replace.txt" , "w") as f:
 f.write(contentnew)