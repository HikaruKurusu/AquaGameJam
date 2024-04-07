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
#BROWN = (68, 45, 10)
#this code below is forimporting music
bgMusic = "backgroundMusic.mp3"
pygame.mixer.init()
cheering_sound = pygame.mixer.Sound('cheering.mp3')
victory_sound = pygame.mixer.Sound('victory.mp3')
#list of questions
questions = ("Which of the following best describes an aquifer?",
             "What is the primary source of water for aquifers?",
             "What is the term for the level below which the ground is saturated with water in an aquifer?",
             "Which of the following pollutants is commonly associated with aquifer contamination?",
             "What is a common method used for decontaminating aquifers polluted with organic contaminants?",
             "Which of the following describes the process of bioremediation in aquifer decontamination?",
             "What role does phytoremediation play in decontaminating aquifers?",
             "What is the primary purpose of chemical oxidation in aquifer decontamination?",
             "Which technique involves the use of electrical currents to remove contaminants from aquifers?",
             "How does physical filtration contribute to aquifer decontamination?",
             "What is one advantage of using bioremediation for aquifer decontamination?",
             "Which method involves the use of activated carbon to adsorb contaminants from aquifers?",
             "What is a potential challenge of using electrochemical treatment for aquifer decontamination?",
             "Which method relies on the principle of osmosis to remove contaminants from aquifers?"
            )
#list of options
answers = (("a) A layer of impermeable rock","b) A layer of permeable rock that contains and transmits groundwater","c) A layer of sedimentary rock formed by volcanic activity"),
           ("a) Rainfall and surface water", "b) Glacier meltwater", "c) Underground rivers"),
           ("a) Aquitard", "b) Water table", "c) Perched water table"),
           ("a) Bioremediation", "b) Chemical oxidation", "c) Physical filtration)"),
           ("a) Using chemicals to neutralize contaminants", "b) Injecting microorganisms to break down contaminants", "c) Filtering contaminants through activated carbon"),
           ("a) Introducing aquatic plants to absorb contaminants", "b) Applying heat to vaporize contaminants", "c) Using ultrasound waves to break down contaminants"),
           ("a) Removing dissolved contaminants", "b) Stimulating microbial growth", "c) Breaking down contaminants into harmless byproducts"),
           ("a) Electrochemical treatment", "b) Reverse osmosis", "c) Ion exchange"),
           ("a) By using membranes to separate contaminants", "b) By injecting chemicals to neutralize contaminants", "c) By promoting the growth of specific microorganisms"),
           ("a) Rapid treatment process", "b) Minimal environmental impact", "c) Low cost of implementation"),
           ("a) Adsorption", "b) Bioremediation", "c) Chemical oxidation"),
           ("a) High cost", "b) Limited effectiveness", "c) Risk of secondary pollution"),
           ("a) Reverse osmosis", "b) Ion exchange", "c) Electrochemical treatment"))
#list of recorded correct answers
correct_answers = (1,0,1,0, 1, 0, 2, 0, 0, 1, 0, 2, 0)
def winner1():
    winner1 = get_font(100).render("Player1 Wins", True, WHITE)
    winner1_RECT = winner1.get_rect(center=(640, 300))
    screen.blit(winner1, winner1_RECT)
def winner2():
    winner2 = get_font(100).render("Player2 Wins", True, WHITE)
    winner2_RECT = winner2.get_rect(center=(640, 300))
    screen.blit(winner2, winner2_RECT)
    
def Instructions():
    global running  # Declare 'running' as a global variable
    
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    running = True  # Initialize 'running' as True within the function scope
    bg = pygame.image.load("mainmenu_background.png")
    bg = pygame.transform.scale(bg,(1280, 720))
    while running:
        screen.blit(bg, (0, 0))
        BACK_MOUSE_POS = pygame.mouse.get_pos()
        BACK_TEXT = get_font(100).render("INSTRUCTIONS", True, (0, 0, 0))
        BACK_RECT = BACK_TEXT.get_rect(center=(640, 100))
        BACK_BUTTON = Button(pos=(640, 500), textInput="BACK", font=get_font(20), baseColor="Grey", hoveringColor="Black")
        screen.blit(BACK_TEXT, BACK_RECT)

        INSTRUCTIONS = get_font(15).render("Welcome to the high-stakes race between two rival companies in a quest to access and clean a contaminated aquifer!", True, (0, 0, 0))
        INSTRUCTIONS2 = get_font(15).render("In this thrilling competition, only one company can emerge victorious and claim the lucrative reward.", True, (0, 0, 0))
        INSTRUCTIONS3 = get_font(15).render("But here's the catch: to dig down and reach the aquifer, you must correctly answer a series of questions.", True, (0, 0, 0))
        INSTRUCTIONS4 = get_font(15).render("Player 1, you hold the keys 1, 2, and 3, while Player 2, you possess the power of 8, 9, and 0 on your keyboard to answer", True, (0, 0, 0))
        INSTRUCTIONS5 = get_font(15).render("Get ready for a battle of wits and strategy as you vie to be the first to cleanse the aquifer and secure the prize.", True, (0, 0, 0))
        INSTRUCTIONS6 = get_font(15).render("Good luck, and may the best company prevail!", True, (0, 0, 0))

        INSTRUCTIONS_RECT = BACK_TEXT.get_rect(center=(550, 300))
        INSTRUCTIONS_RECT2 = BACK_TEXT.get_rect(center=(550, 330))
        INSTRUCTIONS_RECT3 = BACK_TEXT.get_rect(center=(550, 360))
        INSTRUCTIONS_RECT4 = BACK_TEXT.get_rect(center=(550, 390))
        INSTRUCTIONS_RECT5 = BACK_TEXT.get_rect(center=(550, 420))
        INSTRUCTIONS_RECT6 = BACK_TEXT.get_rect(center=(550, 450))
        screen.blit(INSTRUCTIONS, INSTRUCTIONS_RECT)
        screen.blit(INSTRUCTIONS2, INSTRUCTIONS_RECT2)
        screen.blit(INSTRUCTIONS3, INSTRUCTIONS_RECT3)
        screen.blit(INSTRUCTIONS4, INSTRUCTIONS_RECT4)
        screen.blit(INSTRUCTIONS5, INSTRUCTIONS_RECT5)
        screen.blit(INSTRUCTIONS6, INSTRUCTIONS_RECT6)
        for button in [BACK_BUTTON]:
            button.changeColor(BACK_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False  # Update the 'running' variable to terminate the loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(BACK_MOUSE_POS):
                    mainMenu()
        pygame.display.update()
        clock.tick(60)

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

#plays victory sound 
def play_victory():
    cheering_sound.set_volume(0.15)
    victory_sound.set_volume(0.4)
    pygame.mixer.Channel(0).play(cheering_sound)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('victory.mp3'))


