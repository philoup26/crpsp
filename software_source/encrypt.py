#!/usr/bin/python3
from ui import *
from libraries import get_dict
from xml.etree import ElementTree
import xml.etree.cElementTree as ET
import random as rdm
from tqdm import tqdm
from file_read_backwards import FileReadBackwards

def cd(path):
    """
    Better Integrated chdir
    """
    os.chdir(os.path.expanduser(path))

def traduce (key, table):
    """
    traduit (ce que je veux transformer en texte ou en binaire, le dictionaire d'encodage_cinq_bit)
    """
    final_hexToBinary = ''
    for each  in key:
        final_hexToBinary+=table[each]
    return(final_hexToBinary)

def xor(x, y):
    """
    Permet de xor deux strings contenant uniquement des 1 et des 0
    en conservant les 0 flottant au début.
    """
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

def file_len(fname="/Users/Benjamin/Documents/crpsp/testIndex.crpsp/log.txt"):
    """
    Outputs how many lines the log.txt file has.
    """
    test = os.getcwd()
    with open(test+"/log.txt") as f:
        for i, l in enumerate(f):
            pass
        return i + 1

def next(i_d="32-99-09.xml"):
    """
    Input the name of an xml file and it will output the name of the next file
    in the index.
    example:
        Input: "00-12-56.xml"
        Output: "00-12-57.xml"
    """
    intIDlast  = int(i_d[6:8])  # Defines the last two digits (int)
    intIDmid   = int(i_d[3:5])  # Defines the middle two digits (int)
    intIDfirst = int(i_d[0:2])  # Defines the first two digits (int)
    if intIDlast != 99:  # Makes sure it is possible to add one
        intIDlast += 1  # Add one
        return i_d[0:6]+str(f"{intIDlast:02d}")+".xml"  #
    elif intIDmid != 99:  # Makes sure it is possible to add one
        intIDmid += 1  # Add one
        return i_d[0:3]+str(f"{intIDmid:02d}")+"-00.xml"  #
    elif intIDfirst != 99:  # Makes sure it is possible to add one
        intIDfirst += 1  # Add one
        return str(f"{intIDfirst:02d}")+"-00-00.xml"  #
    else:
        return "ERROR - Reached end of index."

def previous(i_d="32-10-00.xml"):
    """
    Input the name of an xml file and it will output the name of the previous file
    in the index.
    example:
        Input: "00-12-56.xml"
        Output: "00-12-55.xml"
    """
    intIDlast  = int(i_d[6:8])  # Defines the last two digits (int)
    intIDmid   = int(i_d[3:5])  # Defines the middle two digits (int)
    intIDfirst = int(i_d[0:2])  # Defines the first two digits (int)
    if intIDlast != 00:  # Makes sure it is possible to substract one
        intIDlast -= 1  # Substract one
        return i_d[0:6]+str(f"{intIDlast:02d}")+".xml"
    elif intIDmid != 00:  # Makes sure it is possible to substract one
        intIDmid -= 1  # Substract one
        return i_d[0:3]+str(f"{intIDmid:02d}")+"-99.xml"
    elif intIDfirst != 00:  # Makes sure it is possible to substract one
        intIDfirst -= 1  # Substract one
        return str(f"{intIDfirst:02d}")+"-99-99.xml"
    else:
        return "00-00-00.xml"

def documentation(lst=["a", "b", "c"]):
    """
    Prints stuff line by line with a delay so that the text doesn't show up
    all at once.
    """
    for i in lst:
        print(i)
        sleep(0.3)

def findSInLog(m="/home/master/Documents/crpsp/software_source/test00"):
    """
    This function will determine using the log, what is the last file that was deleted (or sent to BreadCrumbs).
    This will allow the encryption protocol to determine which file to use.
    """
    test = os.path.abspath("~/")
    test = test[:-1]
    pbar = tqdm(total=file_len(test)*2)
    with FileReadBackwards(test+"/log.txt") as LogFile:  # Opens the log file (read backwds)
        i_d = None
        for line in (LogFile):  # Searched every line from the bottom for S or D
            pbar.update(1)
            if line[0] == "S":  # S: sent to BC, D: deleted.
                i_d = line[4:16]  # id does not include "C", "D" operator.
                return i_d        # ex: "99-48-74.xml"
                pbar.close()
                break
            pbar.update(1)
            if line[0] == "D":  # S: sent to BC, D: deleted.
                i_d = line[4:16]  # id does not include "C", "D" operator.
                return i_d        # ex: "99-48-74.xml"
                pbar.close()
                break
        if i_d == None:
            return "00-00-00.xml"
            pbar.close()

