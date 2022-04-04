player = int(input("Enter player count taken: "))
team = int(input("Enter team size: "))

leftover = player%team

print("Leftover players: " + str(leftover))