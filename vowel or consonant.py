A=['a','e','i','o','u','A','E','I','O','U'];
B=str(input(""))
if(B in A):
  print("Vowel")
elif(B.isalpha()):
  print("Consonant")
else:
  print("invalid")
