#!/bin/python3
import sys
import os
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from tqdm import trange
from time import sleep
from pyfiglet import figlet_format

def header(content='This is the Header'):
    """
    Creates a standardized header style for code uniformity. Headers are made of a string centered inside the Terminal surrounded on both sides by dashes.
    """
    columns = os.get_terminal_size().columns #gets terminal width for centering
    # columns = 20 #temporary for running in vim
    print( content.center(columns, '-') )
    print()

def multiple_choices(inquiry='Make a choice', list_of_choices=['Choice A', 'Choice B', 'Choice C', 'Choice D', 'Choice E', 'Choice F'], feedback='You have chosen: '):
    """
    Simple interface for seamless multiple choices.
    The user will be given a cehoice to which he can give his answer with letters (a-z). This then limitates this to 26 options.

    Definitions:
    Inquiry: This is where you enter (string) the question you are asking
    list_of_choices: This is where you insert as a list all of ther users options.
    """
    print(inquiry)
    option_letter = 65  # A is index 65 in ASCII
    for i in list_of_choices:
        print(chr(option_letter)+': '+i)
        option_letter += 1
    response = input('        :')
    if len(response) > 1:
        print('ERROR: Invalid response - More than one character entered')
    elif ord(response.upper()) > len(list_of_choices) + 65:
        print('ERROR: Response out of Range')
    else:
        # print("Response: "+str(response))
        # print("ord(response.upper()): "+str(ord(response.upper())))
        # print("list_of_choices[ord(response.upper())]: "+str(list_of_choices[ord(response.upper())-65]))
        print()
        print(feedback+list_of_choices[ord(response.upper())-65])
        return list_of_choices[ord(response.upper())-65]

def title(content='This is a Title!'):
    """
    Print titles easily.
    This script clears the terminal screen and then displays in big text your title.
    """
    os.system('clear')
    cprint(figlet_format(content), attrs=['bold'])

def space(nb_of_line=4, pre_text="", post_text=""):
    """
    Enter Space in your script
    This script is pretty sel-explanatory. You can print text befor of after the spacing you desire.
    """
    if len(pre_text) > 0:
        print(pre_text)
    for i in range(nb_of_line):
        print()
    if len(post_text) > 0:
        print(post_text)

def request(inquiry='What is you question?'):
    """
    Aesthetic way to ask for user input.
    Will ask the question to the user on one line and let him answer on the next (indented).
    """
    print(inquiry)
    return input("      :")

def progressbar(milliseconds=5000):
    for i in trange(milliseconds):
        sleep(0.001)
