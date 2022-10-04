from random import choice, randint #Importation des bibliothèques

'''Création des listes pour le mot de passe'''
chiffres = ['1','2','3','4','5','6','7','8','9','0']
lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettresMajuscule = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caracteres = ['!','$','#','@','+','=','*','£','%']


'''Creation de la fonction qui génère le mot de passe'''
def pwd(n, min = True, maj = True, chif = True, cs = True): #n(nombre de caractère du mdp), min(minuscule), maj(Majuscule), chif(chiffre), cs(caracteres speciaux)
    alphabets = dict()
    key = 0
    if min:
        alphabets[key] = lettres
        key += 1
    if maj:
        alphabets[key] = lettresMajuscule
        key += 1
    if chif:
        alphabets[key] = chiffres
        key += 1
    if cs:
        alphabets[key] = caracteres
        key += 1

    mdp = ''

    '''Boucle alternative pour n'''
    for i in range(n):
            s = randint(0,key-1)
            mdp += choice( alphabets[s] )
    return mdp
