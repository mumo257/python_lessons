# Create an empty list of lovers
lovers = []

# Create a lover
def new_lovers(Lover):

    # add lover to lovers list
    lovers.append(lover)

    # successfull save
    print("lover {} has being added succesfully".format(Lover))

# list lovers
def list_lovers():

    #check whether there are any lovers
    if lovers:

        # print them
        print("Your lovers are: ")

        #print lover in order
        for index, lover in enumerate(lovers):
            print("{} - {}".format((index + 1), lover))
    else:
        print("No lovers... please find love soon!!!")

# remove/delete lovers
def remove_lover(lover):

    # check if lover exists
    if lover in lovers:

        # remove that particular lover
        lovers.remove(lover)

        # success removal
        print("lover {} has being removed from your life".format(lover))
    else:
        print("lover not found")


while True:
    print("Enter 'add' to add a lover")
    print("Enter 'remove' to remove a lover")
    print("Enter 'list' to list all lovers")
    print("Enter 'quit' to quit the program")
    print(" ")

    # prompt user to input their choice
    user_input = input("What do you want to do with your lovers?: ")

    # conditions
    if user_input == "quit":
        break

    elif user_input == "add":
        # ask user to enter lovers name
        lover = input("What is your lovers name?: ")
        new_lovers(lovers)

    elif user_input == "list":
        # list all lovers
        list_lovers()

    elif user_input == "remove":
        lover = input("Enter lovers name: ")

        # call the remove function
        remove_lover(lover)
    else:
        print("Invalid input")
        