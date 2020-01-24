def z_critico(pathTabela, nivelDeConfianca):
    
    #transformando a tabela em lista para uso dos dados
    tabelaDistribuicaoNormal = open(pathTabela, 'r').read()
    aux = tabelaDistribuicaoNormal.split("\n")
    listaDistribuicaoNormal = []
    for elemento in aux:
        listaDistribuicaoNormal.append(elemento.split())

    #definindo o valor de Z Critico com base na tabela
    zCritico = 0.0
    for i in range(len(listaDistribuicaoNormal)):
       for j in range(len(listaDistribuicaoNormal[i])):
          
           if float(listaDistribuicaoNormal[i][j]) == nivelDeConfianca:
               
                zCritico = float(listaDistribuicaoNormal[i][0]) + float(listaDistribuicaoNormal[0][j]) 
                return zCritico

def erro_padrao(desvioPadrao, tamanhoAmostra):

    tamanhoAmostra = tamanhoAmostra ** float((1/2))
    return desvioPadrao/tamanhoAmostra

def intervalo_de_confianca(tamanhoAmostra, media, desvioPadrao, nivelDeConfianca, pathTabelaZ):
    
    nivelDeConfianca = (nivelDeConfianca / 100) / 2
    zCritico = z_critico(pathTabelaZ, nivelDeConfianca)
    while zCritico == None:
        nivelDeConfianca += 0.0001
        zCritico = z_critico(pathTabelaZ, round(nivelDeConfianca, 4))

    erroPadrao = erro_padrao(desvioPadrao, tamanhoAmostra)
    margemDeErro = zCritico * erroPadrao

    limiteInferior = media - margemDeErro
    limiteSuperior = media + margemDeErro
    return limiteInferior, limiteSuperior