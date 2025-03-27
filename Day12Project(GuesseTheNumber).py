import random
print ("Welcome to the Number Guessing game! \n I'm thinking in a number between 1 and 100.")

difficult = input("Choos a difficult. Type 'Easy' or 'Hard': ").title()
loop = ''
number = random.randint(1, 100)
if difficult == 'Easy':
    loop = 10
elif difficult == 'Hard':
    loop = 5
else:
    print("Invalid difficult level. Defauting to 'Easy'")
    loop = 10
    

for guess in range (loop):
    print(number)