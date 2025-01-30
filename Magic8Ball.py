#Magic8Ball.py
#Name: Megann Wegner
#Date: 1/28/2025
#Assignment: Lab 2 - Magic 8 ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
question = input("Ask The Magic 8 Ball a question: ")
  #Answer question randomly with one of the options from your earlier list.

answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", 
            "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", 
            "My sources say no.", "Outlook not so good.", "Outlook good.",
            "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.",
            "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]

response = random.choice(answers)

print(response)
if __name__ == '__main__':
  main()
