import numpy as np
import pandas as pd
from math import log2

data = pd.read_csv('data/golf.csv')

#print(data)




class Node:
    label = ""
    branches = []
    
    def __init__(self, label):
        self.label = label

    def addBranches(self, child):
        self.branches.append(child)


def isAllEqual(df):
    element = df.values[0]
    for i in range(df.size):
        if(df.values[i] != element):
            return False
    return True


def allValuesAttrib(df, attribut):
    res = []
    for i in range(df[attribut].size):
        v = df[attribut].values[i]
        if not (v in res):
            res.append(v)

    return res

def entropy(df, label):
    totalRow = df[label].size
    L = df[label].tolist()
    classes = allValuesAttrib(df, label)
    res = 0
    for l in classes:
        p = L.count(l)/totalRow
        res -= p*log2(p)
    return res

def informationGain(df, label):
    totalRow = df[label].size
    classes = allValuesAttrib(df, label)
    L = df[label].tolist()
    res = 0
    for l in classes:
        p = L.count(l)/totalRow
        res += p*entropy(df[df[label] == l], "play")
    return res

    
wholeEntropy = entropy(data, "play")
outlookIG = informationGain(data, "outlook")
I = wholeEntropy - outlookIG
print(I)


def ID3(exemples, attributCible, attributsNonCibles):
    if(exemples.empty): #S'il n'y a pas d'exemples, alors il y a une erreur
        return Node("ERREUR, EXEMPLE VIDE")
    elif(attributsNonCibles == []): #Si il n'y a aucun attribut non cibles, alors notre arbre sera seulement 
                                    #un noeud ettiqueté avec la classe la plus fréquente
        return Node("Valeur la plus fréquente pour l'attribut cible")
    elif(isAllEqual(data[[attributCible]])): # S'il y a qu'une seule classe, alors on a un arbre feuille
        return Node(data[[attributCible]].values[0])
    else:
       attributSelectionne = "a" # On selectionne le "meilleur" attribut
       attributsNonCibles.remove(attributSelectionne) # On le retire de la liste
       newNode = Node(attributSelectionne)
       

       for v in allValuesAttrib(exemples, attributSelectionne):
            filteredExamples = exemples[exemples[attributSelectionne] == v]
            nextNode = ID3(filteredExamples, attributCible, attributsNonCibles)
            print([v, nextNode])
            newNode.addBranches([v, nextNode])
       
       return newNode

#ID3(data, "play", ["outlook", "temp", "humidity", "wind"])
a = data[data["outlook"] == "overcast"]
print(isAllEqual(a[["outlook"]]))
    

