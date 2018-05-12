#-*- coding: utf-8 -*-
""" programme qui dit bonjour.
    Il suffit d'écrire des prénoms dans le fichier prenoms.txt
    et d'exécuter : 
    python bonjour.py
"""

# fichier où sont contenus les prénoms
fichier = open("prenoms.txt","r")

# boucle de lecture des prénoms dans le fichier
for prenom in fichier:
    print ("Bonjour {}".format(prenom)) # écriture du bonjour
