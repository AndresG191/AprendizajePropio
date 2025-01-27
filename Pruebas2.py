# Comandos
# while True:
#     command = input("Enter command:")
#     if command == "exit":
#         break
#     elif command == "sing":
#          print("La la LAAA")
#          continue
#
#     print("Command unknown")
from tokenize import cookie_re

spam = 123456789
maps = spam
eggs = 123456789

print(spam is maps) #prints True
print(spam is eggs) #prints False (Probabaly)

high_score = 10
def score():
    global high_score
    new_score = 465
    if new_score > high_score:
        print("New high score")
        high_score = new_score

score()
print(high_score)

spam = True
def order():
    eggs = 12

    def cook():

        if spam:
         print("Spam!")

    if eggs:
        eggs -= 1
        print("... and eggs")

    cook()
order()

