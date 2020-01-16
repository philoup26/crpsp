#!/usr/bin/python3
from ui import *
from libraries import get_dict
from encrypt import cd
from xml.etree import ElementTree
import xml.etree.cElementTree as ET
import random as rdm
from tqdm import tqdm
from file_read_backwards import FileReadBackwards
from encrypt import traduce
from encrypt import xor

def chunkstring(string, length):
    """
    transforme le message encrypté en morceaux pour que le dictionaire reconnaisse les différentes lettres
    """
    return (string[0+i:length+i] for i in range(0, len(string), length))


def crpsp_decryption(encrypted_message, xml_message_path, indexPath):
    """
    Take the a message and path to an random xml data library
    encrypted_message: xml file name (ex: encrypted_message.xml)
    xml_message_path: ~/Documents/crpsp/test_env/
    index_path: ~/Documents
    """
    all_dictionaries = get_dict()
    cd(xml_message_path)  # Go into the index
    message_tree = ElementTree.parse(encrypted_message)
    message_root = message_tree.getroot()

    for data in message_root.iter('encoding_type'):
        encodage = data.text
    for data in message_root.iter('d_key_ID'):
        d_key_ID = data.text
    for data in message_root.iter('subject'):
        subject = data.text
    for data in message_root.iter('preface'):
        preface = data.text
    for data in message_root.iter('contents'):
        contents = data.text
    for data in message_root.iter('postface'):
        postface = data.text

    xmlPath = d_key_ID[0:2]+"/"+d_key_ID[3:5]#+"/"+randomxml[6:8]
    cd(lib_path+xmlPath)
    lib_tree = ElementTree.parse(d_key_ID)
    lib_root = lib_tree.getroot()
    cle = ""
    for random_data in lib_root.iter('random-data'):
        cle = random_data.text
        cle = cle.replace('\n', ' ').replace('\r', '').replace(' ', '').replace('\t', '')

    # Voici les variables a ta diposition:
    # contents: Message encrypte sous la forme binaire en string
    # cle: contenu de la cle au format hexadecimal
    # encodage: type d'encodage (on a pas de variable decodage)

    clef=traduce(cle,all_dictionaries['autres']['hexToBinaryTable'])
    if len(clef)>=len(contents):  #si la clé est plus longue ou de même longueur au message
        g=len(clef)-len(contents)  #détermine de combien de bits la clé est plus longues
        clef=clef[:-g]  #retire des bits à la clé pour qu'elle soit exactement de même longueur que la clé
        breadcrumbs=cle[((len(contents))//4)+1:]
    else:
        exit("the key is not long enough!")   #ferme le programme avec un message d'erreur puisque la clé n'est pas assez longue

    # print("Hex key: "+cle)
    # print("Binary key: "+clef)
    # print("Binary undecrypted messsage: "+contents)
    decrypted_contents = xor(clef, contents)
    # print("Binary decrypted messsage: "+decrypted_contents)
    decrypted_contents = list(chunkstring(decrypted_contents, all_dictionaries['encodages'][encodage]['nb_of_bits']))
    # print("Chunked decrypted messsage: ")
    # print(decrypted_contents)
    decrypted_contents = traduce(decrypted_contents, all_dictionaries['decodages'][encodage])
    # print("Decrypted messsage: "+decrypted_contents)
    # print(decrypted_contents)

    os.system("rm "+d_key_ID)
    for i in range(2):
        os.chdir("..")
    log = open("log.txt", "a+")
    log.write("\nS : "+d_key_ID)  # Sets the name (ID) of every file based on it's index)
    log.close()
    breadcrumbs_file = open("breadcrumbs.txt", "a+")
    breadcrumbs_file.write(breadcrumbs)  # Sets the name (ID) of every file based on it's index)
    breadcrumbs_file.close()
    header("Subject:")
    print(subject)
    header("Contents:")
    print(preface+" \n"+decrypted_contents+" \n"+postface)
    # print(preface+" "+decrypted_contents+" "+postface)




def main(full_message_path, lib_path):
    """
    The decryption protocol will receive as input the
    filepath (including the filename) of the message which
    needs to be decrypted as well as the path to the xml
    random data library. It will use the metadata of the
    message to find the correct xml file to use with for
    the decryption. The file will then be decyphered
    BUT NOT WRITTEN TO DISK to prevent recuperation of the
    data by unwanted viewers. The used data for the
    decyphering of the message will then be deleted from
    the original xml key and sent to the breadcrumbs folder.
    """
    os.system("clear")
    title("Decryption")

    split_message_path = full_message_path.split("/")  # Every subfloder (and the file is an item in the list)
    encrypted_message = split_message_path[len(split_message_path)-1]  # File is the last item in the list
    split_message_path.pop(len(split_message_path)-1)  # Remove the file from the file list
    message_path = "" # sets an empty variable to receive the file path as a single string
    for i in split_message_path:  # Considers every folder in the path
        message_path += i+"/"  # appends the folder and a slash to recreate the filepath
    crpsp_decryption(encrypted_message, message_path, lib_path)


if __name__ == "__main__":
    # Remove the two following lines for the duration of the testing phase:
    full_message_path = request("What is the path to the message that is to be decyphered?")
    lib_path = request("What is the path to the library which is needed for the decyphering process?")
    # full_message_path = "~/Documents/crpsp/test_env/asdf.xml"
    # lib_path = "~/Documents/crpsp/test_env/decryption_lib.crpsp/"

    main(full_message_path, lib_path)
