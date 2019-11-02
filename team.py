# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
answer = input("Would you like to add players to the list? (Yes/No) ").lower()
while answer == 'yes':
    player = input("\nEnter the name of the player to add to the team: ")
    players.append(player)
    answer = input("Would you like to add another player? (Yes/No) ").lower()

count = len(players)
print("\nThere are {} players on the team.".format(count))
for player in range(count):
    print("Player {}: {}".format(player+1, players[player]))

# TODO print the number of players on the team


# TODO Print the player number and the player name
# The player number should start at the number one


# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index
