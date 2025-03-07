import dictionary
from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.d=Dictionary()


    def printMenu(self):

        print("-------------------------------")
        print("Traduttore Alieno-Italiano")
        print("-------------------------------")
        print(" 1. Stampa tutto il dizionario")
        print(" 2. Inserire una nuova traduzione")
        print(" 3. Cercare una traduzione")
        print(" 4. Cercare con wildcard")
        print(" 5. Exit")




    def loadDictionary(self, dict):

        infile = open(dict, "r")
        dizio={}

        for line in infile:
        # print(line)
            if line[len(line)-1]=="\n":
                line=line[:len(line)-1]
            linea = line.split(" ")
            dizio[linea[0]]=linea[1:]
            self.d.aggiorna(dizio)
        infile.close()

    def stampaDizio(self):
        print(self.d.__str__())

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        flag=True
        if entry[0].isalpha():
            for i in entry[1]:
                if i.isalpha():
                    pass
                else: flag=False
        else :flag=False

        if flag:
            if entry[0] in self.d.dizio:
                self.d.aggiungiParola(entry[0],entry[1])
            else:
                self.d.addWord(entry[0],entry[1])
        else: print("Errore nell'input")


    def handleTranslate(self, query):
        # query is a string <parola_aliena>

        print(self.d.translate(query))


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        print(self.d.translateWordWildCard(query))

    def copiaDizionario(self,nome):
        self.d.scrivi(nome)