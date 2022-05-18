import numpy as np
import pandas as pd

data = pd.read_csv('data/golf.csv')

print(data)

class Node:
    label = ""
    children = []
    
    def __init__(self, label):
        self.label = label


def isAllEqual(values):
    element = values[0]
    for v in values:
        if(v != element):
            return False
    return True



def ID3(exemples, attributCible, attributsNonCibles):
    if(exemples == []): #S'il n'y a pas d'exemples, alors il y a une erreur
        return Node("ERREUR, EXEMPLE VIDE")
    elif(attributsNonCibles == []): #Si il n'y a aucun attribut non cibles, alors notre arbre sera seulement 
                                    #un noeud ettiqueté avec la classe la plus fréquente
        return Node("Valeur la plus fréquente pour l'attribut cible")
    elif(isAllEqual(attributCible)): # S'il y a qu'une seule classe, alors on a un arbre feuille
        return Node(attributCible[0])
    else:
        attributSelectionne = "Mdrr va te faire foutre"
        attributsNonCiblesRestants 
        
    

