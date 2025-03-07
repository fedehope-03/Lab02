import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()



    txtIn = input("Inserire il numero della funzione che si vuole azionare ")

    if txtIn.isdigit() :

        if int(txtIn) == 1:
            t.stampaDizio()


        if int(txtIn) == 2:
            new = input("inserire prima la parola Aliena e poi le traduzioni ")
            parola = new.split(" ")
            #parola[len(parola)-1]+="\n"
            tupla = (parola[0],parola[1:])
            t.handleAdd(tupla)


        if int(txtIn) == 3:
            cercare = input("inserire la parola aliena da tradurre ")
            if cercare.isalpha():
                t.handleTranslate(cercare)

            else: print("Errore nell'input")

        if int(txtIn) == 4:
            cercare = input("inserire la parola aliena da tradurre ")
            cont=0
            for lettera in cercare:
                if lettera == "?":
                    cont+=1
            if cercare.isascii() and cont==1: # non so come controllare altrimenti
                t.handleWildCard(cercare)
            else: print("Errore nell'input")

        if int(txtIn) == 5:
            t.copiaDizionario("dictionary.txt")
            break