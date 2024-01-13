import pygame, sys
from board import Board
import sudoku_generator

HEIGHT = 1000
WIDTH = 1000



#Win Game Function
def won_game(screen):
    win_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    win_surface = win_font.render("Game Won!", 0, (0, 0, 0))
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(win_surface, win_rectangle)

    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((255, 0, 255))
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()


        pygame.display.update()




#Lose Game Function
def lost_game(screen):

    lose_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    lose_surface = lose_font.render("Game Over :(", 0, (0, 0, 0))
    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(lose_surface, lose_rectangle)

    restart_text = button_font.render("Restart", 0, (255, 255, 255))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((255, 0, 255))
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return True

        pygame.display.update()



#Start Screen
def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)


    screen.fill((255,255,255))


    title_surface = start_title_font.render("Sudoku", 0, (0,0,0))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)


    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255,255,255))


    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill((255,0,255))
    easy_surface.blit(easy_text, (10,10))


    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill((255,0,255))
    medium_surface.blit(medium_text, (10,10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill((255,0,255))
    hard_surface.blit(hard_text, (10,10))

    easy_rectangle = easy_surface.get_rect(center = (WIDTH//2, HEIGHT//2))
    medium_rectangle = medium_surface.get_rect(center = (WIDTH//2, HEIGHT//2 + 100))
    hard_rectangle = hard_surface.get_rect(center = (WIDTH//2, HEIGHT//2 + 200))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    difficulty = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    return difficulty
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    return difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    return difficulty

        pygame.display.update()


#Buttons for Game
def draw_buttons(buttonList):
    button_font = pygame.font.Font(None, 70)

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((255, 0, 255))
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((255, 0, 255))
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((255, 0, 255))
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 10 * 9))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 10 * 9))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 10 * 9))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    buttonList.append(reset_rectangle)
    buttonList.append(restart_rectangle)
    buttonList.append(exit_rectangle)

    return




if __name__ == "__main__":
    game_over = False
    restart = True
    buttons = []
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")


    while restart == True:
        restart = False
        difficulty = draw_game_start(screen)

        myBoard = Board(720, 720, screen, difficulty, sudoku_generator.generate_sudoku(9, difficulty))
        draw_buttons(buttons)
        myBoard.draw()





        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    myBoard.select(myBoard.click(event.pos[0] - 140, event.pos[1] - 50)[0], myBoard.click(event.pos[0] - 140, event.pos[1] - 50)[1])

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[2].collidepoint(event.pos):
                        pygame.quit()
                    elif buttons[1].collidepoint(event.pos):
                        restart = True
                        break
                    elif buttons[0].collidepoint(event.pos):
                        for i in range(len(myBoard.cellArray)):
                            for j in range(len(myBoard.cellArray)):
                                myBoard.cellArray[i][j].sketched = None
                                myBoard.cellArray[i][j].value = myBoard.boardArray[i][j]



                if event.type == pygame.KEYDOWN:
                    myBoard.sketch(pygame.key.name(event.key))


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        myBoard.place_number()
                    elif event.key == pygame.K_0:
                        myBoard.clear()

                    elif event.key == pygame.K_LEFT:
                        if myBoard.selectedPos[0] != 0:
                            myBoard.select(myBoard.selectedPos[0]-1, myBoard.selectedPos[1])
                    elif event.key == pygame.K_RIGHT:
                        if myBoard.selectedPos[0] != 8:
                            myBoard.select(myBoard.selectedPos[0]+1, myBoard.selectedPos[1])
                    elif event.key == pygame.K_UP:
                        if myBoard.selectedPos[1] != 0:
                            myBoard.select(myBoard.selectedPos[0], myBoard.selectedPos[1]-1)
                    elif event.key == pygame.K_DOWN:
                        if myBoard.selectedPos[1] != 8:
                            myBoard.select(myBoard.selectedPos[0], myBoard.selectedPos[1]+1)

            myBoard.draw()
            #draw_buttons()
            if myBoard.is_full():
                if myBoard.check_board():
                    restart= won_game(screen)
                else:

                    restart = lost_game(screen)
            pygame.display.update()

            if restart == True:
                break