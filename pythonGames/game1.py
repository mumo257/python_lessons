# Simple chartbot
# functions
# loops
# conditional satements

def chatBot ():
    print("Hello! Am a chatbot, Ask me anything")

    while True:
        user_input = input("How can I help you: ")

        if user_input.lower() == "what is your name":
            print("My name is a simple chat bot")
            break
        elif "how are you" in user_input.lower():
            print("Am fine, how can i help you?")
        else:
            print("I'm not sure how to respond to that")   


chatBot()