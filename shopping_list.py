# As a user I should be continuosly prompted so that I can add a grocery item
#
# As a user, I should be able to ask for HELP so that I can understand how to use the application.
#
# As a user, I should be able to add an item to the list.
#
# As a user, I should be abe to see the list at any time so that I can verify my order.
#
# As a user, I should be I should be able to state when I am DONE, so that I may print out the list in totality.
#
# As a user, upon adding an item the to a list, I should know the total length of my list, so that I don't over buy.

# Create new empty list named shopping_list
shopping_list = []

# Create a function named add_to_list that declares a parameter named item
    # Add the item to the list

def add_to_list(item):
    shopping_list.append(item)

def show_list():
    for item in shopping_list:
        print(item)

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
    """)

show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'LIST':
        print(shopping_list)
        continue

    # Call add_to_list with new_item as an argument
    add_to_list(new_item)
