"""
TO DO:

Create a list with all letters from the alphabet 

pop a letter from the list after it's guessed by a player or the CPU
(create a main menu)set up the game for 2 player play or player VS CPU

add a library of words for the game

"""
#TODO - import all letters as game objects 

import pygame, random, os

Screen_Width = 1600
Screen_Height = 800
Screen_Title = "Hangman Game" #Sets name on gamewindow 
White_Colour = (255,255,255) #colours set according to RGB - R 255 G 255  B 255
Black_Colour = (0,0,0)
Red_Colour = (255,0,0)
Green_Colour = (0,255,0)
Blue_Colour = (0,0,255)
Grey_Colour = (100,100,100)
LightGrey_Colour = (200,200,200)
Clock = pygame.time.Clock()
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Word_List = ["Apple", "Ball"]
GuessList = []


class GameObject: #class for defining game objects that will be drawn onto the game screen and moved arround
    def __init__(self, image_path, X_pos, Y_pos, Width, Height):
        Object_Image = pygame.image.load(image_path) #Loads image to be set
        self.Image = pygame.transform.scale(Object_Image, (Width, Height)) #Scales the image that's been loaded in 
        self.X_pos = X_pos
        self.Y_pos = Y_pos
        self.Width = Width
        self.Height = Height
    
    def Draw (self,background): #This function is used to draw the object on the game screen
        background.blit(self.Image,(self.X_pos,self.Y_pos)) #Blit funtion is used to draw imaghes to the game screen/ surface selected along with the X and Y Pos taken in the form of a tuple 


class Game:
    Tick_Rate = 60 #Change to set framerate
    
    
    def __init__ (self, title, width, height):
        self.title = title
        self.width = width
        self.height = height 
        self.Game_Screen = pygame.display.set_mode((width, height)) #Creates the window being displayed 
        self.Game_Screen.fill(LightGrey_Colour) #Sets the default colour of the displayed window 
        pygame.display.set_caption(title)

