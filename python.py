from tkinter import * #Python GUI platform
import customtkinter #Extention of tkinter
import pygame #Python game library

#Constants
window_width=500 #Width of the window
window_height=600 #Height of the window
bg_colour="#1e4f8f" #Background colour of the window

root = Tk() #Creates the main window for the GUI

root.geometry(f"{window_width}x{window_height}") #Size of the window

# Title screen shown when the program starts
def title_screen():
    titleScreen = Frame(root, bg=bg_colour) #Creates a frame and sets the background colour of the screen
    titleScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions
    Label(titleScreen, text="TITLE SCREEN", font=("Arial", 20)).pack(pady=40)
    Button(titleScreen, text="Go to Settings", command=settings_screen).pack()


# Screen for creating a new user account
def registration_screen():
    registrationScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    registrationScreen.place(x=0, y=0, width=window_width, height=window_height)#Positions the frame at the top-left corner and sets its dimensions

    

# Screen for user login
def login_screen():
    loginScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    loginScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Screen for resetting or changing a password
def forgot_password_screen():
    forgotPasswordScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    forgotPasswordScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Main menu after successful login
def menu_screen():
    menuScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    menuScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Screen to select a racing track
def track_select_screen():
    trackSelectScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    trackSelectScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Screen to select player mode
def player_select_screen():
    playerSelectScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    playerSelectScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Screen to select a car
def car_select_screen():
    carSelectScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    carSelectScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Screen to select difficulty
def difficulty_screen():
    difficultyScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    difficultyScreen.place(x=0, y=0, width=window_width, height=window_height)#Positions the frame at the top-left corner and sets its dimensions


# Game settings screen
def settings_screen():
    settingsScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    settingsScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions

# Tutorial screen
def tutorial_screen():
    tutorialScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    tutorialScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Brightness settings screen
def brightness_screen():
    brightnessScreen= Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    brightnessScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Music settings screen
def music_screen():
    musicScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    musicScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


# Leaderboard screen
def leaderboard_screen():
    leaderboardScreen = Frame(root, bg=bg_colour)#Creates a frame and sets the background colour of the screen
    leaderboardScreen.place(x=0, y=0, width=window_width, height=window_height) #Positions the frame at the top-left corner and sets its dimensions


title_screen()
root.mainloop() #Creates the window and waits for the user to interact with it

