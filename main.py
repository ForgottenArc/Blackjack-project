

import art
import random

        #A                                J  Q    K
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

restart = False
def deal_card(cards):
    return random.choice(cards)


user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

#calculating the scores
def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

play = True



user_result = calculate_score(user_cards)
bot_result = calculate_score(computer_cards)

if bot_result == 0 :
    print("Bot win BlackJack")
    exit()

if user_result == 0:
    print("User win BlackJack")
    exit()

if user_result == 21:
    print(f"User win with the result of {user_result} and Bot has {bot_result}")
    exit()

if bot_result == 21 :
    print(f"bot win with the result of {bot_result} and User has {user_result}")
    exit()


while not restart:
    while play:

        print(f"Your current result is {user_result}")
        another_card = input("Do you want to add another card? y/n").lower()

        if another_card == "n":

            while bot_result < 17 :
                computer_cards.append(deal_card(cards))
                print("Computer is adding cards to itself")
                bot_result = calculate_score(computer_cards)



            if user_result < 21 and bot_result < 21:

                if user_result == bot_result :
                    print(f"Tied with the result of {user_result}")
                    play = False


                elif user_result > bot_result:
                    print(f"User wins with the result of : {user_result}")
                    play = False


                elif bot_result > user_result :
                    print(f"Bot win with the result of : {bot_result}")
                    play = False

            elif user_result > 21:
                print(f"User busted with the result of {user_result}")
                play = False

            else:
                print(f"Bot busted with the result of {bot_result}")
                play = False

        else:
            user_cards.append(deal_card(cards))
            user_result = calculate_score(user_cards)
            print(f"The result is {user_result}")

            if user_result >21 :
                print(f"User Busted with the result of {user_result}")
                play = False

    keep_playing = input("Do you want to play more? y/n").lower()
    if keep_playing == "y":
        user_result = 0
        bot_result = 0
        user_cards.clear()
        computer_cards.clear()

        for i in range(2):
            user_cards.append(deal_card(cards))
            computer_cards.append(deal_card(cards))

        user_result = calculate_score(user_cards)
        bot_result = calculate_score(computer_cards)
        play = True
        restart = False

    else:
        print("Thank you for playing")
        restart = True





