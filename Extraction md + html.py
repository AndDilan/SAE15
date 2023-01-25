import numpy as np
import datetime
import os
import csv
import typing
import matplotlib.pyplot as plt


try:
    with open("analyse.txt", encoding="utf8") as fh:
        res=fh.read()
except:
        print("Le fichier n'existe pas %s", os.path.abspath('fichieratraiter.txt'))
ress=res.split('\n')
tab_dest=np.array([])
tableau_evenements=np.array([])
fic=open("test.csv", "w")#Le fichier d'extraction sera test.csv
evenement = "Date ; Source ; Port utilisé ; Destination ; Flag ; SEQ ; ACK ; WIN ; Options ; Length" #Attribution du nom des colonnes
fic.write(evenement + "\n")
characters = ":"
for event in ress:
        if event.startswith('11:42'): #Heure de début
#Déclaration des variables
            date = ""
            source = ""
            port = ""
            flag = ""
            seq= ""
            ack = ""
            win = ""
            options = ""
            length = ""
#La date
            texte=event.split(" ")
            date1=texte[0]
#La source
            texte=event.split(" ")
            source1=texte[2].split(".")
            print(source1)
            if len(source1) == 2:
                source=source1[0]
            if len(source1) == 3:
                source=source1[0]+ "." +source1[1]
            if len(source1) == 4:
                source=source1[0]+ "." +source1[1]+ "." +source1[2] 
            if len(source1) == 5:
                source=source1[0]+ "." +source1[1]+ "." +source1[2]+ "." +source1[3]
            if len(source1) == 6:
                source=source1[0]+ "." +source1[1]+ "." +source1[2]+ "."+source1[3]+"."+source1[4]
            print("source :",source)
            flag2=0
            for item in tab_dest:
                if item == source:
                    flag2=1
            
            if flag2==0:
                tab_dest = np.append(tab_dest,source)
            print("tableau", tab_dest)
#Le port
            if len(texte) > 1: 
                port1=texte[2].split(".")
                port=port1[-1]
#La destination
            texte=event.split(" ")
            source2=texte[4]
#Le Flag
            texte=event.split("[") 
            if len(texte) > 1: 
                flag1=texte[1].split("]")
                flag=flag1[0]
#SEQ
            texte=event.split(",")
            if len(texte) > 1:
                if texte[1].startswith(" seq"):
                    seq1=texte[1].split(" ")
                    seq=seq1[2]
#ACK
            if len(texte) > 2: #
                if texte[2].startswith(" ack"):
                    ack1=texte[2].split(" ")
                    ack=ack1[2]
#Pas de "SEQ"
                if texte[1].startswith(" ack"):
                    ack1=texte[1].split(" ")
                    ack=ack1[2]
                    
            if len(texte) > 3: #si le nombre de partie est supérieur à 3
#Si il y a "ACK"
                if texte[3].startswith(" win"):
                    win1=texte[3].split(" ")
                    win=win1[2]
#Pas de "ACK"
                if texte[2].startswith(" win"): #Si le texte [2] commence par " win"
                    win1=texte[2].split(" ") #on coupe à l'espace et on prend le texte juste après
                    win=win1[2]#On prend le texte après l'espace (la partie qu'on retrouvera dans le tableau
#Options
            texte=event.split("[") #On coupe à partir du crochet
            if len(texte) > 2: #
                options1=texte[2].split("]") #On part du premier "[" et on a texte [2] pour arriver à ce qu'on souhaite récupérer 
                options=options1[0]#0 pour prendre la partie à gauche du deuxième crochet "]"
            
#Length avec option
            texte=event.split("]") 
            if len(texte) > 2: #vérifier le nombre de partie (split au crochet)
                    length1=texte[2].split(" ")
                    length=length1[2]
#Length sans option
            texte=event.split(",")
            if len(texte) > 3:
                if texte[3].startswith(" length"): #Si ça commence par length :recherche 3 dans le texte
                    length1=texte[3].split(" ") #Coupure à l'espace
                    length=length1[2] #On prend 2 pour n'avoir que le nombre
                    length = length.replace(characters,"")#Remplacement du "characters" par "", cela evite que le tableur l'écrive comme une date
            if event.startswith("11:42:55.536521") : #Limite
                prog=0 #Si limite atteinte : arret  de la boucle
            event=date+ ";" +source+ ";" +port+ ";" +source2+ ";" +flag+ ";" +seq+ ";" +ack+ ";" +win+ ";" +options+ ";" +length
            fic.write(event + "\n") #On écrit la variable event dans le csv et on utilise \n poyr ne pas tout écrire sur la meme ligne
print("tableau final", tab_dest)
plt.plot(tab_dest, [1, 7, 2, 11])
plt.show()
fic.close()

fic=open("test.md", "r")
text = fic.read()
html = markdown.markdown(text)
fic2=open("test.html", "w")
fic2.write(html)