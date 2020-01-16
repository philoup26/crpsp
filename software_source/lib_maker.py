#!/bin/python3
import os
from file_read_backwards import FileReadBackwards
import urllib.request as urllib
from random import *
from shutil import copyfile
from encrypt import file_len
import tqdm
import time
import subprocess

def vpnConfirm(vpnLocation="USA - New Jersey - 1"):
    """
    <--- does not compute --->
    """
    os.system('expressvpn status > tmp')
    # status = subprocess.getstatusoutput('expressvpn status')
    expectedResult = "Connected to "+vpnLocation+"\n\n   - If your VPN connection unexpectedly drops, internet traffic will be blocked to protect your privacy.\n   - To disable Network Lock, disconnect ExpressVPN then type 'expressvpn preferences set network_lock off'."
    if open('tmp', 'r').read() == expectedResult:
        return True
    else:
        print("Expected: ")
        print(expectedResult)
        print("Got: ")
        print(open('tmp', 'r').read())
    # print(status)
    # if p == expectedResult:
    #     return True
    # else:
    #     print("VPN connection error!")
    #     print("Expected:\n\n"+expectedResult)
    #     print("Got:")
    #     print()
    #     print(p)
    #     return False

def vpnConnect(vpnLocation="smart"):
    """
    <--- fonctionne --->
    """
    os.system("expressvpn connect "+vpnLocation)
    print("Connected to the "+vpnLocation+" server location via expressvpn")

def downloadHotBits(API="Pseudorandom", filename="blabla.xml"):
    """
    <--- fonctionne --->

    """
    url = "https://www.fourmilab.ch/cgi-bin/Hotbits?nbytes=2048&fmt=xml&apikey=" + API
    urllib.urlretrieve(url, filename)

def request(inquiry="Please insert your message:"):
    """
    <--- fonctionne --->
    Creates a pleasing UI inside the terminal for the user to respond to requests.
    At the beggining of each request, the terminal screen is cleared.
    The question is printed on one line and the user can enter his response on the line below it.
    """
    os.system("clear")
    print(inquiry)
    return input("           : ")

def findXInLog(m="/Users/Benjamin/Documents/crpsp/software_source/test00/log.txt"):
    """
    <--- fonctionne --->
    This function will determine using the log, what is the last file that was created.
    This will allow the encryption protocol to determine which file to use.
    """
    last_item_index = []  # liste vide
    with FileReadBackwards(m) as LogFile:  # Opens the log file (read backwds)
        for line in (LogFile):  # Searched every line from the bottom for S or D
            if line[0] == "X":  # If we find the last created file
                i = int(line[4])*10  # id does not include "C", "D" operator.
                i += int(line[5])  # id does not include "C", "D" operator.
                print("The i value is: ", i)
                last_item_index.append(i)
                j = int(line[7])*10  # id does not include "C", "D" operator.
                j += int(line[8])  # id does not include "C", "D" operator.
                last_item_index.append(j)
                print("The j value is: ", j)
                k = int(line[10])*10  # id does not include "C", "D" operator.
                k += int(line[11])  # id does not include "C", "D" operator.
                last_item_index.append(k)
                print("The k value is: ", k)
                return last_item_index        # ex: "99-48-74.xml"
                break
        # if last_item_index == []:
        #     return "Null"


def xml_duplicate(file_name="00", template_path="./", template_name=".template_2048"):  # Funnction for creating the XML Files
    """
    Creates a duplicate of a set XML file with it's own name
    """
    os.system("touch "+file_name+".xml")  # Creates a blank XML file
    origin = template_path+"/"+template_name+".xml"
    destination = "./"+file_name+".xml"
    copyfile(origin, destination)

def main(structure_location="./", index_folder_name="test00"):
    """
    Creates an xml indexed database in a set location.
    Every XML file will be a copy of a template XML file priorly set.
    The index is structured in a way that it has (A) 100 folders (00-99) all containing (B) 100 folders (00-99) which themselves contain 100 XML files (AA-BB-XX.xml) that are all a copy of the set template XML file.
    """
    template_path = os.getcwd()
    os.chdir(structure_location)  # Sets the current working directory
    if not os.path.exists(index_folder_name):
        os.mkdir(index_folder_name)  # Creates a recipient folder for the index
    os.chdir("./"+index_folder_name)  # Enters the directory to start the index
    log = open("log.txt", "a+")
    log.close()
    list_antecedents = findXInLog("./log.txt")
    if list_antecedents == None:
        list_antecedents = [0,0,0]

    for i in range(100-list_antecedents[0]):  # First layer of 00-99 folders
        ni = i+int(list_antecedents[0])  # ni stands for new i value
        if not os.path.exists(f"{i:02d}"):
            os.mkdir(f"{ni:02d}")  # name of the folder (adds a 0 to 01)
        os.chdir("./"+ f"{ni:02d}")  # Go inside that folder
        if ni == 99:
            list_antecedents[0] = 0

        for j in range(100-list_antecedents[1]):  # Second layer of 00-99 folders
            nj = j+int(list_antecedents[1])  # ni stands for new i value
            if not os.path.exists(f"{j:02d}"):
                os.mkdir(f"{nj:02d}")  # name of the folder (adds a 0 to 01)
            os.chdir("./"+ f"{nj:02d}")  # Go inside that folder
            if nj == 99:
                list_antecedents[1] = 0

            for k in range(100-list_antecedents[2]):  # Loop for creating the actual XML files
                nk = k+int(list_antecedents[2])  # ni stands for new i value
                xml_name = f"{ni:02d}"+"-"+f"{nj:02d}"+"-"+f"{nk:02d}"+".xml"  # Sets the name (ID) of every file based on it's index
                downloadHotBits("Pseudorandom", xml_name)
                # xml_duplicate(xml_name, template_path)  # Creates the XML file using the xml_files function
                os.chdir("..")
                os.chdir("..")
                log = open("log.txt", "a+")
                log.write("X : "+f"{ni:02d}"+"-"+f"{nj:02d}"+"-"+f"{nk:02d}"+".xml \n")  # Sets the name (ID) of every file based on it's index)
                log.close()
                os.chdir(f"{ni:02d}"+"/"+f"{nj:02d}")
                if nk == 99:
                    list_antecedents[2] = 0
            os.chdir("..")
        os.chdir("..")

if __name__ == "__main__":
    # if request("Do you want to create the index folder in the current directory (Y/N)?").lower == "y" or "yes":
    #     structure_location = "./"
    # else:
    #     structure_location = request("In which directory would you like the index to be located? (folder path)?")
    # index_folder_name = request("Enter the name of your index folder:")
    # index_folder_name.replace(" ", "_")
    # main(structure_location, index_folder_name)
    main()
