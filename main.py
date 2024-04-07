import pygame
import sys
from button import Button
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
running = True

def get_font(size):
    return pygame.font.SysFont("Times", size)

def play():
    pygame.display.set_caption("Play")
    bg = pygame.image.load("bg.jpg")
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(bg, (0, 0))
        PLAY_TEXT = get_font(100).render("PLAY", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = Button(pos=(640, 250), textInput="BACK", font=get_font(75), baseColor="White", hoveringColor="Black")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenu()
        pygame.display.update()
        clock.tick(60)

def mainMenu():
    global running  # Declare 'running' as a global variable

    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    running = True  # Initialize 'running' as True within the function scope
    bg = pygame.image.load("bg.jpg")
    while running:
        screen.blit(bg, (0, 0))
        # screen.fill(bg)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, (0, 0, 0))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(pos=(640, 250), textInput="PLAY", font=get_font(75), baseColor="Grey", hoveringColor="Black")
        INSTRUCTIONS_BUTTON = Button(pos=(640, 350), textInput="INSTRUCTIONS", font=get_font(75), baseColor="Grey", hoveringColor="Black")
        QUIT_BUTTON = Button(pos=(640, 450), textInput="QUIT", font=get_font(75), baseColor="Grey", hoveringColor="Black")
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False  # Update the 'running' variable to terminate the loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mainMenu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(60)

mainMenu()
