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

count = 1
for player in players:
    print("Player {}: {}".format(count, player))
    count =+ 1

# TODO print the number of players on the team


# TODO Print the player number and the player name
# The player number should start at the number one


# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index
