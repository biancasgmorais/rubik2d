#esse algoritmo gera uma estado inicial a partir do objetivo, fazendo operações sorteadas sobre ele. 
#Além de preencher uma estrutura nó como as informações de descrevem o estado, por meio da função "expande".

import random

queue = [] #fila
reg = [] #registra estados ja visitados
aux = []
passos = []#vetor com movimentos sorteados para embaralhar
si = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4] #Estado Objetivo
s = []
contador = 0
#numero de movimentos para embaralhar
#movimentos = int(input('Insira a quantidade de movimentos para embaralhar: '))
print('\nInsira qual a heuristica que vc deseja usar: \n[1] NÚMERO DE PEÇAS FORA DO LUGAR \n[2] REGRA DA VIZINHANÇA \n[3] NÚMERO DE PEÇAS DIFERENTES SOMADO')
h = int(input('A Heuristica escolhida: '))
#nesse caso o custo é a quantidade de movimentos executados até chegar ao estado objetivo
c = 0 
heu = 0
#Variáveis das heuristicas
h1=0 #número de peças fora do lugar
h2=0 #regra da vizinhança
h3=0 #número de peças diferentes

#Estrutura
class Node:
    def __init__(self, estado, custo, heuristica, parent):
        self.estado = estado
        self.custo = custo
        self.heuristica = heuristica
        self.parent = parent

def cria_estrutura():
    global c
    global heu
    return Node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4], c, heu, None)

def initial_state():
    global passos
    s = cria_estrutura()
    '''for i in range(len(passos)):
        s = acoes2(passos[i], s)'''
    s.estado = [3, 1, 1, 1, 2, 3, 2, 3, 4, 2, 4, 4]
    s.custo = 0
    s.heuristica = 0

    return s

def enqueue(s):  #Insere filhos na fila
    global queue
    queue.append(s)

def empty_queue():#Verifica se a fila está vazia
    if len(queue) == 0:
        return True
    return False

def dequeue():  #Retira filhos da fila
    global queue
    queue.sort(key=lambda s: s.heuristica)
    return queue.pop(0)

def copia(s): #copia uma estrutura para outra
    novo = cria_estrutura()
    for i in range(len(s.estado)):
        novo.estado[i] = s.estado[i]
    novo.custo = s.custo
    novo.heuristica = s.heuristica
    return novo

# essa função gera uma sequencia de movimentos que vão embaralha
'''def sequencia():
    global movimentos
    global passos
    print('\nEMBARALHAMENTO RANDOMICO FEITO %d VEZES' % movimentos)
    for i in range(movimentos):
        passos.append(random.randint(1, 8))
        if passos[i] == 1:
            print('ROTAÇÃO HORÁRIA')
        elif passos[i] == 2:
            print('ROTAÇÃO ANTI-HORÁRIA')
        elif passos[i] == 3:
            print('TRANSLAÇÃO LINHA 2')
        elif passos[i] == 4:
            print('TRANSLAÇÃO LINHA 3')
        elif passos[i] == 5:
            print('TRANSLAÇÃO LINHA 4')
        elif passos[i] == 6:
            print('TRANSLAÇÃO COLUNA 2')
        elif passos[i] == 7:
            print('TRANSLAÇÃO COLUNA 3')
        elif passos[i] == 8:
            print('TRANSLAÇÃO COLUNA 4')
            
    return passos'''

# inicio do bloco de funções para modificação

def rotHoraria(s): #Rotação horaria
    count = 0
    s1 = copia(s)
    s1.estado = []
    s1.estado.append(s.estado[11])
    while count <= 10:
        s1.estado.append(s.estado[count])
        count += 1
    return s1

def rotAntiHoraria(s): #Rotação anti-horária
    count = 1
    s1 = copia(s)
    s1.estado = []
    while count <= 11:
        s1.estado.append(s.estado[count])
        count += 1
    s1.estado.append(s.estado[0])
    return s1

