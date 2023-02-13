#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # # TODO: define a while loop
    # while (x<=5):
    #     print (x)
    #     x=x+1

    # # TODO: define a for loop
    # for x in range(5,10):
    #     print (x)

    # # TODO: use a for loop over a collection
    # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for d in days:
#     #     print(d+1)


#     # TODO: using the enumerate() function to get index 

# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# for i,d in enumerate (days):
#     print (i+1,d)   
  
# if __name__ == "__main__":
#     main()

raw = input("Please enter something and we'll telll you if it's a palindrome: ")
val= raw.lower()
punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
space=""
for x in punctuation:
    val= val.replace(x,space)

print("That value revesered without the punctuation is: " +val)
reverseval= val[::-1]
print(raw+" backwards is " +reverseval)

if val[::-1]== val:
    print("YES! THAT IS A PALINDROME!")
else:
    print("No sorry, that's not a palindrome")
    

