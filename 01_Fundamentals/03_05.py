print("Hi\n")
name = input("What's your name? ")

print(f"It is nice to meet you {name}.")
answer = str(input(f"Are you enjoying course so far,{name}? ")).lower()

if(answer == "yes"):
    print("That's good to hear!")
else:
    print("Oh no! That's bad! Please contact the course staff!")