def transL2(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[11]
    s1.estado[11] = s1.estado[3]
    s1.estado[3] = aux1
    return s1

def transL3(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[10]
    s1.estado[10] = s1.estado[4]
    s1.estado[4] = aux1
    return s1

def transL4(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[9]
    s1.estado[9] = s1.estado[5]
    s1.estado[5] = aux1
    return s1

def transC2(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[0]
    s1.estado[0] = s1.estado[8]
    s1.estado[8] = aux1
    return s1

def transC3(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[1]
    s1.estado[1] = s1.estado[7]
    s1.estado[7] = aux1
    return s1

def transC4(s):
    global aux1
    s1 = copia(s)
    aux1 = s1.estado[2]
    s1.estado[2] = s1.estado[6]
    s1.estado[6] = aux1
    return s1

# fim do bloco de funções para modificação

def iguais(reg, s):
    for i in range(len(reg)):
        if reg[i] != s[i]:
            return False
    return True

def ja_expandido(s):
    global reg

    for i in range(len(reg)):
        if iguais(reg[i], s):
            return True
    return False

def expande(s): #expande
    global reg
    global h1
    global h2
    global h3
    global h
    global passos
    global contador

    contador = contador + 1

    list = []

    for i in range(8):
        s1 = acoes2(i + 1, s)
        if not ja_expandido(s1.estado):
            if h == 1:
                h1 = heuristica1(s1, h1)
                s1.heuristica = h1
            if h == 2:
                h2 = heuristica2(s1, h2)
                s1.heuristica = h2
            if h == 3:
                h3 = heuristica2(s1, h3)
                s1.heuristica = h3
            list.append(s1) 
        

    return list
    
def exibe2 (s):# essa função exibe um estado

    print('  -%d  %d  %d-' % (s.estado[0], s.estado[1], s.estado[2]))
    print('%d           %d ' % (s.estado[11], s.estado[3]))
    print('%d           %d ' % (s.estado[10], s.estado[4]))
    print('%d           %d ' % (s.estado[9], s.estado[5]))
    print('  -%d  %d  %d-' % (s.estado[8], s.estado[7], s.estado[6]))
    print('\nCusto = %d' % s.custo)
    print('Heuristica = %d' % s.heuristica)

def acoes2(acao, s):#Executa ação por ação
    parent = s
    if acao == 1:
     s = rotHoraria(s)
     s.custo = s.custo+1
    elif acao == 2:
     s = rotAntiHoraria(s)
     s.custo = s.custo+1
    elif acao == 3:
     s = transL2(s)
     s.custo = s.custo+1
    elif acao == 4:
     s = transL3(s)
     s.custo = s.custo+1
    elif acao == 5:
     s = transL4(s)
     s.custo = s.custo+1
    elif acao == 6:
     s = transC2(s)
     s.custo = s.custo+1
    elif acao == 7:
     s = transC3(s)
     s.custo = s.custo+1
    elif acao == 8:
     s = transC4(s)
     s.custo = s.custo+1

    s.parent = parent
    return s

# Peças fora do lugar
def heuristica1( s, h1):
    h1 = 0
    i = 0
    si = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    for i in range(len(si)):

        if si[i] != s.estado[i]:

            h1 = h1+1

    return h1

# Regra da Vizinhança
def heuristica2(s, h2):
    h2 = 0
    i = 0
    vets = []
    vets.append(s.estado[11])
    for i in range(len(s.estado)):
        vets.append(s.estado[i])

    vets.append(s.estado[0])
    i = 1
    for i in range(13):

            if vets[i] == 1:
                if (vets[i + 1] == 3):
                    h2 = h2 + 1
                if (vets[i - 1] == 3):
                    h2 = h2 + 1
            elif vets[i] == 2:
                if (vets[i + 1] == 4):
                    h2 = h2 + 1
                if  (vets[i - 1] == 4):
                    h2 = h2 + 1
            elif vets[i] == 3:
                if (vets[i + 1] == 1):
                    h2 = h2 + 1
                if (vets[i - 1] == 1):
                    h2 = h2 + 1
            elif vets[i] == 4:
                if (vets[i + 1] == 2):
                    h2 = h2 + 1
                if (vets[i - 1] == 2):
                    h2 = h2 + 1
    return h2

# Número de peças diferentes por lado
def heuristica3(s, h3):
    i = 0
    global si

    for i in range(len(si)):
        if i == 0:
            if s.estado[0] != s.estado[1]:
                h3 = h3 + 1
            if s.estado[1] != s.estado[2]:
                h3 = h3 + 1
            if s.estado[0] != s.estado[2]:
                h3 = h3 + 1

        if i == 3:
            if s.estado[3] != s.estado[4]:
                 h3 = h3 + 1
            if s.estado[4] != s.estado[5]:
                h3 = h3 + 1
            if s.estado[3] !=  s.estado[5]:
                h3 = h3 + 1

        if i == 6:
            if s.estado[6] != s.estado[7]:
                h3 = h3 + 1
            if s.estado[7] != s.estado[8]:
                h3 = h3 + 1
            if s.estado[6] != s.estado[8]:
                 h3 = h3 + 1

        if i == 8:
            if s.estado[8] != s.estado[9]:
                h3 = h3 + 1
            if s.estado[9] != s.estado[10]:
                h3 = h3 + 1
            if s.estado[8] != s.estado[10]:
                h3 = h3 + 1

    return h3

def show_path(s): 
    if s == None:
        return

    show_path(s.parent)
    print('  -%d  %d  %d-' % (s.estado[0], s.estado[1], s.estado[2]))
    print('%d           %d ' % (s.estado[11], s.estado[3]))
    print('%d           %d ' % (s.estado[10], s.estado[4]))
    print('%d           %d ' % (s.estado[9], s.estado[5]))
    print('  -%d  %d  %d-' % (s.estado[8], s.estado[7], s.estado[6]))
    print('Custo = %d' %s.custo)
    print('Heuristica =  %d' %s.heuristica)
    print('\n')

def goals(s):
    global si
    for i in range(len(si)):
        if si[i] != s.estado[i]:
            return False
    return True
  
#Busca gulosa pela melhor escolha
def bgme():
    global reg
    global contador

    s = cria_estrutura()
    print('\n----------------------------------')
    print('ESTADO OBJETIVO')
    exibe2(s)
    print('----------------------------------')
    s = initial_state()
    print('ESTADO INICIAL')
    exibe2(s)
    print('----------------------------------')
    
    s.custo = 0
    s.heuristica = 0

    enqueue(s)

    while not empty_queue():

        s = dequeue()
       
        if(goals(s)):
            print("DESEMBARALHAMENTO COMPLETO!\n")
            exibe2(s)
            print('----------------------------------')
            print('RESULTADO:')
            print('Custo = %d' % s.custo)
            print('Heuristica = %d' % s.heuristica)
            print('Estados Espandidos = %d' %contador)
            print('----------------------------------')
            print('CAMINHO:\n')
            show_path(s)
            return True

        children = expande(s)
        reg.append(s.estado)

        for child in children:
           enqueue(child)

    print('ESTADO COM RESULTADO IMPOSSIVEL DE SER ENCONTRADO') 
    return False

#sequencia()
bgme()
