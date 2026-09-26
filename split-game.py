# import random

class Player:

    def __init__(self):
        self.left = self.right = 1
        self.dead_left = False
        self.dead_right = False
        self.name = None

    def make_move(self, send_hand, receive_hand, opponent):
        if receive_hand == 'R':
            opponent.right = (opponent.right + send_hand)%5
        elif receive_hand == 'L':
            opponent.left = (opponent.left + send_hand)%5

class Game:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player = self.player1
        self.opponent = self.player2
        self.game_over = False

    def display(self):
        print()
        print(f"{self.player1.name}\nLeft Hand: {self.player1.left}     Right Hand: {self.player1.right}")
        print(f"{self.player2.name}\nLeft Hand: {self.player2.left}     Right Hand: {self.player2.right}")
        print()
    
    def switch_turn(self):
        self.player, self.opponent = self.opponent, self.player

    def play_turn(self):
        print(f"{self.player.name}'s turn to PLAY!")
        send_hand = input("Which hand to use(L/R)? OR SPLIT: ")
        if send_hand == "SPLIT":
            if self.player.left == 4 or self.player.left == 2:
                self.player.dead_right = False
                self.player.left = self.player.right = self.player.left//2
            if self.player.right == 4 or self.player.right == 2:
                self.player.left = self.player.right = self.player.right//2
                self.player.dead_left = False
            self.display()
            return self.play_turn()
        receive_hand = input("Which hand to hit(L/R)?: ")
        if send_hand == 'L':
            send_hand = self.player.left
            self.player.make_move(send_hand,receive_hand,self.opponent)
        elif send_hand == 'R':
            send_hand = self.player.right
            self.player.make_move(send_hand,receive_hand,self.opponent)
        
        

    def game_updates(self):
        if self.player.left == 0:
            self.player.dead_left = True
        if self.player.right == 0:
            self.player.dead_right = True
        if self.opponent.left == 0:
            self.opponent.dead_left = True
        if self.opponent.right == 0:
            self.opponent.dead_right = True

        if self.opponent.dead_right and self.opponent.dead_left:
            self.game_over = True
            
#MAIN

game=Game()

game.player1.name = input("Enter Name of Player 1: ")
game.player2.name = input("Enter Name of Player 2: ")

print("\nGAME START\n")

while True:
    game.display()
    game.play_turn()
    game.game_updates()
    if game.game_over:
        print()
        print("GAME OVER")
        print(f"{game.player.name} has WON!!!")
        break
    game.switch_turn()
