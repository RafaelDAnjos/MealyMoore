import sys


def converteMealyparaMoore(arq,nomearqsai):
    lstEstados = []
    lstSimbolos = []
    estadoInit = ""
    lstAlfasai = []
    lstTransicao = []
    print("------------------mealy-------------")
    linha = arq.readline()
    linha = linha.strip()
    lstEstados = linha.split(" ")
    linha = arq.readline()
    linha = linha.strip()
    lstSimbolos = linha.split(" ")
    linha = arq.readline()
    linha = linha.strip()
    estadoInit = linha
    linha = arq.readline()
    linha = linha.strip()
    lstEstadosaida = linha.split(" ")
    linha = arq.readline()
    linha = linha.strip()
    lstAlfasai = linha.split(" ")

    linha = arq.readline()
    while linha!= "":
        linha = linha.strip()
        linha = linha.split()
        lstTransicao.append(linha)
        linha = arq.readline()

    print(lstEstados,'Estados')
    print(lstSimbolos,'simbolos')
    print(estadoInit,'Estado inicial')
    print(lstEstadosaida,"Estadofinal")
    print(lstAlfasai,'Alfabetosaida')
    print(lstTransicao,'Transicao')

#Dividindo os simbolos não terminais:
    lstEstadosMoore  = []
    for i in range(len(lstTransicao)):
        cont = 0
        for transicao in lstTransicao:

            if lstTransicao[i][2] == transicao[2]:
                if lstTransicao[i][3] in lstAlfasai:
                    cont = cont +1
        if estadoInit == lstTransicao[i][2]:
            lstEstadosMoore.append(lstTransicao[i][2])
            lstEstadosMoore.append(lstTransicao[i][2] + "'")
        if cont > 1 and lstTransicao[i][2] not in lstEstadosMoore:
            lstEstadosMoore.append(lstTransicao[i][2])
            lstEstadosMoore.append(lstTransicao[i][2]+"'")
    for transicao in lstTransicao:
        if transicao[2]  not in lstEstadosMoore:
            lstEstadosMoore.append(transicao[2])
    print(lstEstadosMoore, "lstEstadosMoore")





def converteMooreparaMealy(arq,nomearqsai):
    print("----------------moore--------------")
def main(argv):

    nomearqentrada = argv[1]
    nomearqsaida = argv[2]




    arqentrada = open(nomearqentrada,"r")
    linha = arqentrada.readline()
    linha = linha.strip()
    if(linha == "mealy"):

        converteMealyparaMoore(arqentrada,nomearqsaida)

    elif(linha == "moore"):
        converteMooreparaMealy(arqentrada,nomearqsaida)

    return 0

if __name__ == '__main__':
    main(sys.argv)