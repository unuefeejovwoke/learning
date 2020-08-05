print("hello everyone")#greet user

print("What is your name? :")#ask user for name

myName=input()

print("is good to see you, " +myName)

print("Hey here is the lenght of your name:")
print(len(myName))

print("What is your age :")
myAge = input()

print("you will be " + str(int(myAge) +1) + " in a year")

likes = 0
if likes <5:
    print("increased")
    likes += 1
   
    likes += 1
    print(likes)
    
likes = 0
while likes < 4:
    print("increased")
    likes +=1
    print(likes)
    
name = ""
while name != "your name":
    print("please type ur name")
    name = input()
    
print("thank u")


while True :
    print("pleas ur name")
    name = input()
    if name == "jerry":
        break
print("thank u")
    