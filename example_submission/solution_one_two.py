def chat():
    print("Try talking to the machine :)")
    print("############################")
    while True:
        user_input = input()
        if "hello" in user_input.lower():
            print("hello!  How are you?")
        else:
            print("hmm, interesting")

        print("CTRL-Z to exit")

chat()
