fortunes = [
    "Yes", "No", "It is certain", "It is decidedly so", "Without a doubt", 
    "Outlook not so good", "Cannot predict now", "Ask again later", 
    "Reply hazy, try again", "Signs point to yes", "Don't count on it", "Very doubtful"
]
print("""
  ___    ____        _ _ _ 
 ( _ )  | __ )  __ _| | | |
 / _ \  |  _ \ / _` | | | |
| (_) | | |_) | (_| | | | |
 \___/  |____/ \__,_|_|_|_|
""")
import random
def ask_for():
    response = input("Would you like your fortune? (yes/no)): ").lower()
    return response == "yes" or response == "y"
while True:
 read_fortune = random.choice(fortunes)
 print(read_fortune)
 if not ask_for():
    print("Fortune be with you!")
    break