def crpsp_protocol(message, indexPath, encodage):
    """
    Take the a message and path to an random xml data library
    """
    print("Finding correct randomness xml file to use...")
    all_dictionaries = get_dict()
    cd('~/')  # Go into the index
    cd(indexPath)  # Go into the index
    randomxml = next(findSInLog(indexPath+"log.txt"))
    print("Done!")
    space(2)
    print(randomxml+" will be used.")
    print("Encrypting...")
    xmlPath = randomxml[0:2]+"/"+randomxml[3:5]#+"/"+randomxml[6:8]
    cd(indexPath+xmlPath)
    tree = ElementTree.parse(randomxml)
    root = tree.getroot()
    cle = ""
    for random_data in root.iter('random-data'):
        cle = random_data.text
        cle = cle.replace('\n', ' ').replace('\r', '').replace(' ', '').replace('\t', '')


    #assigner la clé en hexadecimal ici

    clef=traduce(cle, all_dictionaries['autres']['hexToBinaryTable']) #transforme la clé en binaire selon le dictionaire hexToBinaryTable
    msg=traduce(message, all_dictionaries['encodages'][encodage])  #tranforme le message en binaire selon le dictionaire encodage_cinq_bit  #TODO: Laisser l'utilisateur choisir le type d'encodage
    if len(clef)>=len(msg):  #si la clé est plus longue ou de même longueur au message
        g=len(clef)-len(msg)  #détermine de combien de bits la clé est plus longues
        # les "g/4" derniers caractères de la clé ne sont pas utilisé
        #TODO: replace the random contents of the xml file with the value of g (and move the xml file to BreadCrumbs)
        clef=clef[:-g]      #retire des bits à la clé pour qu'elle soit exactement de même longueur que la clé
        breadcrumbs=cle[((len(msg))//4)+1:]  #les breadcrumbs sont créés
    else:
        exit("the key is not long enough!")   #ferme le programme avec un message d'erreur puisque la clé n'est pas assez longue
    #TODO assigné le string breadcrumbs au fichier xml dans le dossier breadcrumbs
    #une fonction qui permet de xor deux strings contenant uniquement des 1 et des 0 en conservant les 0 flottant au début
    crya=xor(msg,clef)  #encrypte le message
    print(crya)
    output = [crya, randomxml]
    os.system("rm "+randomxml)
    for i in range(2):
        os.chdir("..")
    log = open("log.txt", "a+")
    log.write("\nS : "+randomxml)  # Sets the name (ID) of every file based on it's index)
    log.close()
    breadcrumbs_file = open("breadcrumbs.txt", "a+")
    breadcrumbs_file.write(breadcrumbs)  # Sets the name (ID) of every file based on it's index)
    breadcrumbs_file.close()
    return output



    progressbar()  # TODO: maybe link each char with the pbar...
    # TODO: Actually make the encryption protocol
    pass

def main(lib_path):
    """
    "Proper" introduction...
    """  #TODO: Write a proper introduction

    #TODO: Setup the CWD to be inside of the USB key for transport

    root = ET.Element("root")  # Initializes the root of the XML file.
    doc  = ET.SubElement(root, "doc")  # The doc file contains the user side data
    title("Encryption Protocol")  # prints the title

    header("Documentation")
    # TODO: print the explanation of the message structure.
    docs = [
            "line 1",
            "line 2",
            "line 3"
            ]
    documentation(docs)
    space(4)

    # Encoding (into xml)
    header("Type d'encodage")
    list_of_encodings = []
    all_dictionaries = get_dict()
    for available_encodings in all_dictionaries['encodages']:
        list_of_encodings.append(available_encodings)

    encodage_choisi = multiple_choices("Please enter the encoding you desire:", list_of_encodings)
    space(4)

    # Subject (into xml)
    header("Message Subject")
    subject = request("Please enter the message's subject (Maximum 140 characters)")
    ET.SubElement(doc, "subject").text  = subject  # The subject
    space(4)

    # Preface (into xml)
    header("Message Preface")
    preface = request("Please enter the message's preface (Maximum 500 characters)")
    ET.SubElement(doc, "preface").text  = preface  # The preface
    space(4)

    # Encrypted Contents
    header("Encrypted Content")
    message = request("Please enter the content which you would like to encrypt (maximum 140 characters):")
    encryption_result = crpsp_protocol(message, lib_path, encodage_choisi)
    ET.SubElement(doc, "contents").text = encryption_result[0]
    space(4)

    # Postface (into xml)
    header("Message Postface")
    postface = request("Please enter the message's postface (Maximum 500 characters)")
    ET.SubElement(doc, "postface").text = postface  # The postface of the message
    space(4)

    ### TODO: To be completed from here: ###

    # Closes and writes the xml file
    doc = ET.SubElement(root, "doc")  # The document holder for things seen by the user.
    doc = ET.SubElement(root, "processes")  # The holder for data needed for subprocesses (index deletion etc.)
    ET.SubElement(doc, "encoding_type", name="Encoding Type").text = encodage_choisi  # The index of the key in which data needs to be deleted.
    ET.SubElement(doc, "d_key_ID", name="Used Key for Encryption").text = encryption_result[1]  # The index of the key in which data needs to be deleted.

    tree = ET.ElementTree(root)  # Sets a tree to be written from the XML structure
    ran = rdm.randrange(10**80)  # Random generator for filename
    myhex = "%064x" % ran  # Conversion of randomness to hex
    tree.write(myhex +".xml")  # Write the XML file with myhex as it's name
    space(4)
    header("All Done!")
    print("Your message has been encrypted to: "+myhex+".xml")
    space(1)
    os.chdir("..")
    print("It is located at: "+os.getcwd())
    os.getcwd()

if __name__ == "__main__":
    lib_path = request("Where is the library folder located (not including the '.crpsp' file extension)?")+".crpsp/"
    if not os.path.exists(lib_path):
        os.system("mkdir -p "+lib_path)
    main(lib_path)
