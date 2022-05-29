import numpy as np
import pandas as pd
from math import log2

data = pd.read_csv('data/golf.csv')

#print(data)


class Node:

    def __init__(self, label):
        self.label = label
        self.branches = []

    def addBranches(self, child):
        self.branches.append(child)

    def getLabel(self):
        return self.label

    def printTree(self):
        print(self.label)
        for b in self.branches:
            print("L'attribut " + b[0] + " a pour fils : " + b[1].getLabel())
            b[1].printTree()



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

def informationGain(feature, label):
    totalRow = data[label].size
    classes = allValuesAttrib(data, feature)
    L = data[feature].tolist()
    res = 0
    for l in classes:
        p = L.count(l)/totalRow
        res += p*entropy(data[data[feature] == l], "play")
    return res

    
wholeEntropy = entropy(data, "play")


def ID3(exemples, attributCible, attributsNonCibles):
    if(exemples.empty): #S'il n'y a pas d'exemples, alors il y a une erreur
        return Node("ERREUR, EXEMPLE VIDE")
    elif(attributsNonCibles == []): #Si il n'y a aucun attribut non cibles, alors notre arbre sera seulement 
                                    #un noeud ettiqueté avec la classe la plus fréquente
        return Node("Valeur la plus fréquente pour l'attribut cible")
    elif(isAllEqual(exemples[[attributCible]])): # S'il y a qu'une seule classe, alors on a un arbre feuille
        return Node(exemples[[attributCible]].values[0])
    else:
        attributSelectionne = "a" # On selectionne le "meilleur" attribut
        max = 0
        for attrib in attributsNonCibles:
            I = wholeEntropy - informationGain(attrib, attributCible)
            if I > max:
                max = I
                attributSelectionne = attrib

        attributsNonCibles.remove(attributSelectionne) # On le retire de la liste
        newNode = Node(attributSelectionne)

        for v in allValuesAttrib(exemples, attributSelectionne):
            filteredExamples = exemples[exemples[attributSelectionne] == v]
            nextNode = ID3(filteredExamples, attributCible, attributsNonCibles)
            newNode.addBranches([str(v), nextNode])

        return newNode

ID3(data, "play", ["outlook", "temp", "humidity", "wind"]).printTree()
