from ui import *
from xml.etree import ElementTree
import xml.etree.cElementTree as ET
import random as rdm
from tqdm import tqdm
from file_read_backwards import FileReadBackwards

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
    with open(fname) as f:
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
    pbar = tqdm(total=file_len(m)*2)
    with FileReadBackwards(m) as LogFile:  # Opens the log file (read backwds)
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

def crpsp_protocol(message, indexPath="/home/master/Documents/crpsp/software_source/test00"):
    """
    Take the a message and path to an random xml data library
    """

    print("Finding correct randomness xml file to use...")
    os.chdir(indexPath)  # Go into the index
    randomxml = next(findSInLog(indexPath+"log.txt"))
    print("Done!")
    space(2)
    print(randomxml+" will be used.")
    print("Encrypting...")
    xmlPath = randomxml[0:2]+"/"+randomxml[3:5]#+"/"+randomxml[6:8]
    os.chdir(indexPath+xmlPath)
    tree = ElementTree.parse(randomxml)
    root = tree.getroot()
    cle = ""
    for random_data in root.iter('random-data'):
        cle = random_data.text
        cle = cle.replace('\n', ' ').replace('\r', '').replace(' ', '').replace('\t', '')

    encodage_cinq_bit = {'a': '00000', 'b': '00001', 'c': '00010', 'd': '00011', 'e': '00100', 'f': '00101', 'g': '00110', 'h': '00111', 'i': '01000', 'j': '01001', 'k': '01010', 'l': '01011', 'm': '01100', 'n': '01101', 'o': '01110', 'p':'01111', 'q': '10000', 'r': '10001', 's': '10010', 't': '10011', 'u': '10100', 'v': '10101', 'w': '10110', 'x': '10111', 'y': '11000', 'z': '11001', '_': '11010', '.': '11011', '-': '11100', ',': '11101', '(': '11110', ')': '11111'}
    decodage_cinq_bit = {'00000': 'a', '00001': 'b', '00010': 'c', '00011': 'd', '00100': 'e', '00101': 'f', '00110':'g', '00111': 'h', '01000': 'i', '01001': 'j', '01010': 'k', '01011': 'l', '01100': 'm', '01101': 'n', '01110': 'o', '01111': 'p', '10000': 'q', '10001': 'r', '10010': 's', '10011': 't', '10100': 'u', '10101': 'v', '10110': 'w', '10111': 'x', '11000': 'y', '11001': 'z', '11010': '_', '11011': '.', '11100': '-', '11101': ',', '11110': '(', '11111': ')'}
    hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4': '0100', '5': '0101', '6':'0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    #assigner la clé en hexadecimal ici

    clef=traduce(cle,hexToBinaryTable) #transforme la clé en binaire selon le dictionaire hexToBinaryTable
    msg=traduce(message,encodage_cinq_bit)  #tranforme le message en binaire selon le dictionaire encodage_cinq_bit
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
    return output



    progressbar()  # TODO: maybe link each char with the pbar...
    # TODO: Actually make the encryption protocol
    pass

def main():
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
    list_of_encodings = [
    "encodage_cinq_bit",
    ]
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

    # Encrypted Contents - TODO: Actually apply the XOR function to the contents
    header("Encrypted Content")
    message = request("Please enter the content which you would like to encrypt (maximum 140 characters):")
    encryption_result = crpsp_protocol(message, "/home/master/Documents/crpsp/software_source/test00/")
    ET.SubElement(doc, "contents").text = encryption_result[0]
    space(4)

    # Postface (into xml)
    header("Message Postface")
    postface = request("Please enter the message's postface (Maximum 500 characters)")
    ET.SubElement(doc, "postface").text = postface  # The postface of the message
    space(4)

    ### To be completed from here: ###

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
    main()
