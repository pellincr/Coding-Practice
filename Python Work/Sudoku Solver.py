puzzle = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]

#print_grid: 2dmatrix -> void
#purpose: to print the given matrix to the console in a readable format
def print_grid(grid):
    for row in grid:
         print(row)


#is_possible: int int int
#purpose: to determine if the given number is a possible option for a given spot in the given grid
def is_possible(x,y,num):
    #checks to see if the number is found in the same column
    for i in range(0,9):
        if puzzle[y][i] == num:
            return False
    #checks to see if the number is found in the same row
    for i in range (0,9):
        if puzzle[i][x] == num:
            return False
    #checks to see if the number exists in the same box
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[y0+i][x0+j] == num:
                return False
    return True

#solve: ->
#purpose: to fill in the correct numbers in the given sudoku grid
def solve():
    for y in range (9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for num in range(1,10):
                    if is_possible(x,y,num):
                        puzzle[y][x] = num
                        solve()
                        puzzle[y][x] = 0
                return
    print_grid(puzzle)
    #when enter is pressed, either terminates or displays another solution to the given puzzle
    #(finds the first solution possible then would go on to find further solutions when enter is pressed)
    input("More?")


if __name__ == "__main__":
    solve()