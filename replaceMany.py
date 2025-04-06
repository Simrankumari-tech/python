words = ["donkey" , "ganda" , "bad"]

with open("replaceMany.txt" , "r") as f:
  content = f.read()

for word in words:
  content = content.replace(word, "#" * len(word))

with open("replaceMany.txt" , "w") as f :
  f.write(content)    
  