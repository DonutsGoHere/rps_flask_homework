from models.player import Player

player_1 = Player("Calum", "rock")
player_2 = Player("Lisa", "paper")

players = [player_1, player_2]

def winning_player(player_1_choice, player_2_choice):
  winner = "player_2"

  if player_1_choice  ==  player_2_choice:
    winner = "draw"
  if player_1_choice == "rock" and player_2_choice == "scissors":
    winner = "player_1"
  if player_1_choice == "paper" and player_2_choice == "rock":
    winner = "player_1"
  if player_1_choice == "scissors" and player_2_choice == "rock":
    winner = "player_1"

  return winner
