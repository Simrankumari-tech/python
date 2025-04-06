
def main():
  try:
    a= int(input("hey , enter a no. : "))
    print(a)

  except Exception as e:
    print(e)  

  finally:
    print("finally")

main()      