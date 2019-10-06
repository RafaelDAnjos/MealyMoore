import sys

def procuraLista(lst,elem):
    for i in range(len(lst)):
        if(lst[i] == elem):
            return 1
    return 0

def montaEstadosMoore(estadosNormal,estadosMultSimbolos):

    estadosMoore = []

    for i in range (len(estadosNormal)):

        estadosMoore.append(estadosNormal[i])

        for j in range (len(estadosMultSimbolos)):
            
            if(estadosMultSimbolos[j][0] == estadosNormal[i]):
                
                tam = len(estadosMultSimbolos[j][1])
                stringAUX = estadosMultSimbolos[j][0]
            
                for i in range (tam-1):
                    stringAUX += "'"
                    estadosMoore.append(stringAUX)

 
    return estadosMoore

def montaEstadosEndMoore(estadosNormal,estadosMultSimbolos,estadosFinais):

    estadosFinaisMoore = []

    for i in range (len(estadosFinais)):

        estadosFinaisMoore.append(estadosFinais[i])

        for j in range (len(estadosMultSimbolos)):
            
            if(estadosMultSimbolos[j][0] == estadosFinais[i]):
                
                tam = len(estadosMultSimbolos[j][1])
                stringAUX = estadosMultSimbolos[j][0]
            
                for i in range (tam-1):
                    stringAUX += "'"
                    estadosFinaisMoore.append(stringAUX)

 
    return estadosFinaisMoore

def montaTransicoesMoore(estadosMoore,transicoes,estadosMealy):


    transicoesMoore = []
    lstNos = []
    no = ["q0", None]
    lstNos.append(no)

    for i in range(len(estadosMoore)):

        no = [estadosMoore[i], None]

        for j in range(len(transicoes)):

            if (transicoes[j][2] == no[0]):

                if no[0] == "q0":
                    no[0] = "q0'"
                    no[1] = transicoes[j][3]
                    lstNos.append(no)
                else:
                    if no[1] == None:

                        no[1] = transicoes[j][3]
                        lstNos.append(no)
                    else:

                        no = [estadosMoore[i + 1], transicoes[j][3]]
                        lstNos.append(no)

    print(lstNos)
    # print(transicoes)

    noMoore = [None, None, None]
    estadoAlternativo = ""
    for i in range(len(estadosMealy)):
        estadoAlternativo = estadosMealy[i]+"'"
        if estadoAlternativo in estadosMoore:
            for j in range (len(transicoes)):
                if transicoes[j][0] == estadosMealy[i]:
                    noaux1 =  [transicoes[j][2],transicoes[j][3]]
                    noaux2 =  [transicoes[j][2]+"'",transicoes[j][3]]
                    if noaux1 in lstNos:
                        noMoore = [transicoes[j][0],transicoes[j][1],noaux1[0]]
                        transicoesMoore.append(noMoore)
                        noMoore = [transicoes[j][0]+"'",transicoes[j][1],noaux1[0]]
                        transicoesMoore.append(noMoore)
                    if noaux2 in lstNos:
                        noMoore = [transicoes[j][0],transicoes[j][1],noaux2[0]]
                        transicoesMoore.append(noMoore)
                        noMoore = [transicoes[j][0]+"'",transicoes[j][1],noaux2[0]]
                        transicoesMoore.append(noMoore)
        else:
            for j in range (len(transicoes)):
                if transicoes[j][0] == estadosMealy[i]:
                    noaux1 =  [transicoes[j][2],transicoes[j][3]]
                    noaux2 =  [transicoes[j][2]+"'",transicoes[j][3]]
                    if noaux1 in lstNos:
                        noMoore = [transicoes[j][0],transicoes[j][1],noaux1[0]]
                        transicoesMoore.append(noMoore)
                    if noaux2 in lstNos:
                        noMoore = [transicoes[j][0],transicoes[j][1],noaux2[0]]
                        transicoesMoore.append(noMoore)



    for transicao in transicoesMoore:
        print(transicao)

    return transicoesMoore











def montaMoore(estadosNormal,estadosMultSimbolos,transicoes,simbolos,estadoInic,estadosFinais,alfabetoSaida):

    print("=========== Conversão: Mealy para Moore ============")

    estadosMoore = montaEstadosMoore(estadosNormal,estadosMultSimbolos);

    print("Estados Moore: ",estadosMoore)

    estadosFinaisMoore = montaEstadosEndMoore(estadosNormal,estadosMultSimbolos,estadosFinais)
    
    print("Estados end Moore",estadosFinaisMoore)

    simbolosMoore = simbolos;

    print("Simbolos Moore: ",simbolosMoore)

    alfabetoSaidaMoore = alfabetoSaida;

    print("Alfabeto saida Moore: ",alfabetoSaidaMoore);

    print("Transições: ",transicoes)
    print("-------------------------------------------------")
    
    transicoesMoore = montaTransicoesMoore(estadosMoore,transicoes,estadosNormal)

    #definicaoSaida = montaDefinicaoSaida()


