import copy

__author__ = "Nima Iji"
__email__ = "ijinima@gmail.com"


class TicTacToe:

    def __init__(self, size: int):
        self.grid_size = size
        self.data = []
        self.win_accuracy = 8
        self.max_player = 'X'
        self.min_player = 'O'
        self.empty_cell = '?'
        self.win_value = self.grid_size ** 2 + 1
        self.lose_value = -2
        self.game_over_value = -1
        self.is_inf = False
        self.is_minf = False

        for i in range(size):
            self.data.append([])
            for j in range(size):
                self.data[i].append(self.empty_cell)

    # Inserting a new cell at (i, j)
    def insert(self, i: int, j: int, data: int):
        self.data[i][j] = data

    # Inserting a new max player move at (i, j)
    def insert_x(self, i: int, j: int):
        self.data[i][j] = self.max_player

    # Update Tic-Tac-Toe data
    def insert_data(self, data: list):
        self.data = data

    # Make a Tic-Tac-Toe with positive infinity value
    def set_inf(self):
        self.is_inf = True

    # Make a Tic-Tac-Toe with negative infinity value
    def set_minf(self):
        self.is_minf = True

    """
    How is evaluation process?
    we check some parameters on all cells including:
        * horizontal cells are valid for winning Max player
        * vertical cells are valid for winning Max player
        * main diagonal is valid for winning Max player
        * anti diagonal is valid for winning Max player
        * game is over or not -> returns -1
        * Max player won or not -> returns (grid_size)^2
        * Min player won or not -> returns -2
    """

    def evaluate_position(self) -> int:

        if self.is_inf:
            return 99999999  # infinity value
        elif self.is_minf:
            return -99999999

        value = 0
        win_array = self.grid_size * [self.max_player]
        lose_array = self.grid_size * [self.min_player]
        d_tmp = []
        s_tmp = []

        is_game_over = True
        for i in range(self.grid_size):

            if self.empty_cell in self.data[i]:
                is_game_over = False

            if self.data[i] == lose_array:
                return self.lose_value
            elif self.data[i] == win_array:
                return self.win_value

            # horizontal evaluation
            if self.min_player not in self.data[i]:
                value += 1

            v_tmp = []

            for j in range(self.grid_size):
                v_tmp.append(self.data[j][i])

            # vertical evaluation
            if self.min_player not in v_tmp:
                value += 1

            d_tmp.append(self.data[i][i])
            s_tmp.append(self.data[i][self.grid_size - (i + 1)])

        if is_game_over:
            return self.game_over_value

        if lose_array in (v_tmp, d_tmp, s_tmp):
            return self.lose_value
        elif win_array in (v_tmp, d_tmp, s_tmp):
            return self.win_value

        # main diagonal evaluation
        if self.min_player not in d_tmp:
            value += 1

        # anti diagonal evaluation
        if self.min_player not in s_tmp:
            value += 1

        return value

    """
    This method has several usages in the Min-Max algorithm, including:
        * for playing with computer
        * finding chosen leaf
        * finding path to a leaf
    """

    def get_possible_tics(self, player: str) -> list:
        arr = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.data[i][j] == self.empty_cell:
                    tic = TicTacToe(self.grid_size)
                    tic.insert_data(copy.deepcopy(self.data))
                    tic.insert(i, j, player)
                    arr.append(tic)
        return arr

    def get_possible_moves(self) -> list:
        moves = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.data[i][j] == self.empty_cell:
                    moves.append((i, j))
        return moves

    def __str__(self):
        string = 'i/j'
        for i in range(self.grid_size):
            string += '  ' + str(i) + '  '
        string += '\n'
        for i in range(self.grid_size):
            string += '   '
            string += self.grid_size * ' --- '
            string += '\n'
            for j in range(self.grid_size):
                if j == 0:
                    string += str(i) + '  '
                string += '| ' + self.data[i][j] + ' |'
                if (j + 1) % self.grid_size == 0:
                    string += '\n'
        string += '   '
        string += self.grid_size * ' --- '
        return string


def min_max(state: TicTacToe, move: tuple, human_turn: bool, alpha: TicTacToe, beta: TicTacToe) -> (TicTacToe, tuple):
    state_value = state.evaluate_position()
    if state_value in (state.game_over_value, state.win_value, state.lose_value):
        return state, move

    turn = human_turn
    if not turn:
        min = None
        possible_tics = state.get_possible_tics(state.min_player)
        for index, m in enumerate(state.get_possible_moves()):
            val = min_max(possible_tics[index], m, not turn, alpha, beta)
            min = val if min is None or val[0].evaluate_position() < min[0].evaluate_position() else min
            beta = val[0] if val[0].evaluate_position() < beta.evaluate_position() else beta
            if beta.evaluate_position() <= alpha.evaluate_position():
                break
        return min
    else:
        max = None
        possible_tics = state.get_possible_tics(state.max_player)
        for index, m in enumerate(state.get_possible_moves()):
            val = min_max(possible_tics[index], m, not turn, alpha, beta)
            max = val if max is None or val[0].evaluate_position() > max[0].evaluate_position() else max
            alpha = val[0] if val[0].evaluate_position() > alpha.evaluate_position() else alpha
            if beta.evaluate_position() <= alpha.evaluate_position():
                break
        return max


# Sample: playing with computer
tic = TicTacToe(3)

# creating positive infinite and negative infinite TicTacToes
infinite_tic = TicTacToe(tic.grid_size)
infinite_tic.set_inf()
neg_infinite_tic = TicTacToe(tic.grid_size)
neg_infinite_tic.set_minf()


# printing horizontal lines
def hline():
    str = 30 * '-'
    print(str)


print(
    'Lets play a 3x3 Tic-Tac-Toe:\nYour player is "{}"\nComputer player is "{}"'.format(tic.max_player, tic.min_player))
hline()

human_turn = True
print(tic)
while tic.evaluate_position() not in (tic.game_over_value, tic.win_value, tic.lose_value):
    if human_turn:
        print('Yours turn')
        print('Insert "i" and "j" of a cell:')
        print('i:')
        i = int(input())
        print('j:')
        j = int(input())
        tic.insert_x(i, j)
        print(tic)
        human_turn = not human_turn
    else:
        print('Computer \'s turn:')
        res = min_max(tic, None, human_turn, infinite_tic, neg_infinite_tic)
        tic.insert(res[1][0], res[1][1], tic.min_player)
        print(tic)
        human_turn = not human_turn

if tic.evaluate_position() == tic.win_value:
    print('You won!')
elif tic.evaluate_position() == tic.lose_value:
    print('Computers won!')
else:
    print('No one won and game is over!')
