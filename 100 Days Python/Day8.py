print("AFFIRMATION GENERATOR")
print("---------------------")
print()
print("Hello, welcome to your daily affirmation generator. I will ask you a few questions and then generate an affirmation for you based on your answers.")
print()
name = input("Who are you?: ")
print()
if name == name:
   DOW = input("What is the day of the week? ")
   if DOW == "monday" or DOW == "Monday":
     print("It is going to be a great Monday", name)
   if DOW == "tuesday" or DOW == "Tuesday":
     print("What a wonderful Tuesday it is", name)
   if DOW == "wednesday" or DOW == "Wednesday":
     print("Happy Hump Day", name)
   if DOW == "thursday" or DOW == "Thursday":
     print(name,"your week is almost over!")
   if DOW == "friday" or DOW == "Friday":
     print(name, "It's FRIDAY!")
   else:
     print("I do not know your name, but I hope you are having a great day!")

print()
achieve = input("What do you want to achieve?: ")
print()
feel = input("On a scale of 1 - 10 how do you feel today? (1 - 😔, 10 - 😁👌): ")
print()

print("Hey!",name, "keep your chin up! So Its", DOW ,"you're going to", achieve,"!","in the most amazing way, simply by being you - YOU ROCK!" )
