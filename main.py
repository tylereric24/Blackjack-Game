import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_blackjack = True
print(logo)
while play_blackjack == True:
  dealer_hand = []
  player_hand = []
  start_game = input("Would you like to play a game of Blackjack? 'y' or 'n' ")
  if start_game == 'y':
    os.system('clear')
  else:
    play_blackjack = False
  

  def score_game():
    dealer_score = sum(dealer_hand)
    player_score = sum(player_hand)
    if player_score > 21 and dealer_score < 21:
      print(f"Your Score: {player_score} You Bust \n Dealer Score: {dealer_score} you lose")
    elif player_score > 21 and dealer_score > 21:
      print(f"Your Score: {player_score} \n Dealer Score: {dealer_score} DRAW!")
    elif player_score < 21 and dealer_score > 21:
      print(f"Your Score: {player_score} \n Dealer Score: {dealer_score} Dealer busts YOU WIN!!")
    elif player_score <= 21 and dealer_score <= 21:
      if player_score > dealer_score:
        print(f"Your Score: {player_score} \n Dealer Score: {dealer_score} YOU WIN!!!")
      elif dealer_score > player_score:
        print(f"Your Score: {player_score} \n Dealer Score: {dealer_score} YOU LOSE!!!")
      elif dealer_score == player_score:
        print(f"Your Score: {player_score} \n Dealer Score: {dealer_score} DRAW!!")
    
  

  def deal_cards():
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    

  def dealer_card():
    dealer_hand.append(random.choice(cards))

  def player_card():
    player_hand.append(random.choice(cards))

  if start_game == 'y':
    deal_cards()
    play_blackjack = True
    game_running = True
  else:
    play_blackjack = False
    game_running = False
    print("Goodbye")


  while game_running == True:
    current_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    print(f"Your Cards {player_hand} Current Score: {current_score}")
    print(f"Dealer First Card: {dealer_hand[0]}")
    if current_score <= 21:
      get_card = input("To get another card type 'y' type 'n' to pass ").lower()
    else:
      score_game()
      break
    
      
      
    if get_card == 'y':
      player_card()
    elif dealer_score <= 16:
      print("Dealer Takes Card")
      dealer_card()
    else:
      game_running = False
      score_game()
