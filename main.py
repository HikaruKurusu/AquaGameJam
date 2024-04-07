import pygame
import sys
from button import Button
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
running = True
#imported pixel font
font_path = "Pixel.ttf"
#colors for background of Back button
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#this code below is forimporting music
bgMusic = "backgroundMusic.mp3"
pygame.mixer.init()


def get_font(size):
    return pygame.font.Font(font_path, size)

#function to play music
def play_music():
    pygame.mixer.music.load(bgMusic)
    #since its set to -1 it will play indefinetly
    pygame.mixer.music.play(-1)

def play():
    #pygame.display.set_caption("Play")
    bg = pygame.image.load("Background.png")
    bg = pygame.transform.scale(bg,(720, 720))
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(bg, (280,0))
        #uncomment out for play text at the top
        #PLAY_TEXT = get_font(100).render("PLAY", True, "Black")
        #PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        #screen.blit(PLAY_TEXT, PLAY_RECT)
        #back button
        PLAY_BACK = Button(pos=(640, 650), textInput="BACK", font=get_font(25), baseColor="Black", hoveringColor="red")
        #background rect of back button
        pygame.draw.rect(screen,WHITE,(PLAY_BACK.rect.x-9, PLAY_BACK.rect.y+1, PLAY_BACK.rect.width+15, PLAY_BACK.rect.height))
        pygame.draw.rect(screen,BLACK,(PLAY_BACK.rect.x-9, PLAY_BACK.rect.y+1, PLAY_BACK.rect.width+15, PLAY_BACK.rect.height),5)
        #change color after hover
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

#music will play and loop until window is closed
play_music()
mainMenu()
