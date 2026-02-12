print("Chinese New Year is near!")
print("Let me guess your Chinese zodiac sign")

import random
import time

zodiac = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
print("I think your sign is:")
time.sleep(2)
print(random.choice(zodiac))
