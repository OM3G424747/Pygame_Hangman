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
        Game_Over = False
        GameMenu = True
        OnePlayerGame = False #sets game into a state where you play against the CPU
        TwoPlayerGame = False #sets game into a two player state where you play against another player 
        ChooseWords = False
        letterGuessed = ""
        turn = ""

        while Game_Over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_Over = True
                keys = pygame.key.get_pressed()  
                if keys[pygame.K_ESCAPE] == True:
                    Game_Over = True 
               
                print(keys)

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

            #ToDo - possibly add option for AI difficulty to increase     
            if GameMenu == True
            self.Game_Screen.fill(Grey_Colour)

            elif GameMenu == False and OnePlayerGame == True:
                pass
                #add if statement for if ChooseWord == True
                #if ChooseWord == True, display a list of words

            elif GameMenu == False and TwoPlayerGame == True:
                pass
                #add if statement for if ChooseWord == True
                #if ChooseWord == True, display a list of words, ask other player to look away 

            pygame.display.update() #Updates the current frame after completing the loop
            Clock.tick(self.Tick_Rate) #Sets the frame rate per second

pygame.init()

new_game = Game(Screen_Title,Screen_Width,Screen_Height) #creates a new game part of the "game class"

new_game.run_game_loop() #Starts the game loop as defined in the class to continue looping until the game over state becomes true 

pygame.quit()
quit()