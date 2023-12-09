from numpy import random
import copy

"""
According to: http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf
"""

__author__ = "Nima Iji"
__email__ = "ijinima@gmail.com"

# Sample filled Sudoku for testing algorithm
# filled = [(0, 1, 3), (0, 2, 4), (0, 3, 6), (0, 4, 7), (0, 5, 2), (0, 6, 1), (0, 7, 9), (0, 8, 8),
#           (1, 0, 6), (1, 1, 7), (1, 2, 8), (1, 3, 1), (1, 4, 9), (1, 5, 5), (1, 6, 3), (1, 7, 4), (1, 8, 2),
#           (2, 0, 9), (2, 1, 1), (2, 2, 2), (2, 3, 3), (2, 4, 4), (2, 5, 8), (2, 6, 5), (2, 7, 6), (2, 8, 7),
#           (3, 0, 8), (3, 1, 5), (3, 2, 9), (3, 3, 4), (3, 4, 2), (3, 5, 6), (3, 6, 7), (3, 7, 1), (3, 8, 3),
#           (4, 0, 7), (4, 1, 6), (4, 2, 1), (4, 3, 8), (4, 4, 5), (4, 5, 3), (4, 6, 9), (4, 7, 2), (4, 8, 4),
#           (5, 0, 4), (5, 1, 2), (5, 2, 3), (5, 3, 7), (5, 4, 9), (5, 5, 1), (5, 6, 8), (5, 7, 5), (5, 8, 6),
#           (6, 0, 9), (6, 1, 6), (6, 2, 1), (6, 3, 2), (6, 4, 8), (6, 5, 7), (6, 6, 3), (6, 8, 5),
#           (7, 0, 5), (7, 1, 3), (7, 2, 7), (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 6, 2), (7, 7, 8),
#           (8, 0, 2), (8, 1, 8), (8, 2, 4), (8, 3, 6), (8, 4, 3), (8, 5, 5), (8, 6, 1), ]

filled = [(0, 0, 5), (0, 1, 3), (0, 3, 6), (0, 7, 9), (0, 8, 8),
          (1, 1, 7), (1, 3, 1), (1, 4, 9), (1, 5, 5),
          (2, 7, 6),
          (3, 0, 8), (3, 3, 4), (3, 6, 7),
          (4, 1, 6), (4, 3, 8), (4, 5, 3), (4, 7, 2),
          (5, 2, 3), (5, 5, 1), (5, 8, 6),
          (6, 1, 6),
          (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 7, 8),
          (8, 0, 2), (8, 1, 8), (8, 5, 5), (8, 7, 7), (8, 8, 9)]

board = []


# useful function for checking unused numbers
def not_array(arr):
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in arr:
        if a in t:
            t.remove(a)
    return t


# create board
for i in range(9):
    board.append([])
    for j in range(9):
        board[i].append(0)

# fill board with filled items
for item in filled:
    board[item[0]][item[1]] = item[2]


# finding naked cells
def population(filled, brd, add2filled):
    naked_flag = 1
    while naked_flag:
        naked_flag = 0
        for i in range(9):
            for j in range(9):

                v_tmp = []
                h_tmp = []
                i_diff = i % 3
                j_diff = j % 3

                for index in [0 + i_diff, 3 + i_diff, 6 + i_diff]:
                    for jj in [0 + j_diff, 3 + j_diff, 6 + j_diff]:
                        v_tmp.append(brd[index][jj])

                for index in [0 + int(i / 3) * 3, 1 + int(i / 3) * 3, 2 + int(i / 3) * 3]:
                    for jj in [0 + int(j / 3) * 3, 1 + int(j / 3) * 3, 2 + int(j / 3) * 3]:
                        h_tmp.append(brd[index][jj])

                naked_array = not_array(v_tmp + h_tmp + brd[i])
                if len(naked_array) == 1 and brd[i][j] == 0:
                    # print(naked_array, v_tmp, h_tmp, i, j)
                    if add2filled:
                        filled += [(i, j, naked_array[0])]
                    naked_flag = 1
                    brd[i][j] = naked_array[0]


population(filled, board, True)

# create 4 parents
b1 = copy.deepcopy(board)
b2 = copy.deepcopy(board)
b3 = copy.deepcopy(board)
b4 = copy.deepcopy(board)

# create random populations
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            # Filling population with random items
            # b1[i][j] = (random.randint(1, 9))
            # b2[i][j] = (random.randint(1, 9))
            # b3[i][j] = (random.randint(1, 9))
            # b4[i][j] = (random.randint(1, 9))

            # Filling population with more smart way
            b1[i][j] = not_array(b1[i][:9])[random.randint(0, len(not_array(b1[i][:9])))] if not_array(
                b1[i][:9]) != [] else random.randint(1, 9)
            b1[i][j] = not_array(b2[i][:9])[random.randint(0, len(not_array(b2[i][:9])))] if not_array(
                b2[i][:9]) != [] else random.randint(1, 9)
            b1[i][j] = not_array(b3[i][:9])[random.randint(0, len(not_array(b3[i][:9])))] if not_array(
                b3[i][:9]) != [] else random.randint(1, 9)
            b1[i][j] = not_array(b4[i][:9])[random.randint(0, len(not_array(b4[i][:9])))] if not_array(
                b4[i][:9]) != [] else random.randint(1, 9)

            # find naked cells
            population(filled, b1, False)
            population(filled, b2, False)
            population(filled, b3, False)
            population(filled, b4, False)


