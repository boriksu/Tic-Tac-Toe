def make_matrix():
    matrix = []

    i = 0
    while i < 9:
        matrix.append([])
        j = 0
        while j < 3:
            matrix[i // 3].append(input_str[i + j])
            j += 1
        i += 3
    return matrix

def print_matrix():
    print("---------")

    i = 0
    while i < 3:
        print("|", end='')
        j = 0
        while j < 3:
            print(' ' + matrix[i][j], end='')
            j += 1
        print(" |")
        i += 1
        
    print("---------")

def check_row(row):
    if row[0] == row[1] == row[2] != '_':
        return 1
    return 0

def check_colum(number):
    if matrix[0][number] == matrix[1][number] == matrix[2][number] != '_':
        return 1
    return 0

def check_rows():
    row_0 = check_row(matrix[0])
    row_1 = check_row(matrix[1])
    row_2 = check_row(matrix[2])
    sum_row = row_0 + row_1 + row_2
    if sum_row > 0:
        if sum_row == 2:
            print("Impossible")
        else:
            if row_0 == 1:
                print(matrix[0][0] + " wins")
            elif row_1 == 1:
                print(matrix[1][0] + " wins")
            else:
                print(matrix[2][0] + " wins")
        return 1
    return 0

def check_colums():
    colum_0 = check_colum(0)
    colum_1 = check_colum(1)
    colum_2 = check_colum(2)
    sum_colum = colum_0 + colum_1 + colum_2
    if sum_colum > 0:
        if sum_colum == 2:
            print("Impossible")
        else:
            if colum_0 == 1:
                print(matrix[0][0] + " wins")
            elif colum_1 == 1:
                print(matrix[0][1] + " wins")
            else:
                print(matrix[0][2] + " wins")
        return 1
    return 0

def check_diag():
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != '_':
        print(matrix[0][0] + " wins")
        return 1
    if matrix[2][0] == matrix[1][1] == matrix[0][2] != '_':
        print(matrix[2][0] + " wins")
        return 1
    return 0

def count_symbol():
    num_x = input_str.count('X')
    num_o = input_str.count('O')
    if abs(num_o - num_x) >= 2:
        return 1
    return 0

def find_space():
    if not input_str.find('_') == -1:
        return 1
    return 0


def check_winner():
    if check_diag() == 0:
        if check_rows() == 0:
            if check_colums() == 0:
                if number_symbol != 9:
                    return (0)
                else:
                    print("Draw")
    return (1)


def check_coord(coordi):
    global matrix
    if coordi.isdigit():
        if int(coordi) > 3 or int(coordi) < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            return 1
    else:
        print("You should enter numbers!")
    return 0


def draw_symbol():
    input_coordinate = input("Enter the coordinates:")
    coordinate = input_coordinate.split()
    # print(coordinate)
    if check_coord(coordinate[0]) and check_coord(coordinate[1]):
        new_coord_x = abs(int(coordinate[1]) - 3)
        new_coord_y = int(coordinate[0]) - 1
        if matrix[new_coord_x][new_coord_y] == '_':
            matrix[new_coord_x][new_coord_y] = 'X' if number_symbol % 2 else 'O'
            return (1)
        else:
            print("This cell is occupied! Choose another one!")
    return (0)
    
    

matrix = [['_', '_', '_' ], ['_', '_', '_' ], ['_', '_', '_' ]]
print_matrix()
number_symbol = -1
while True:
    if draw_symbol():
        print_matrix()
        number_symbol += 1
    if check_winner():
        break
    