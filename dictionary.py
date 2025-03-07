class Dictionary:
    def __init__(self):
        self.dizio= None


    def aggiorna(self,dizio):
        self.dizio=dizio


    def addWord(self,chiave,lista):
        self.dizio[chiave]= lista

    def __str__(self):
        out=""
        for chiave,valore in self.dizio.items():
            out+= chiave+" "
            for i in valore:
                out+= i
                out+=" "
            out+="\n"
        return out


    def aggiungiParola(self,chiave,lista):
        for i in lista:
            self.dizio[chiave].append(i)
        

    def translate(self,parola):
        out=""
        for i in self.dizio[parola]:
            out+= i +" "

        return out


    def translateWordWildCard(self,parola):
        out=""
        lista1=[]
        for lettera in parola:
            lista1.append(lettera)
        for i in self.dizio:
            listaP=[]
            for lettera in i:
                listaP.append(lettera)
            if len(lista1) == len(listaP):
                flag=True
                for c in range(0,len(lista1)):
                    if lista1[c]!=listaP[c] and lista1[c]!= "?":
                        flag=False

                if flag:
                    for t in self.dizio[i]:
                        out+= t+" "

        return out

    def scrivi(self,nome):
        infile = open(nome,"w")
        for chiave,valori in self.dizio.items():
            out="\n"+chiave
            for i in valori:
                out+=" "+i

            infile.writelines(out) #da chiedere se si devo per forza mettere "\n"

        infile.close()






