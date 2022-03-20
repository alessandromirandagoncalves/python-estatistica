## Calcula as principas fórmulas estatísticas de uma lista fornecida pelo usuário
## Alessandro Miranda - 18/03/2022
## Obs: existem bibliotecas que podem gerar estas informações mais rapidamente e com facilidade.
##      O objetivo aqui é ir às origens dos cálculos para fins educativos

def calc_variancia(valor,media):
    return (valor-media)**2

entrada = input('Informe os itens na lista (separados por espaço): ')
lista = entrada.split()
lista=sorted(lista)              # Ordena para facilitar descobrir o menor número (elem. 0) e o maior (último elem)
lista = list(map(int, lista))    # Transforma a lista recebida como "string" para "int"
qtd_elementos = len(lista)       # Guarda em variável para evitar calcular várias vezes, ganhando performance
media = sum(lista)/qtd_elementos # Guarda em variável para evitar calcular várias vezes, ganhando performance
variancia_amostral = 0
variancia_populacional = 0
moda = 0
maior = 0
for i in range (qtd_elementos):
    var_elemento = calc_variancia(lista[i],media)
    variancia_amostral += var_elemento
    variancia_populacional += var_elemento
    if lista.count(lista[i]) >= maior:       ## Conta a ocorrência deste elemento na lista
        maior = lista.count(lista[i])        ## se for o maior, guarda a qtd. elementos
        moda = lista[i]                      ## Se for a maior quantidade até agora, considera o número como "moda"

variancia_amostral = variancia_amostral/(qtd_elementos-1)
variancia_populacional = variancia_populacional/(qtd_elementos)
desvio_amostral = variancia_amostral*0.5            ##Elevar a 0,5 equivale à raiz quadrada da variância amostral
desvio_populacional = variancia_populacional*0.5    ##Elevar a 0,5 equivale à raiz quadrada da variância populac.

print ('----------------------------------')
print ('| Análise estatística            |')
print ('----------------------------------')
print ('Quant.elementos         : {0:8.2f}'.format(qtd_elementos))
print ('Menor elemento          : {0:8.2f}'.format(lista[0]))
print ('Maior elemento          : {0:8.2f}'.format(lista[qtd_elementos-1]))
print ('Média                   : {0:8.2f}'.format(media))
print ('Moda                    : {0:8.2f}'.format(moda))
print ('Variância amostral      : {0:8.2f}'.format(variancia_amostral))
print ('Variância populacional  : {0:8.2f}'.format(variancia_populacional))
print ('Desvio padrão amostral  : {0:8.2f}'.format(desvio_amostral))
print ('Desvio padrão populac.  : {0:8.2f}'.format(desvio_populacional))
print ('----------------------------------')