#GAME LOOP ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def run_game_loop (self):
        click = False
        Game_Over = False
        GameMenu = True
        OnePlayerGame = False #sets game into a state where you play against the CPU
        TwoPlayerGame = False #sets game into a two player state where you play against another player 
        ChooseWord = False
        RandomWord = False
        letterGuessed = ""
        turn = ""
        onScreenKeyBoard = "qwertyuiopasdfghjklzxcvbnm"

 
        title = GameObject("assets/Menu/Title.png", 350,100,896,110) 
        onePlayer = GameObject("assets/Menu/singlePlayer.png", 650,600,233,34)
        twoPlayer = GameObject("assets/Menu/2Player.png", 650,675,241,34)
        selectWord = GameObject("assets/Menu/selectWord.png", 565,600,367,36)
        randomWord = GameObject("assets/Menu/randomWord.png", 565,675,442,36)

        A = GameObject("assets/A.png", 100,100,26,21)
        B = GameObject("assets/B.png", 100,100,20,21)
        C = GameObject("assets/C.png", 100,100,22,21)
        D = GameObject("assets/D.png", 100,100,26,21)
        E = GameObject("assets/E.png", 100,100,17,21)
        F = GameObject("assets/F.png", 100,100,17,21)
        G = GameObject("assets/G.png", 100,100,24,22)
        H = GameObject("assets/H.png", 100,100,28,21)
        I = GameObject("assets/I.png", 100,100,13,21)
        J = GameObject("assets/J.png", 100,100,16,21)
        K = GameObject("assets/K.png", 100,100,25,21)
        L = GameObject("assets/L.png", 100,100,19,21)
        M = GameObject("assets/M.png", 100,100,33,21)
        N = GameObject("assets/N.png", 100,100,28,21)
        O = GameObject("assets/O.png", 100,100,25,21)
        P = GameObject("assets/P.png", 100,100,19,21)
        Q = GameObject("assets/Q.png", 100,100,27,21)
        R = GameObject("assets/R.png", 100,100,24,21)
        S = GameObject("assets/S.png", 100,100,14,21)
        T = GameObject("assets/T.png", 100,100,22,22)
        U = GameObject("assets/U.png", 100,100,25,21)
        V = GameObject("assets/V.png", 100,100,25,21)
        W = GameObject("assets/W.png", 100,100,34,21)
        X = GameObject("assets/X.png", 100,100,28,21)
        Y = GameObject("assets/Y.png", 100,100,25,21)
        Z = GameObject("assets/Z.png", 100,100,20,22)
        


        while Game_Over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_Over = True
                keys = pygame.key.get_pressed()
                mousePos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

                if keys[pygame.K_ESCAPE] == True:
                    Game_Over = True 

                if keys[pygame.K_a] == True: #Checks for A Key - to be repeated for entire keyboard
                    if "A" not in GuessList:
                        GuessList.append("A")
                        turn = "Over"
                elif keys[pygame.K_b] == True: #Checks for B Key - to be repeated for entire keyboard
                    if "B" not in GuessList:
                        GuessList.append("B")
                        turn = "Over"
                elif keys[pygame.K_c] == True: #Checks for C Key - to be repeated for entire keyboard
                    if "C" not in GuessList:
                        GuessList.append("C")
                        turn = "Over"
                elif keys[pygame.K_d] == True: #Checks for D Key - to be repeated for entire keyboard
                    if "D" not in GuessList:
                        GuessList.append("D")
                        turn = "Over"
                elif keys[pygame.K_e] == True: #Checks for E Key - to be repeated for entire keyboard
                    if "E" not in GuessList:
                        GuessList.append("E")
                        turn = "Over"
                elif keys[pygame.K_f] == True: #Checks for F Key - to be repeated for entire keyboard
                    if "F" not in GuessList:
                        GuessList.append("F")
                        turn = "Over"
                elif keys[pygame.K_g] == True: #Checks for G Key - to be repeated for entire keyboard
                    if "G" not in GuessList:
                        GuessList.append("G")
                        turn = "Over"
                elif keys[pygame.K_h] == True: #Checks for H Key - to be repeated for entire keyboard
                    if "H" not in GuessList:
                        GuessList.append("H")
                        turn = "Over"
                elif keys[pygame.K_i] == True: #Checks for I Key - to be repeated for entire keyboard
                    if "I" not in GuessList:
                        GuessList.append("I")
                        turn = "Over"
                elif keys[pygame.K_j] == True: #Checks for J Key - to be repeated for entire keyboard
                    if "J" not in GuessList:
                        GuessList.append("J")
                        turn = "Over"
                elif keys[pygame.K_k] == True: #Checks for K Key - to be repeated for entire keyboard
                    if "K" not in GuessList:
                        GuessList.append("K")
                        turn = "Over"
                elif keys[pygame.K_l] == True: #Checks for L Key - to be repeated for entire keyboard
                    if "L" not in GuessList:
                        GuessList.append("L")
                        turn = "Over"
                elif keys[pygame.K_m] == True: #Checks for M Key - to be repeated for entire keyboard
                    if "M" not in GuessList:
                        GuessList.append("M")
                        turn = "Over"
                elif keys[pygame.K_n] == True: #Checks for N Key - to be repeated for entire keyboard
                    if "N" not in GuessList:
                        GuessList.append("N")
                        turn = "Over"
                elif keys[pygame.K_o] == True: #Checks for O Key - to be repeated for entire keyboard
                    if "O" not in GuessList:
                        GuessList.append("O")
                        turn = "Over"
                elif keys[pygame.K_p] == True: #Checks for P Key - to be repeated for entire keyboard
                    if "P" not in GuessList:
                        GuessList.append("P")
                        turn = "Over"
                elif keys[pygame.K_q] == True: #Checks for Q Key - to be repeated for entire keyboard
                    if "Q" not in GuessList:
                        GuessList.append("Q")
                        turn = "Over"
                elif keys[pygame.K_r] == True: #Checks for R Key - to be repeated for entire keyboard
                    if "R" not in GuessList:
                        GuessList.append("R")
                        turn = "Over"
                elif keys[pygame.K_s] == True: #Checks for S Key - to be repeated for entire keyboard
                    if "S" not in GuessList:
                        GuessList.append("S")
                        turn = "Over"
                elif keys[pygame.K_t] == True: #Checks for T Key - to be repeated for entire keyboard
                    if "T" not in GuessList:
                        GuessList.append("T")
                        turn = "Over"
                elif keys[pygame.K_u] == True: #Checks for U Key - to be repeated for entire keyboard
                    if "U" not in GuessList:
                        GuessList.append("U")
                        turn = "Over"
                elif keys[pygame.K_v] == True: #Checks for V Key - to be repeated for entire keyboard
                    if "V" not in GuessList:
                        GuessList.append("V")
                        turn = "Over"
                elif keys[pygame.K_w] == True: #Checks for W Key - to be repeated for entire keyboard
                    if "W" not in GuessList:
                        GuessList.append("W")
                        turn = "Over"
                elif keys[pygame.K_x] == True: #Checks for X Key - to be repeated for entire keyboard
                    if "X" not in GuessList:
                        GuessList.append("X")
                        turn = "Over"
                elif keys[pygame.K_y] == True: #Checks for Y Key - to be repeated for entire keyboard
                    if "Y" not in GuessList:
                        GuessList.append("Y")
                        turn = "Over"
                elif keys[pygame.K_z] == True: #Checks for Z Key - to be repeated for entire keyboard
                    if "Z" not in GuessList:
                        GuessList.append("Z")
                        turn = "Over"

            def displayLetter( Letter ):
                if Letter.capitalize() == "A":
                    A.Draw(self.Game_Screen)
                elif Letter.capitalize() == "B":
                    B.Draw(self.Game_Screen)
                elif Letter.capitalize() == "C":
                    C.Draw(self.Game_Screen)
                elif Letter.capitalize() == "D":
                    D.Draw(self.Game_Screen)
                elif Letter.capitalize() == "E":
                    E.Draw(self.Game_Screen)
                elif Letter.capitalize() == "F":
                    F.Draw(self.Game_Screen)
                elif Letter.capitalize() == "G":
                    G.Draw(self.Game_Screen)
                elif Letter.capitalize() == "H":
                    H.Draw(self.Game_Screen)
                elif Letter.capitalize() == "I":
                    I.Draw(self.Game_Screen)
                elif Letter.capitalize() == "J":
                    J.Draw(self.Game_Screen)
                elif Letter.capitalize() == "K":
                    K.Draw(self.Game_Screen)
                elif Letter.capitalize() == "L":
                    L.Draw(self.Game_Screen)
                elif Letter.capitalize() == "M":
                    M.Draw(self.Game_Screen)
                elif Letter.capitalize() == "N":
                    N.Draw(self.Game_Screen)
                elif Letter.capitalize() == "O":
                    O.Draw(self.Game_Screen)
                elif Letter.capitalize() == "P":
                    P.Draw(self.Game_Screen)
                elif Letter.capitalize() == "Q":
                    Q.Draw(self.Game_Screen)
                elif Letter.capitalize() == "R":
                    R.Draw(self.Game_Screen)
                elif Letter.capitalize() == "S":
                    S.Draw(self.Game_Screen)
                elif Letter.capitalize() == "T":
                    T.Draw(self.Game_Screen)
                elif Letter.capitalize() == "U":
                    U.Draw(self.Game_Screen)
                elif Letter.capitalize() == "V":
                    V.Draw(self.Game_Screen)
                elif Letter.capitalize() == "W":
                    W.Draw(self.Game_Screen)
                elif Letter.capitalize() == "X":
                    X.Draw(self.Game_Screen)
                elif Letter.capitalize() == "Y":
                    Y.Draw(self.Game_Screen)
                elif Letter.capitalize() == "Z":
                    Z.Draw(self.Game_Screen)
                
            def changeLetterPos(Letter, newX_pos, newY_pos ):
                if Letter.capitalize() == "A":
                    A.X_pos = newX_pos
                    A.Y_pos = newY_pos
                elif Letter.capitalize() == "B":
                    B.X_pos = newX_pos
                    B.Y_pos = newY_pos
                elif Letter.capitalize() == "C":
                    C.X_pos = newX_pos
                    C.Y_pos = newY_pos
                elif Letter.capitalize() == "D":
                    D.X_pos = newX_pos
                    D.Y_pos = newY_pos
                elif Letter.capitalize() == "E":
                    E.X_pos = newX_pos
                    E.Y_pos = newY_pos
                elif Letter.capitalize() == "F":
                    F.X_pos = newX_pos
                    F.Y_pos = newY_pos
                elif Letter.capitalize() == "G":
                    G.X_pos = newX_pos
                    G.Y_pos = newY_pos
                elif Letter.capitalize() == "H":
                    H.X_pos = newX_pos
                    H.Y_pos = newY_pos
                elif Letter.capitalize() == "I":
                    I.X_pos = newX_pos
                    I.Y_pos = newY_pos
                elif Letter.capitalize() == "J":
                    J.X_pos = newX_pos
                    J.Y_pos = newY_pos
                elif Letter.capitalize() == "K":
                    K.X_pos = newX_pos
                    K.Y_pos = newY_pos
                elif Letter.capitalize() == "L":
                    L.X_pos = newX_pos
                    L.Y_pos = newY_pos
                elif Letter.capitalize() == "M":
                    M.X_pos = newX_pos
                    M.Y_pos = newY_pos
                elif Letter.capitalize() == "N":
                    N.X_pos = newX_pos
                    N.Y_pos = newY_pos
                elif Letter.capitalize() == "O":
                    O.X_pos = newX_pos
                    O.Y_pos = newY_pos
                elif Letter.capitalize() == "P":
                    P.X_pos = newX_pos
                    P.Y_pos = newY_pos
                elif Letter.capitalize() == "Q":
                    Q.X_pos = newX_pos
                    Q.Y_pos = newY_pos
                elif Letter.capitalize() == "R":
                    R.X_pos = newX_pos
                    R.Y_pos = newY_pos
                elif Letter.capitalize() == "S":
                    S.X_pos = newX_pos
                    S.Y_pos = newY_pos
                elif Letter.capitalize() == "T":
                    T.X_pos = newX_pos
                    T.Y_pos = newY_pos
                elif Letter.capitalize() == "U":
                    U.X_pos = newX_pos
                    U.Y_pos = newY_pos
                elif Letter.capitalize() == "V":
                    V.X_pos = newX_pos
                    V.Y_pos = newY_pos
                elif Letter.capitalize() == "W":
                    W.X_pos = newX_pos
                    W.Y_pos = newY_pos
                elif Letter.capitalize() == "X":
                    X.X_pos = newX_pos
                    X.Y_pos = newY_pos
                elif Letter.capitalize() == "Y":
                    Y.X_pos = newX_pos
                    Y.Y_pos = newY_pos
                elif Letter.capitalize() == "Z":
                    Z.X_pos = newX_pos
                    Z.Y_pos = newY_pos
           
            #ToDo - possibly add option for AI difficulty to increase     
            if GameMenu == True and OnePlayerGame == False and TwoPlayerGame == False:
                self.Game_Screen.fill(LightGrey_Colour)
                title.Draw(self.Game_Screen)
                onePlayer.Draw(self.Game_Screen)
                twoPlayer.Draw(self.Game_Screen)
                numSelect = random.randint(0,1)
                if event.type == pygame.MOUSEBUTTONDOWN and mousePos[0] >= onePlayer.X_pos and mousePos[1] >= onePlayer.Y_pos and mousePos[0] <= onePlayer.X_pos + 233 and mousePos[1] <=  onePlayer.Y_pos + 34:
                    print(mousePos)
                    print("You clicked on One Player Mode")
                    if click == True:
                        OnePlayerGame = True
                        click = False
                elif mousePos[0] >= twoPlayer.X_pos and mousePos[1] >= twoPlayer.Y_pos and mousePos[0] <= twoPlayer.X_pos + 241 and mousePos[1] <=  twoPlayer.Y_pos + 34:
                    print(mousePos)
                    print("You clicked on Two Player Mode")
                    if click == True:
                        OnePlayerGame = True
                        click = False
                

            

            elif GameMenu == True and RandomWord == False and ChooseWord == False :
                self.Game_Screen.fill(LightGrey_Colour)
                title.Draw(self.Game_Screen)
                selectWord.Draw(self.Game_Screen)
                randomWord.Draw(self.Game_Screen)
                if mousePos[0] >= selectWord.X_pos and mousePos[1] >= selectWord.Y_pos and mousePos[0] <= selectWord.X_pos + 367 and mousePos[1] <=  selectWord.Y_pos + 36:
                    print(mousePos)
                    print("You clicked on Select a Word Mode")
                    if click == True:
                        ChooseWord = True
                        click = False
                elif mousePos[0] >= randomWord.X_pos and mousePos[1] >= randomWord.Y_pos and mousePos[0] <= randomWord.X_pos + 442 and mousePos[1] <=  randomWord.Y_pos + 36:
                    print(mousePos)
                    print("You clicked on Random Word Mode")
                    if click == True:
                        RandomWord = True
                        click = False
                        print (RandomWord)
                        

                #add if statement for if ChooseWord == True
                #if ChooseWord == True, display a list of words

            elif GameMenu == True and RandomWord == True or ChooseWord == True :
                self.Game_Screen.fill(LightGrey_Colour)
                
                if RandomWord == True:

                    
