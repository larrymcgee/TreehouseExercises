# TODO Create an empty list to maintain the player names


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'


# TODO print the number of players on the team


# TODO Print the player number and the player name
# The player number should start at the number one


# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index


players = []

answer = input("Would you like to add players to the list? (Yes/No) ").lower()
while answer == 'yes':
    player = input("\nEnter the name of the player to add to the team: ")
    players.append(player)
    answer = input("Would you like to add another player? (Yes/No) ").lower()

# First solution
# count = len(players)
# print("\nThere are {} players on the team.".format(count))
# for player in range(count):
#     print("Player {}: {}".format(player+1, players[player]))

# Cleaner solution
print("\nThere are {} players on the team.".format(len(players)))
count = 1
for player in players:
    print("Player {}: {}".format(count, player))
    count += 1

player_num = int(input("Please select the goal keeper by selecting the player number. (1-{}) ".format(len(players))))
print("Great!!! The goal keeper for the game will be {}!".format(players[player_num-1]))
