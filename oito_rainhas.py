import random

# 000 - 0
# 001 - 1
# 010 - 2
# 011 - 3
# 100 - 4
# 101 - 5
# 110 - 6
# 111 - 7

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


def gera_populacao():
    populacao = []
    i = 0
    while i < 100:
        lista_int = random.sample(range(8),8)
        if lista_int not in populacao:
            #print(lista_int)
            populacao.append(int_to_bin(lista_int))
            i += 1
        else:
            print('repetido')
    
    return populacao

def calcula_fitness(individuo):
    ind = bin_to_int(individuo)
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

def seleciona_pais(populacao):
    rand = random.sample(populacao,5)
    print(rand)
    fit = []
    pai_x = ''
    pai_y = ''
    for i in rand:
        fit.append(calcula_fitness(i))
    
    print(fit)
    pai_x = rand.pop(fit.index(max(fit)))
    fit.pop(fit.index(max(fit)))
    pai_y = rand.pop(fit.index(max(fit)))

    return pai_x, pai_y

def sel_sobreviventes(populacao):
    if len(populacao) != 102:
        return 'populacao menor que 102'
    populacao.pop(populacao.index(min(populacao)))
    populacao.pop(populacao.index(min(populacao)))

    return populacao

        


#def crossover()
#def mutacao()
    

            

    



