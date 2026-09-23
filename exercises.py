class Game():
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
    }
    def __init__(self, turn = 'X', tie = False, winner = None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = Game.board

    # def play_game(self):
    #     print('welcome message!')

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if(self.tie == True):
            print('Time Game!')
        elif(self.winner != None):
            print(f'{self.winner} win the game!')
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        Game.print_board()
        Game.print_message()

    def get_move(self):
        while True:    
            move = input(f"Enter a valid move (example: A1)").lower()
            if move in self.board:
                if self.board(move) == None:
                    self.board(move) = self.turn
                    break
                else:
                    print('This spot is occupied')
            else:
                print('This spot does not exist, please enter a valid move')

    def check_winner(self):
        winning_combos=[
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
            ('a1', 'b2', 'c3'),
            ('a3', 'b2', 'c1'),
        ]
        for line in winning_combos:
            a, b, c = line
            if self.board[a] and (self.board[a] == self.board[b] == self[c]):
                self.winner = self.board[a]
                return True

    def check_tie(self):
        if all(value is not None for value in self.board.values):
            self.tie = True
            return True

    def switch_turn(self):
        if(self.turn == 'X'):
            self.turn = 'O'
            print('O turn')
        if(self.turn == 'O'):
            self.turn = 'X'
            print('X turn')

    def play_game(self):
        while True:
            self.render()
            self.get_move()
            if self.check_winner() == True:
                print(f'Congrats! {self.turn} won')
                break
            if self.check_tie() == True:
                print(f'It is a Tie')
                break
            self.switch_turn()




            



game_instance = Game()
game_instance.play_game()
# game_instance.play_game()
# game_instance.print_board()

        