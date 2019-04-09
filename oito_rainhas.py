import random

# 000 - 0
# 001 - 1
# 010 - 2
# 011 - 3
# 100 - 4
# 101 - 5
# 110 - 6
# 111 - 7


def gera_individuo():

    lista_int = random.sample(range(8),8)

    return lista_int



def gera_populacao():
    populacao = []
    i = 0
    while i < 100:
        lista_int = random.sample(range(8),8)
        if lista_int not in populacao:
            #print(lista_int)
            populacao.append(lista_int)
            i += 1
        else:
            print('repetido')
        
    
    return populacao

def calcula_fitness(ind):
    colisoes = 0
    for i in ind:
        #print('rainha na linha ', i)
        for j in range(len(ind)):
            if ind[j] != i:
                if j in range(ind.index(i)):
                    #print('range ',ind.index(i))
                    dist = ind.index(i) - j
                    #print('distancia ', dist)
                    if ind[j] == (i - dist) or ind[j] == (i + dist):
                        #print('colisão entre a rainha {} na coluna {} e a rainha {} na coluna {}'.format(i, ind.index(i), ind[j], j ))
                        colisoes += 1
                elif j in range(ind.index(i),len(ind)):
                    #print('range ',ind.index(i), len(ind))
                    dist = j - ind.index(i)                    
                    if ind[j] == (i + dist) or ind[j] == (i - dist):
                       #print('colisão entre a rainha {} na coluna {} e a rainha {} na coluna {}'.format(i, ind.index(i), ind[j], j ))
                        colisoes += 1
       
    colisoes = int(colisoes/2)
    fitness = 28 - colisoes #28 é o número total de colisões possíveis(C(8,2))
    return fitness

def roleta(fit):
    fatias = list(map(lambda x: int(round(x / sum(fit),2) *100), fit)) 
    roleta = round(random.random(),2) * 100
    escolhido = 0
    i = 1
    while i< len(fatias):
        fatias[i] = fatias[i-1]+fatias[i]
        #print(fatias[i])
        i += 1

    x = 0
    i = 0
    while i < len(fatias):
        if roleta in range(x,fatias[i]):
           
            escolhido = i
            i = len(fatias)            
        else:
            x = fatias[i]
            i += 1

    return escolhido


def seleciona_pais(populacao):
    rand = random.sample(populacao,10)     
    fit = list(map(calcula_fitness, rand))         
    if 0 in fit:
        for i in fit:
            if i==0:
                i += 1

    index = roleta(fit)
    fit.pop(index)
    
    pai_x = rand[index]
    rand.pop(index)
    index = roleta(fit)
    pai_y = rand[index]       
    

    return pai_x, pai_y


def crossover(pai_x, pai_y):  
    filho_x = []
    filho_y = []
    pc = random.randrange(0,10)    
    if pc in range(0,9):
        l = list(range(0,8))
        ponto1 = random.sample(l,1)[0]
        l.remove(ponto1)
        ponto2 = random.sample(l,1)[0]
        
        #print(pai_x,pai_y,ponto1,ponto2)
        filho_x = crossoverX(pai_x, pai_y, ponto1,ponto2)
        filho_y = crossoverX(pai_y,pai_x,ponto1,ponto2)
           
    else:
        print('filhos iguais aos pais')
        filho_x = pai_x
        filho_y = pai_y

    return filho_x,filho_y


def crossoverX(pai_x, pai_y, ponto1, ponto2):
    ponto1 = min(ponto1,ponto2)
    ponto2 = max(ponto1,ponto2)
    temp = ponto1

    filho = pai_x[:ponto1] + pai_y[ponto1:ponto2] + pai_x[ponto2:]    
    
    while ponto1 < ponto2:
        for i in range(0,8):
            if i not in range(ponto1,ponto2):
                if filho[i] == pai_y[ponto1]:
                    filho[i] = pai_x[ponto1]                    
                    
        ponto1 += 1
        if ponto1 == ponto2 and len(set(filho)) != 8:
            ponto1 = temp        
           
    
    return filho              

        

def mutacao(individuo):

    pm = random.randrange(0,10)

    if pm in range(0,6):
        geneX = random.randrange(0,7)
        geneY = random.randrange(0,7)

        temp = individuo[geneX]
        individuo[geneX] = individuo[geneY]
        individuo[geneY] = temp   
   
    
    
    return individuo


def gera_solucao():
    solucao = [0,0,0,0,0,0,0,0]
    iteracao = 0
    pop = gera_populacao()
    while iteracao < 10000:
        print(iteracao)
        for i in pop:
            if calcula_fitness(i) == 28:
                solucao = i
                return 'Solucao {} encontrada na populacao inicial'.format(solucao)
        
        paiX, paiY = seleciona_pais(pop)        
        filhoX, filhoY = crossover(paiX, paiY)

        #seleção de sobreviventes geracional
        pop.remove(paiX)
        pop.remove(paiY)

        

        if calcula_fitness(filhoX) == 28:
            solucao = filhoX
            
            print('Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao))
            #return 'Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao)

        elif calcula_fitness(filhoY) == 28:
            solucao = filhoY
           
            print('Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao))
            #return 'Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao)

        filhoX = mutacao(filhoX)
        filhoY = mutacao(filhoY)

        
        pop.append(filhoX)
        pop.append(filhoY)

        print(filhoX, calcula_fitness(filhoX))
        print(filhoY, calcula_fitness(filhoY))
      
        if calcula_fitness(filhoX) == 28:
            solucao = filhoY
            return 'Solução {} encontrada após mutação na iteração {}'.format(solucao, iteracao)
            
        elif calcula_fitness(filhoY) == 28:
            solucao = filhoY
            return 'Solução {} encontrada após mutação na iteração {}'.format(solucao, iteracao)
        
        iteracao += 1           

        

    return 'Solução não encontrada'





        
    

            

    



