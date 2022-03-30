## Calcula as principais fórmulas estatísticas de uma lista fornecida pelo usuário
## Alessandro Miranda - 18/03/2022
## Obs: existem bibliotecas que podem gerar estas informações mais rapidamente e com facilidade.
##      O objetivo aqui é ir às origens dos cálculos para fins educativos

def desvio_amostral(lista):
    return (variancia_amostral(lista) ** 0.5)       ## Elevar a 0,5 equivale à raiz quadrada da variância amostral

def desvio_populacional(lista):
    return (variancia_populacional(lista) ** 0.5)   ## Elevar a 0,5 equivale à raiz quadrada da variância populac.

def entrar_dados():
    entrada = input('Informe os itens na lista (separados por espaço): ')
    lista = entrada.split()
    lista = sorted(lista)              # Ordena para facilitar descobrir o menor número (elem. 0) e o maior (último elem)
    lista = list(map(float, lista))    # Transforma a lista recebida como "string" para "int"
    return lista

def imprimir_resultados(lista):
    qtd = qtd_elementos(lista)
    med = media(lista)
    print('----------------------------------')
    print('| Análise estatística            |')
    print('----------------------------------')
    print('Quant.elementos         : {0:8.2f}'.format(qtd))
    print('Menor elemento          : {0:8.2f}'.format(minimo(lista)))
    print('Maior elemento          : {0:8.2f}'.format(maximo(lista)))
    print('Média                   : {0:8.2f}'.format(med))
    print('Moda                    : {0:8.2f}'.format(moda(lista)))
    print('Variância amostral      : {0:8.2f}'.format(variancia_amostral(lista)))
    print('Variância populacional  : {0:8.2f}'.format(variancia_populacional(lista)))
    print('Desvio padrão amostral  : {0:8.2f}'.format(desvio_amostral(lista)))
    print('Desvio padrão populac.  : {0:8.2f}'.format(desvio_populacional(lista)))
    print('----------------------------------')


def maximo(lista):
    return lista[len(lista)-1]

def minimo(lista):
    return lista[0]

def media(lista):
    med = sum(lista) / len(lista)
    return med

def moda(lista):
    maior = 0
    for i in range(len(lista)):
        if lista.count(lista[i]) >= maior:  ## Conta a ocorrência deste elemento na lista
            moda = lista[i]                 ## Se for a maior quantidade até agora, considera o número como "moda"
    return moda

def qtd_elementos(lista):
    l = len(lista)
    return l

def variancia(valor,media):
    return (valor-media)**2

def variancia_amostral(lista):
    m = media(lista)
    var_amostral = 0
    qtd = qtd_elementos(lista)
    for i in range(qtd):
        var_elemento = variancia(lista[i], m)
        var_amostral += var_elemento
    var_amostral = var_amostral / (qtd - 1)
    return var_amostral

def variancia_populacional(lista):
    m = media(lista)
    var_populacional = 0
    #maior = 0
    qtd = qtd_elementos(lista)
    for i in range(qtd):
        var_elemento = variancia(lista[i], m)
        #var_amostral += var_elemento
        var_populacional += var_elemento
        # if lista.count(lista[i]) >= maior:  ## Conta a ocorrência deste elemento na lista
        #     maior = lista.count(lista[i])  ## se for o maior, guarda a qtd. elementos
        #     moda = lista[i]  ## Se for a maior quantidade até agora, considera o número como "moda"
    var_populacional = var_populacional / (qtd)
    return var_populacional

lista = entrar_dados()
imprimir_resultados(lista)