def multSimboloEstado(lstEstados,lstTransicao,lstSimbolos):
    
    quantTransic    = len(lstTransicao) # Quantidade de Transicoes;
    quantEstados    = len(lstEstados)   # Quantidade de Estados;
    simbolos        = []                # Simbolos encontrados na transicao para um estado;
    estadosMult     = []                # Estados com mais de um simbolo
    pack            = []                # Pacote auxiliar
    megaPack        = []                # Pacote com estados finais com mais de um simbolo na transicao;

    #Passa por todos estados
    for i in range (quantEstados):
        quant = 0

        #Passa por todas as transicoes
        for j in range (quantTransic):

            # Se <estadoAtual> == <estadoFinalDaTransicao>
            if lstEstados[i] == lstTransicao[j][2]:
                
                # Procura se esse simbolo da trasicao já foi usado por outra transicao
                # 0 = False
                if lstEstados[i] == "q0":
                    if (procuraLista(simbolos,lstTransicao[j][3]) == 0):

                        estado = lstTransicao[j][2]         # Pega o estado atual
                        quant = 2                         # Um transicao com simbolo novo
                        simbolos.append(None) # Adciona esse simbolo na lista de simbolos
                        simbolos.append(lstTransicao[j][3]) # Adciona esse simbolo na lista de simbolos
                else:
                    if (procuraLista(simbolos,lstTransicao[j][3]) == 0):

                        estado = lstTransicao[j][2]         # Pega o estado atual
                        quant +=1                           # Um transicao com simbolo novo
                        simbolos.append(lstTransicao[j][3]) # Adciona esse simbolo na lista de simbolos


        if quant >= 2 :
                
            pack.append(estado)     # Adciona o estado atual
            pack.append(simbolos)   # Os simbolos que esse estado recebe
            megaPack.append(pack)   
        
        pack = []       
        quant = 0
        simbolos = []
     
    return megaPack
    

def converteMealyparaMoore(arq,nomearqsai):

    estadoInit      = None
    lstEstados      = []
    lstSimbolos     = []
    lstAlfasai      = []
    lstTransicao    = []
    
    print("========= Mealy =============")

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

    print('Estados:',lstEstados,)
    #print('Simbolos: ',lstSimbolos)
    #print('Estado inicial: ',estadoInit)
    #print('Estadofinal: ',lstEstadosaida)
    #print('Alfabetosaida: ',lstAlfasai,)
    #print('Transicao: ',lstTransicao)

    estadosMultSimbolos = multSimboloEstado(lstEstados,lstTransicao,len(lstSimbolos))

    print("MegaPack: ",estadosMultSimbolos)

    montaMoore(lstEstados,estadosMultSimbolos,lstTransicao,lstSimbolos,estadoInit,lstEstadosaida,lstAlfasai)








    # Dividindo os simbolos não terminais:
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
    
    #print(lstEstadosMoore, "lstEstadosMoore")





def converteMooreparaMealy(arq,nomearqsai):
    print("----------------moore--------------")
    lstestadosMoore = []
    alfabetoEntrada = []
    estadoInicial = ""
    estadosFinais = []
    alfabetoSaida = []
    transicoes = []
    marca = "-----"
    lstNos = []

    linha = arq.readline()
    linha =linha.strip()
    lstestadosMoore = linha.split(" ")
    print("Estados Moore: ", lstestadosMoore)

    linha = arq.readline()
    linha = linha.strip()
    alfabetoEntrada = linha.split(" ")
    print("Alfabeto Entrada: ", alfabetoEntrada)

    linha = arq.readline()
    linha = linha.strip()
    estadoInicial = linha
    print("Estado Inicial: ", estadoInicial)

    linha = arq.readline()
    linha = linha.strip()
    estadosFinais = linha.split(" ")
    print("Estados Finais: ", estadosFinais)


    linha = arq.readline()
    linha = linha.strip()
    alfabetoSaida = linha.split(" ")
    print("Alfabeto Saida: ", alfabetoSaida)

    linha = arq.readline()
    linha = linha.strip()

    while linha != marca:
        linha = linha.strip()
        linha = linha.split(" ")
        transicoes.append(linha)
        linha = arq.readline()
        linha = linha.strip()
    print("Transições: ", transicoes)

    linha = arq.readline()
    while linha != "":
        linha = linha.strip()
        linha = linha.split(" ")
        lstNos.append(linha)
        linha = arq.readline()






    print("Nos: ",lstNos)






def main(argv):

    nomearqentrada = "entrada2.txt"
    nomearqsaida = "saida.txt"




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