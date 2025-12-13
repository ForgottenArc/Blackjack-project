
import art
import random
         #A                       #J,Q,K
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#The user and computer should
#each get 2 random cards

user_card1 = random.choice(cards)
user_card2 = random.choice(cards)

bot_card1 = random.choice(cards)
bot_cards2 = random.choice(cards)



def battle(card1,card2):
    
    

    if card1 > card2 :
        print( "user wins")
    else:
        print( "bot wins" )


battle(user_card1,bot_card1)

print(user_card1)