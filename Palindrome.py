#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
name=input("Enter a string: \n")
string=name.lower()
original=[]
reverse=[]
for i in range(0, len(string)):
  original.append(string[i])
for i in range(1, len(string)+1):
  reverse.append(string[-i])
  if original==reverse:
    print("Palindrome")
  else:
    print("Not Palindrome")

    
inp = input("Enter a string: ")
if inp[::-1] == inp:
  print("Your entered string is palindrome.")
else:
  print("Your string is not palindrome. ")
