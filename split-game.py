from random import choice
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
    
    def get_legal_moves(self):
        possible_moves = [('L','L'), ('L','R'), ('R','L'), ('R','R'), ("SPLIT",None)]
        legal_moves=[]
        for i,j in possible_moves:
            if i == "SPLIT":
                if self.can_split():
                    legal_moves.append((i,j))
                continue

            if self.can_use_hand(i) and self.can_hit_hand(j):
                legal_moves.append((i,j))
        return legal_moves
        
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
                            attack_value = self.player.left
                            self.player.make_move(attack_value,receive_hand,self.opponent)
                        elif send_hand == 'R':
                            attack_value = self.player.right
                            self.player.make_move(attack_value,receive_hand,self.opponent)
                        return
                    else:
                        print("YOU CANNOT HIT THAT HAND!!!")
                        continue
            else:
                print("YOU CANNOT USE THAT HAND!!!")
                continue
            
#MAIN

game=Game()

opponent_type = input("Enter opponent type (HUMAN/AI): ")
game.player1.name = input("Enter Name of Player 1: ")
if opponent_type.upper() == "AI":  
    game.player2.name = "AI"
elif opponent_type.upper() == "HUMAN":
    game.player2.name = input("Enter Name of Player 2: ")

print("\nGAME START\n")
print(f"{game.player1.name} vs {game.player2.name}\n")
if opponent_type.upper() == "HUMAN":
    while True:
        
        game.display()
        game.play_turn()

        game.switch_turn()

        if not game.get_legal_moves():
            game.display()
            print("GAME OVER")
            print(f"{game.player.name} has WON!!!")
            break

elif opponent_type.upper() == "AI":
    while True:
        if game.player.name == "AI":
            legal_moves = game.get_legal_moves()
            if not legal_moves:
                game.display()
                print("GAME OVER")
                print(f"{game.opponent.name} has WON!!!")
                break
            send_hand, receive_hand = choice(legal_moves)
            print(f"AI chooses to use {send_hand} hand to hit {receive_hand} hand.")
            if send_hand == 'L':
                attack_value = game.player.left
                game.player.make_move(attack_value, receive_hand, game.opponent)
            elif send_hand == 'R':
                attack_value = game.player.right
                game.player.make_move(attack_value, receive_hand, game.opponent)
        elif game.player.name != "AI":
            game.display()
            game.play_turn()
        game.switch_turn()