# Fitness function
def fitness(brd):
    fit_rate = 0

    # check squares
    for i in range(9):
        sorted_sqr = sorted(brd[i])
        if sorted_sqr == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            fit_rate += 8
        else:
            for index in range(len(sorted_sqr) - 1):
                if sorted_sqr[index] != sorted_sqr[index + 1]:
                    fit_rate += 1

    # if squares are fit check plus relations
    if True:
        for i in range(9):
            for j in range(9):
                v_tmp = []
                h_tmp = []
                i_diff = i % 3
                j_diff = j % 3

                for index in [0 + i_diff, 3 + i_diff, 6 + i_diff]:
                    for jj in [0 + j_diff, 3 + j_diff, 6 + j_diff]:
                        v_tmp.append(brd[index][jj])

                for index in [0 + int(i / 3) * 3, 1 + int(i / 3) * 3, 2 + int(i / 3) * 3]:
                    for jj in [0 + int(j / 3) * 3, 1 + int(j / 3) * 3, 2 + int(j / 3) * 3]:
                        h_tmp.append(brd[index][jj])

                fit_rate += ((9 - len(not_array(v_tmp))) + (9 - len(not_array(h_tmp))))

    return fit_rate


def get_selection(slc):
    return sorted(slc, key=lambda x: x[0], reverse=True)


def crossover(brd1, brd2, brd3):
    rnd1 = random.randint(1, 8)
    rnd2 = random.randint(1, 8)
    rnd3 = random.randint(1, 8)
    rnd4 = random.randint(1, 8)
    tmp2 = brd2[0:rnd2] + brd1[rnd2:9] if fitness(brd2[0:rnd2] + brd1[rnd2:9]) - fitness(brd2) > random.randint(1,
                                                                                                                5) else brd2
    tmp1 = brd1[0:rnd1] + brd2[rnd1:9] if fitness(brd1[0:rnd1] + brd2[rnd1:9]) - fitness(brd1) > random.randint(1,
                                                                                                                5) else brd1
    tmp3 = brd3[0:rnd3] + brd2[rnd3:9] if fitness(brd3[0:rnd3] + brd2[rnd3:9]) - fitness(brd3) > random.randint(1,
                                                                                                                5) else brd3
    return [[fitness(tmp1), tmp1],
            [fitness(tmp2), tmp2],
            [fitness(tmp3), tmp3],
            [fitness(brd1[0:rnd4] + tmp1[rnd4:9]), brd1[0:rnd4] + tmp1[rnd4:9]]]


def mutation(brd):
    tmp = copy.deepcopy(brd)
    first_fit = fitness(tmp)
    for i in range(9):
        for j in range(9):

            # filled items
            c_flag = 0
            for item in filled:
                if item[0] == i and item[1] == j:
                    c_flag = 1
                    break
            if c_flag == 1:
                continue

            # check vertical and horizontal cells
            v = []
            h = []
            i_diff = i % 3
            j_diff = j % 3

            for index in [0 + i_diff, 3 + i_diff, 6 + i_diff]:
                for jj in [0 + j_diff, 3 + j_diff, 6 + j_diff]:
                    v.append(brd[index][jj])

            try:
                brd[i][j] = not_array(v)[random.randint(0, len(not_array(v)) - 1)] if not_array(v) != [] else brd[i][j]
            except:
                None

            for index in [0 + int(i / 3) * 3, 1 + int(i / 3) * 3, 2 + int(i / 3) * 3]:
                for jj in [0 + int(j / 3) * 3, 1 + int(j / 3) * 3, 2 + int(j / 3) * 3]:
                    h.append(brd[index][jj])

            try:
                brd[i][j] = not_array(h)[random.randint(0, len(not_array(h)) - 1)] if not_array(h) != [] else brd[i][j]
            except:
                None

            # check squares
            for t in brd[i][0:j] + brd[i][(j + 1):9]:
                if brd[i][j] == t:
                    try:
                        brd[i][j] = not_array(brd[i])[
                            random.randint(0, len(brd[i]) - 1)]
                    except:
                        None

    if first_fit > fitness(brd):
        return tmp
    return brd


# Fittest generation = best "fit rank" a Sudoku board can has
fittest_rank = 1530

# First selection
selection = get_selection([[fitness(b1), b1], [fitness(b2), b2], [fitness(b3), b3], [fitness(b4), b4]])

gen_num = 0
while gen_num < 1000:
    gen_num += 1
    if selection[0][0] >= fittest_rank:
        print(gen_num, 'is best generation: ', selection[0][1])
        break
    else:
        print('Generation number:', gen_num, 'with fitness rate:', selection[0][0])
        selection = get_selection(
            crossover(mutation(selection[1][1]),
                      mutation(selection[0][1]),
                      mutation(selection[1][1])))
