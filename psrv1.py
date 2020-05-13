#player 1 
#player 2
print(".....paper....")
print(".....scissor....")
print(".....Rock......")

print("player 1 turn\n" * 20)

_player_1 = input("player 1 Enter your choice rock-paper-scissor ")

print("player 2 turn\n" * 20)

player2 =input("player 2 Enter your choice (rock-paper-scissor ")

if player1 == player2:
    print("its a draw")
elif player1 == "paper" and player2 == "scissor":
    print("player2 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")
elif player1 =="scissor" and player2 == "rock":
	print("player2 wins")
elif player2 == "paper" and player1 == "scissor":
    print("player1 wins")
elif player2 == "rock" and player1 == "paper":
    print("player1 wins")
elif player2 =="scissor" and player1 == "rock":
	print("player1 wins")
else:
    print("something went wrong")

