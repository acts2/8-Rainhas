
import random

def int_to_bin(int_list):
    bin_str = ''
    for i in int_list:
        if i in range(2):
            bin_str += ''.join('00'+bin(i)[2:])
        elif i in range(2,4):
            bin_str += ''.join('0'+bin(i)[2:])
        else:
            bin_str += ''.join(bin(i)[2:])
    return bin_str

def bin_to_int(bin_str):
    int_list = []
    i = 1
    while i<23:
        int_list.append(int(bin_str[(i-1):(2+i)],2))
        i += 3
    
    return int_list 


def gera_individuo():
    individuo = ''
    for i in range(24):
        individuo += str(random.sample([0,1],1)[0])
    
    return individuo


def gera_populacao():
    populacao = []
    i = 0
    while i < 100:
        individuo = gera_individuo()
        if individuo not in populacao:
            populacao.append(individuo)
            i += 1
        else:
            print('repetido')
    
    return populacao

def calcula_fitness(individuo):
    ind = bin_to_int(individuo)
    colisoes = 0
    for i in ind:
        colisoes += (ind.count(i) - 1)
       
        for j in range(len(ind)):
            if ind.index(ind[j]) != ind.index(i): #se não é o mesmo índice               
                if j in range(ind.index(i)):                    
                    dist = ind.index(i) - j                   
                    if ind[j] == (i - dist) or ind[j] == (i + dist):
                        #print('colisão entre a rainha {} na coluna {} e a rainha {} na coluna {}'.format(i, ind.index(i), ind[j], j ))
                        colisoes += 1
                elif j in range(ind.index(i),len(ind)):                    
                    dist = j - ind.index(i)                    
                    if ind[j] == (i + dist) or ind[j] == (i - dist):
                       #print('colisão entre a rainha {} na coluna {} e a rainha {} na coluna {}'.format(i, ind.index(i), ind[j], j ))
                        colisoes += 1
       
    colisoes = int(colisoes/2)
    fitness = 28 - colisoes #28 é o número total de colisões possíveis(C(8,2))
    return fitness

def seleciona_pais(populacao):
    rand = random.sample(populacao,5)
    
    fit = []
    pai_x = ''
    pai_y = ''
    for i in rand:
        fit.append(calcula_fitness(i))
    
    
    pai_x = rand.pop(fit.index(max(fit)))
    fit.pop(fit.index(max(fit)))
    pai_y = rand.pop(fit.index(max(fit)))

    return pai_x, pai_y

def sel_sobreviventes(populacao):
    if len(populacao) != 100:
        return 'populacao diferente de 100'
    populacao.pop(populacao.index(min(populacao)))
    populacao.pop(populacao.index(min(populacao)))

    return populacao

def crossover(pai_x, pai_y):  
    filho_x = ''
    filho_y = ''
    pc = random.randrange(0,10)

    if pc in range(0,9):
        ponto = random.randrange(0,23)
        
        filho_x = pai_x[0:ponto] + pai_y[ponto:24]
        filho_y = pai_y[0:ponto] + pai_x[ponto:24]
           
    else:
        print('filhos iguais aos pais')
        filho_x = pai_x
        filho_y = pai_y

    return filho_x,filho_y


def mutacao(individuo):

    
    for i in range(24):        
        pm = random.randrange(0,10)    
        if pm in range(0,4):
            if individuo[i] == '1':
                temp = list(individuo)
                temp[i] = '0'
                individuo = ''.join(temp)
            else:
                temp = list(individuo)
                temp[i] = '1'
                individuo = ''.join(temp)
    
    return individuo

def gera_solucao():
    solucao = '000000000000000000000000'
    iteracao = 0
    pop = gera_populacao()
    while iteracao < 10000:
        
        print(iteracao)
        for i in pop:
            if calcula_fitness(i) == 28:
                solucao = i
                return 'Solucao {} encontrada na populacao na iteração {}'.format(solucao, iteracao)
        paiX, paiY = seleciona_pais(pop)           
        filhoX, filhoY = crossover(paiX, paiY)
        
                
        if calcula_fitness(filhoX) == 28:
            solucao = filhoX
            return 'Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao)
            
        elif calcula_fitness(filhoY) == 28:
            solucao = filhoY
            return 'Solução {} encontrada após crossover na iteração {}'.format(solucao, iteracao)
        
        filhoX = mutacao(filhoX)
        filhoY = mutacao(filhoY)
        print(filhoX, calcula_fitness(filhoX))
        print(filhoY, calcula_fitness(filhoY))
      
        if calcula_fitness(filhoX) == 28:
            solucao = filhoX
            return 'Solução {} encontrada após mutação na iteração {}'.format(solucao, iteracao)
            
        elif calcula_fitness(filhoY) == 28:
            solucao = filhoY
            return 'Solução {} encontrada após mutação na iteração {}'.format(solucao, iteracao) 

        pop = sel_sobreviventes(pop)
        pop.append(filhoX)
        pop.append(filhoY)

       

        iteracao += 1
                    

    return 'Solução não encontrada'





        
