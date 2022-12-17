def main():
    print("Quays Game")
    user_name = input("Hi, whats your name? ")

    print("Hey, " + user_name)

    play_answers = ["yes", "YES", "Yes", "y", "Y", "ok", "OK", "Ok", "YEs", "yeS", "yea", "Yea", "sure", "Sure"]

    user_decision = input("Wanna play? ")

    # print(play_answers[ask_to_play])


    if user_decision in str(play_answers):
        print("Lets Go!")
    else:
        print("Aw you suck")
        main()

    birth_year = input("What year were you born? ")
    age = 2022 - int(birth_year)
    print("wow," + user_name + " you're only " + str(age) + "!!")
    if age > 20:
        print("Since you're older than 21, lets toast!")
    else:
        print("You're under 21 or i'd propose a toast!")
    user_career = input("what is your profession? ")
    print("A " + str(age) + "yr old " + user_career + ". " + "You're really killing it " + user_name)
    user_num1 = input("Pick a number: ")
    user_num2 = input("Nice! and one more: ")
    user_num_sum = float(user_num1) + float(user_num2)
    print("Ok, " + user_name + " i just added those numbers for no reason and got " + str(user_num_sum))
    print("Hmmm, let me think...")
    print("Lets take a trip!")
    passengers = int(input("How many people do you want to come " + user_name + "? Tickets are 100 each. "))
    childTicket = int(input("If any kids, how many will there be? By the way, kids under 12 are free 99! "))
    print("Ok, lets see...")

    total = 0

    if passengers > 0:
        total += (100 * passengers) - (childTicket * 100)

    print("That will be $" + str(total) + " in total")


main()