#!/usr/bin/env python
# vim:fileencoding=utf-8
n=5 #créateur de table d'encodage
l2= ['{:0{}b}'.format(i, n) for i in range(1 << n)] #a list wih all binary numbers of n lenght
l1= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','.','-',',','(',')']#doesn't work with spaces so deal with it (there are ways of replacing a character like _ with a space )
d1={} #an empty dictionary
def list_to_dictionary(l1,l2):
    for l1_ in l1:
        for l2_ in l2:
            d1[l1_] = l2_
            l2.remove(l2_)
            break
#creates a dictionary from two lists
list_to_dictionary(l1,l2)
#dictionaries that I have already made
encodage= {'a': '00000', 'b': '00001', 'c': '00010', 'd': '00011', 'e': '00100', 'f': '00101', 'g': '00110', 'h': '00111', 'i': '01000', 'j': '01001', 'k': '01010', 'l': '01011', 'm': '01100', 'n': '01101', 'o': '01110', 'p':'01111', 'q': '10000', 'r': '10001', 's': '10010', 't': '10011', 'u': '10100', 'v': '10101', 'w': '10110', 'x': '10111', 'y': '11000', 'z': '11001', '_': '11010', '.': '11011', '-': '11100', ',': '11101', '(': '11110', ')': '11111'}
decodage= {'00000': 'a', '00001': 'b', '00010': 'c', '00011': 'd', '00100': 'e', '00101': 'f', '00110':'g', '00111': 'h', '01000': 'i', '01001': 'j', '01010': 'k', '01011': 'l', '01100': 'm', '01101': 'n', '01110': 'o', '01111': 'p', '10000': 'q', '10001': 'r', '10010': 's', '10011': 't', '10100': 'u', '10101': 'v', '10110': 'w', '10111': 'x', '11000': 'y', '11001': 'z', '11010': '_', '11011': '.', '11100': '-', '11101': ',', '11110': '(', '11111': ')'}
hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4': '0100', '5': '0101', '6':'0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

#traduit (ce que je veux transformer en texte ou en binaire, le dictionaire d'encodage)
def traduce (key, table):
    """
    traduit (ce que je veux transformer en texte ou en binaire, le dictionaire d'encodage)
    """
    final_hexToBinary = ''
    for each  in key:
        final_hexToBinary+=table[each]
    return(final_hexToBinary)
#encryptage

cle="8271AF53973984893465"  #assigner la clé en hexadecimal ici
message="ben_et" #assigner le message ici

clef=traduce(cle,hexToBinaryTable) #transforme la clé en binaire selon le dictionaire hexToBinaryTable
msg=traduce(message,encodage)  #tranforme le message en binaire selon le dictionaire encodage
if len(clef)>=len(msg):  #si la clé est plus longue ou de même longueur au message
    g=len(clef)-len(msg)  #détermine de combien de bits la clé est plus longues
    clef=clef[:-g]  #retire des bits à la clé pour qu'elle soit exactement de même longueur que la clé
    breadcrumbs=cle[((len(msg))//4)+1:]
else:
    exit("the key is not long enough!")   #ferme le programme avec un message d'erreur puisque la clé n'est pas assez longue
print(breadcrumbs)
print(clef)    #imprime la clé en binaire
print(msg)    #imprime le message en binaire
def xor(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))
#une fonction qui permet de xor deux strings contenant uniquement des 1 et des 0 en conservant les 0 flottant au début
crya=xor(msg,clef)  #encrypte le message
print(crya)        #imprime le message encrypté en binaire

#décryptage

cryb=xor(clef,crya) #décrypte pour donner la même chose que le message en binaire(msg)
print(cryb)  #imprime le message décrypté en binaire
def chunkstring(string, length):
    """
    transforme le message encrypté en morceaux pour que le dictionaire reconnaisse les différentes lettres
    """
    return (string[0+i:length+i] for i in range(0, len(string), length))

cryp=list(chunkstring(cryb, n))
#transforme les morceaux en liste
msg2=traduce(cryp,decodage) #décode la liste binaire pour la transformer en texte
print(msg2) #imprime le message en texte
