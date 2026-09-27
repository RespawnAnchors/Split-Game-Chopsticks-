class Player:

    def __init__(self):
        self.left = self.right = 1
        self.name = None

    def make_move(self, send_hand, receive_hand, opponent):
        if receive_hand == 'R':
            opponent.right = (opponent.right + send_hand) % 5
        elif receive_hand == 'L':
            opponent.left = (opponent.left + send_hand) % 5

class Game:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player = self.player1
        self.opponent = self.player2
        self.is_game_over = False

    def display(self):
        print()
        print(f"{self.player1.name}\nLeft Hand: {self.player1.left}     Right Hand: {self.player1.right}")
        print(f"{self.player2.name}\nLeft Hand: {self.player2.left}     Right Hand: {self.player2.right}")
        print()
    
    def switch_turn(self):
        self.player, self.opponent = self.opponent, self.player

    def can_split(self):
        if self.player.left in (4,2) and self.player.right == 0:
            return True
        elif self.player.right in (4,2) and self.player.left == 0:
            return True
        return False

    def can_use_hand(self, send_hand):
        if send_hand == 'L' and self.player.left == 0:
            return False
        if send_hand == 'R' and self.player.right == 0:
            return False
        return True

    def can_hit_hand(self, receive_hand):
        if receive_hand == 'L' and self.opponent.left == 0:
            return False
        if receive_hand == 'R' and self.opponent.right == 0:
            return False
        return True

    def play_turn(self):
        print(f"{self.player.name}'s turn to PLAY!")
        while True:
            send_hand = input("Which hand to use(L/R)? OR SPLIT: ")
            if send_hand not in ('L','R','SPLIT'):
                print("INVALID CHOICE!!!")
                continue

            if send_hand == 'SPLIT':
                if self.can_split():
                    if self.player.left == 4 or self.player.left == 2:
                        self.player.left = self.player.right = self.player.left//2
                    elif self.player.right == 4 or self.player.right == 2:
                        self.player.left = self.player.right = self.player.right//2
                    self.display()
                    return self.play_turn()
                else:
                    print("YOU CANNOT SPLIT!!!")
                    continue

            if self.can_use_hand(send_hand):
                while True:
                    receive_hand = input("Which hand to hit(L/R)?: ")
                    if receive_hand not in ('L','R'):
                        print("Invalid Choice!!!")
                        continue
                    if self.can_hit_hand(receive_hand):
                        if send_hand == 'L':
                            send_hand = self.player.left
                            self.player.make_move(send_hand,receive_hand,self.opponent)
                        elif send_hand == 'R':
                            send_hand = self.player.right
                            self.player.make_move(send_hand,receive_hand,self.opponent)
                        return
                    else:
                        print("YOU CANNOT HIT THAT HAND!!!")
                        continue
            else:
                print("YOU CANNOT USE THAT HAND!!!")
                continue
            
#MAIN

game=Game()

game.player1.name = input("Enter Name of Player 1: ")
game.player2.name = input("Enter Name of Player 2: ")

print("\nGAME START\n")

while True:
    game.display()
    game.play_turn()

    if game.opponent.right == 0 and game.opponent.left == 0:
        print()
        print("GAME OVER")
        print(f"{game.player.name} has WON!!!")
        break

    game.switch_turn()