#TODO - Turn into a function for displaying words on screen                 
                    Word = Word_List[numSelect] 
                    X_posList = []
                    print(Word)
                    Counter = 0
                    for Letter in Word:
                        Y_pos = 500 #Yposition of where the word will be displayed
                        if Counter >= 1:
                            X_posList.append(X_posList[Counter - 1] + 33)
                            changeLetterPos(Letter, X_posList[Counter], Y_pos )
                            displayLetter(Letter)
                            Counter = Counter + 1
                            if Counter == len(Word):
                                print (Counter)
                                print(X_posList)
                                Counter = 0
                                
                        elif Counter == 0:
                            X_posList.append(600) # set starting postion of first letter 
                            changeLetterPos(Letter ,X_posList[Counter], Y_pos)
                            displayLetter(Letter)
                            Counter = Counter + 1

                
                       



               
                #add if statement for if ChooseWord == True
                #if ChooseWord == True, display a list of words, ask other player to look away 



            pygame.display.update() #Updates the current frame after completing the loop
            Clock.tick(self.Tick_Rate) #Sets the frame rate per second

pygame.init()

new_game = Game(Screen_Title,Screen_Width,Screen_Height) #creates a new game part of the "game class"

new_game.run_game_loop() #Starts the game loop as defined in the class to continue looping until the game over state becomes true 

pygame.quit()
quit()