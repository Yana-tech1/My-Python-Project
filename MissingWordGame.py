#The missing word game
import random
import time
choices = ["is","am","are"]
print("Welcome is the missing word game\n")
#Subprogram 
def question():
    answer = input("\nWhich is the missing word?\nis\nam\nare\n")
    return answer
    
#Question1
Question1 = "\nI ___ late."
print(Question1)
answer = question()
if answer == choices[1]:
    print("Correct!")
else: 
    print("Incorrect.")
time.sleep(1)

#Question2
Question2 = "\nIt ___ raining."
print(Question2)
answer = question()
if answer == choices[0]:
    print("Correct!")
else:
    print("Incorrect.")
time.sleep(1)

#Question3
Question3 = "\nYou ___ short."
print(Question3)
answer = question()
if answer == choices[2]:
    print("Correct!")
else:
    print("Incorrect.")
time.sleep(1)  
    
