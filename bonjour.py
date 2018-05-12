#-*- coding: utf-8 -*-

fichier = open("prenoms.txt","r")

for prenom in fichier:
    print ("Bonjour {}".format(prenom))
