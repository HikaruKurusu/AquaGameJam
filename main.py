import pygame
import sys
from button import Button
#adding random for random question selection
import random
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
#list of questions
questions = ("Which of the following best describes an aquifer?",
             "What is the primary source of water for aquifers?",
             "What is the term for the level below which the ground is saturated with water in an aquifer?")
#list of options
answers = (("a) A layer of impermeable rock","b) A layer of permeable rock that contains and transmits groundwater","c: A layer of sedimentary rock formed by volcanic activity"),
           ("a) Rainfall and surface water", "b) Glacier meltwater", "c) Underground rivers"),
           ("a) Aquitard", "b) Water table", "c) Perched water table")
           )
#list of recorded correct answers
correct_answers = (1,1,2)


def get_font(size):
    return pygame.font.Font(font_path, size)

#returns a string of characters that don't exceed the width
def render_text(text, width,font):
    #splits the words in the string and put them in a list called words
    words = text.split()
    #makes and empty array
    lines = []
    #empty string
    line = ""

    for word in words:
        #for each word in the sentence, if the size + the line is less than the width, add the next word
        if font.size(line + word)[0] <= width:
            line += word + " "
        else:
        #if the line is too big, append the line to lines and start the next line
            lines.append(line)
            line = word + " "
    #this just adds the last line
    lines.append(line)
    return lines


def display_question(question_index,font_size,x):
    #max width for question
    max_question_width = 260
    max_option_width = 260
    #displays question text
    y = 10
    question_lines = render_text(questions[question_index], max_question_width, get_font(font_size))
    #questions
    for line in question_lines:
        #get list of strings of each line
        question_text = get_font(font_size).render(line, True, BLACK)
        #display the list of strings for each line
        screen.blit(question_text, (x, y))
        #add spacing between each line
        y += question_text.get_height() + 5
    #pick the options that correlate to the question
    options = answers[question_index]
    y += 25
    #options
    for option in options:
        option_lines = render_text(option, max_option_width, get_font(font_size-2))
        for option_line in option_lines:
            option_text = get_font(font_size-2).render(option_line, True, BLACK)
            screen.blit(option_text, (x, y))
            y += option_text.get_height() 
        y += 15
        
#function to play music
def play_music():
    pygame.mixer.music.load(bgMusic)
    #since its set to -1 it will play indefinetly
    pygame.mixer.music.play(-1)

def play():
    
    #pygame.display.set_caption("Play")
    bg = pygame.image.load("Background.png")
    bg = pygame.transform.scale(bg,(720, 720))
    #display_question(2)
    #display question for player 1
    a = random.randint(0,2)
    display_question(a,20,10)
    #display question for player 2
    b = random.randint(0,2)
    display_question(b,20,1010)

    #this is like fixed update
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
        #display back
        PLAY_BACK.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenu()
            #if u press 1 2 or 3,
            # if event.type == pygame.KEYDOWN:
            #     if event.type == pygame.K_1:
            #         if correct_answers[a] == 1:
            #             a = random.randint(0,2)
            #             display_question(a,20,10)
            #     if event.type == pygame.K_2:
            #         if correct_answers[a] == 2:
            #             a = random.randint(0,2)
            #             display_question(a,20,10)
            #     if event.type == pygame.K_3:
            #         if correct_answers[a] == 3:
            #             a = random.randint(0,2)
            #             display_question(a,20,10)


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
