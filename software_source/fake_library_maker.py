#!/usr/bin/env python
# vim:fileencoding=utf-8
import os
import urllib
from random import *
from shutil import copyfile

def downloadHotBits(API="Pseudorandom", filename="blabla.xml"):
    url = "https://www.fourmilab.ch/cgi-bin/Hotbits?nbytes=2048&fmt=xml&apikey=" + API
    urllib.request.urlretrieve(url, filename)

def request(inquiry="Please insert your message:"):
    """
    Creates a pleasing UI inside the terminal for the user to respond to requests.
    At the beggining of each request, the terminal screen is cleared.
    The question is printed on one line and the user can enter his response on the line below it.
    """
    os.system("clear")
    print(inquiry)
    return input("           : ")

def xml_files(file_name="00", template_path="./", template_name=".template_2048"):  # Funnction for creating the XML Files
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
    os.mkdir(index_folder_name)  # Creates a recipient folder for the index
    os.chdir("./"+index_folder_name)  # Enters the directory to start the index

    for i in range(100):  # First layer of 00-99 folders
        os.mkdir(f"{i:02d}")  # name of the folder (adds a 0 to 01)
        os.chdir("./"+ f"{i:02}")  # Go inside that folder

        for j in range(100):  # Second layer of 00-99 folders
            os.mkdir(f"{j:02d}")  # name of the folder (adds a 0 to 01)
            os.chdir("./"+ f"{j:02}")  # Go inside that folder

            for k in range(100):  # Loop for creating the actual XML files
                xml_name = f"{i:02d}"+"-"+f"{j:02d}"+"-"+f"{k:02d}"  # Sets the name (ID) of every file based on it's index
                xml_files(xml_name, template_path)  # Creates the XML file using the xml_files function
            os.chdir("..")
        os.chdir("..")

if __name__ == "__main__":
    if request("Do you want to create the index folder in the current directory (Y/N)?").lower == "y" or "yes":
        structure_location = "./"
    else:
        structure_location = request("In which directory would you like the index to be located? (folder path)?")
    index_folder_name = request("Enter the name of your index folder:")
    index_folder_name.replace(" ", "_")
    main(structure_location, index_folder_name)
