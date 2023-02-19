raw = input("Please enter something and we'll telll you if it's a palindrome: ")
val= raw.lower()
punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
space=""
for x in punctuation:
    val= val.replace(x,space)
    
reverseval= val[::-1]
print(raw+" backwards is " +reverseval)

if val[::-1]== val:
    print("YES! THAT IS A PALINDROME!")
else:
    print("No sorry, that's not a palindrome")