def display_hole(hole_width, player_depth,player_x):
    pygame.draw.rect(screen, BLACK, (player_x,180, hole_width, player_depth))



def play():
    #set player depth to 0 at start of game
    player1_depth = 0
    player2_depth = 0
    #pygame.display.set_caption("Play")
    bg = pygame.image.load("Background.png")
    bg = pygame.transform.scale(bg,(720, 720))
    #load player sprites
    p1 = pygame.image.load("Player1.png")
    p1 = pygame.transform.scale(p1,(72, 72))
    p2 = pygame.image.load("Player2.png")
    p2 = pygame.transform.scale(p2,(72, 72))
    #random question picked
    a = random.randint(0,12)
    b = random.randint(0,12)
    hole_width = 67
    player1_x = 400
    player2_x = 800

    #this updates players depth based on question and inputed answer
    def update_player_depth(question_number, player_depth,correct_answer):
        if correct_answers[question_number] == correct_answer:
            question_number = random.randint(0,12)
            player_depth += 15
        elif correct_answers[question_number] != correct_answer and player_depth > 0 and player_depth < 200:
            question_number = random.randint(0,12)
            player_depth -= 8
        elif correct_answers[question_number] != correct_answer and player_depth > 200:
            question_number = random.randint(0,12)
            player_depth -= 17
        return question_number, player_depth
        
    

    #this is like fixed update
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #background display
        screen.blit(bg, (280,0))
        #display hole
        display_hole(hole_width,player1_depth,player1_x)
        display_hole(hole_width,player2_depth,player2_x)
        #player display
        screen.blit(p1, (player1_x,player1_depth+105))
        screen.blit(p2, (player2_x,player2_depth+105))
        #background or question text
        pygame.draw.rect(screen, (255, 255, 255), (5, 5, 270, 720))
        #background or question text
        pygame.draw.rect(screen, (255, 255, 255), (1005, 5, 270, 720))
        #display question for player 1
        display_question(a,20,10)
        #display question for player 2
        display_question(b,20,1010)
        #display p1 height from aquifer
        p1depth = get_font(50).render(str(player1_depth) + "ft", True, "black")
        screen.blit(p1depth,(75,600))
        #display p2 height from aquifer
        p2depth = get_font(50).render(str(player2_depth) + "ft", True, "black")
        screen.blit(p2depth,(1075,600))
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
        if player1_depth > 345:
            winner1()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        mainMenu()

        elif player2_depth > 345:
            winner2()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        mainMenu()
            
            
             
            #mainMenu()  
        if player1_depth <= 345 and player2_depth <= 345:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        mainMenu()
                #player 1 controls: 1,2,3
                #player 2 controls: 8,9,0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        a, player1_depth = update_player_depth(a, player1_depth, 0)
                    elif event.key == pygame.K_2:
                        a, player1_depth = update_player_depth(a, player1_depth, 1)
                    elif event.key == pygame.K_3:
                        a, player1_depth = update_player_depth(a, player1_depth, 2)
                    if event.key == pygame.K_8:
                        b, player2_depth = update_player_depth(b, player2_depth, 0)
                    elif event.key == pygame.K_9:
                        b, player2_depth = update_player_depth(b, player2_depth, 1)
                    elif event.key == pygame.K_0:
                        b, player2_depth = update_player_depth(b, player2_depth, 2)
        

     

        pygame.display.update()
        clock.tick(60)

def mainMenu():
    global running  # Declare 'running' as a global variable
    
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    running = True  # Initialize 'running' as True within the function scope
    
    bg = pygame.image.load("mainmenu_background.png")
    bg = pygame.transform.scale(bg,(1280, 720))
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
                    Instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(60)

#music will play and loop until window is closed
play_music()
mainMenu()
