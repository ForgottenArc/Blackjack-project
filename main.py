
import art
import random

        #A                                J  Q    K
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


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

user_result = calculate_score(user_cards)
bot_result = calculate_score(computer_cards)

if bot_result == 0 :
    print("Bot win BlackJack")
    exit()

if user_result == 0:
    print("User win BlackJack")
    exit()

if user_result == 21:
    print(f"User win with the result of {user_result}")
    exit()

if bot_result == 21 :
    print(f"bot win with the result of {bot_result}")
    exit()

if user_result < 21 and bot_result < 21:

    if user_result == bot_result :
        print(f"Tied with the result of {user_result}")


    elif user_result > bot_result:
        print(f"User wins with the result of : {user_result} and Bot has {bot_result}")

    elif bot_result > user_result :
        print(f"Bot win with the result of : {bot_result} and User has {user_result}")

else:
    print("Busted!!!!")





