#chatbot
import random
import time
Dessert = ["Ice cream", "Cupcake","Cake","Chocolate mousse","Brownies"]
print("Welcome to chatbot")
name = input("What's your name?")
print("Hello,", name, "it's nice to meet you.")
time.sleep(2)
Fave_Dessert = input("What's your favourite dessert?")
print("That sounds delicious, my favourite is", random.choice(Dessert))
Day = input("Have you had a good day?")
if Day == "yes":
    print("Good to hear.")
else:
    print("I hope tomorrow is better")
