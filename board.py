#Import required modules and classes
import pygame
from cell import Cell

#Define board class
class Board:

    #Board constructor sets height, width, screen, difficulty, array of cells, solution board, and unfilled board
    def __init__(self, width, height, screen, difficulty, boardArray):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #Keep track of the original unfilled board
        self.boardArray = boardArray[0]
        #Keep the solution to the Sudoku
        self.original = boardArray[1]
        #Make an empty 9 by 9 cell array
        self.cellArray = [[None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9,
                      [None] * 9]

        self.surface = pygame.Surface((720, 720))
        self.surface.fill((255,255,255))
        self.selected = None

        #Fill the cell array with cells
        for i in range(9):
            for j in range(9):
                self.cellArray[i][j] = Cell(self.boardArray[i][j], i, j, self.surface)


    #Draw board by drawing each cell in the board, then draw 9 boxes with thicker borders
    def draw(self):
        for i in range(9):
            for j in range(9):
                self.cellArray[i][j].draw()
        self.screen.blit(self.surface, (140, 50))

        for a in range(3):
            for b in range(3):
                myRect = pygame.Rect((a * 240 + 140, b * 240 + 50), (240, 240))
                pygame.draw.rect(self.screen, (0,0,0), myRect, 5)


    #Select a cell
    def select(self, row, col):
        #Check that index is not negative
        if row < 0 or col < 0:
            return -1
        #Unselect all cells in the array
        for i in self.cellArray:
            for j in i:
                j.selected = False
        #Try to select cell at specified row and column
        try:
            self.cellArray[row][col].selected = True
            self.selectedPos = (row, col)
            self.selected = self.cellArray[row][col]
        except:
            pass


    #Get box coordinates of click
    def click(self, x, y):
        return (int(x//(self.width/9)), int(y//(self.height/9)))



    #Clear board by setting all cell value and sketched values to 0.
    def clear(self):
        if self.boardArray[self.selectedPos[0]][self.selectedPos[1]] == 0:
            self.selected.value = 0
            self.selected.sketched = None


    #Set a sketched value, make sure that it is in range 1 to 9
    def sketch(self, value):
        if self.boardArray[self.selectedPos[0]][self.selectedPos[1]] == 0:
            try:
                value = int(value)
                if value > 9 or value < 1:
                    raise Exception

                self.selected.sketched = value
            except:
                pass


    #Set cell value to sketched value if there is one, then set sketched value to none
    def place_number(self):
        if self.selected.sketched is not None:
            self.selected.value = self.selected.sketched
            self.selected.sketched = None



    #Turn board into original board
    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.cellArray[i][j] = Cell(self.boardArray[i][j], i, j, self.surface)



    #Check if board is full by returning False if any cell has value 0.
    def is_full(self):
        for i in self.cellArray:
            for j in i:
                if j.value == 0:
                    return False
        return True



    def update_board(self):
        pass


    #Return a tuple of a cell which has value 0.
    def find_empty(self):
        for i in self.cellArray:
            for j in i:
                if j.value == 0:
                    return (i, j)


    #Check if board is solved by comparing every cell in the current board to the solution board.
    def check_board(self):
        for i in range(len(self.cellArray)):
            for j in range(len(self.cellArray[i])):
                if self.cellArray[i][j].value != self.original[i][j]:
                    return False
        return True
