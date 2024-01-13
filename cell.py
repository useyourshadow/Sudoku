#Import required classes
import pygame


#Define cell class
class Cell:

    #Cell constructor initializes a value, its position in the board, whether or not it is selected, and a temporary 'sketched' value.
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched = None


    #Draw cell function
    def draw(self):

        #Set border color to red if cell is selected; make border thicker if selected
        if self.selected:
            color = (255, 0, 0)
            width = 5
        else:
            color = (0, 0, 0)
            width = 1


        #Cover cell with white rectangle
        fillRect = pygame.Rect((self.row*80, self.col*80), (80,80))
        pygame.draw.rect(self.screen, (255,255,255), fillRect)

        #Give cell red or black border
        myRect = pygame.Rect((self.row * 80, self.col * 80), (80, 80))
        pygame.draw.rect(self.screen, color, myRect, width)



        #Render text with cell value
        number_font = pygame.font.Font(None, 70)
        title_surface = number_font.render(str(self.value), 0, (0, 0, 0))

        #Put text surface into cell
        self.screen.blit(title_surface, (myRect.centerx - 15, myRect.centery - 20))

        #Check if there is a sketched value and put it in the cell if there is.
        if self.sketched is not None:
            sketch_font = pygame.font.Font(None, 40)
            other_surface = sketch_font.render(str(self.sketched), 0, (0,0,255))
            self.screen.blit(other_surface, (myRect.left + 5, myRect.top + 5))



