
import art
import random
         #A                       #J,Q,K
cards = {
        "A":11,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "J":10,
        "Q":10,
        "K":10
}

def random_input(cards):
    input_storing=[]
    for keys in cards:
       input_storing.append(keys)

    return random.choice(input_storing)
          
user_card= []

bot_card = []

get_first = str(random_input(cards))
get_second = str(random_input(cards))
get_third = str(random_input(cards))
get_forth = str(random_input(cards))

#The user and computer should
#each get 2 random cards




user_card1 = cards[get_first]
user_card.append(user_card1)
user_card2 =cards[get_second]
user_card.append(user_card2)

bot_card1 = cards[get_third]
bot_card.append(bot_card1)
bot_cards2 = cards[get_forth]
bot_card.append(bot_cards2)


user_total = user_card[0] + user_card[1]
bot_total = bot_card[0] + bot_card[1]


def battle():



    if user_total >=21:
        print("You lose BUSTED")
        return
    
    if bot_total >=21:
        print("Bot lose BUSTED")
        return

    if user_total > bot_total :
        print(f"User wins the total is {user_total}, and the bot is {bot_total}")
    elif user_total == bot_total:
        print(f"tie the value is {user_total}, bot value is {bot_total}")
    else:
        print(f"The bot wins the total is {bot_total} and User is {user_total}")

battle()



