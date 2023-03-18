#passo 1 - definir funções
def soma(numeros):
    return int(numeros[0]) + int(numeros[1])

def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])

def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])

def multiplicacao(numeros):
    return int(numeros[0]) * int(numeros[1])

#passo 2 - perguntar ao usuario qual operação ele quer realizar
numeros_input = input('Digite os números separados por espaço: ').split(' ') #encadeamento de duas funções
operacao_input = input('Digite a operação (+ / - *): ')
resultado_calculo = 0 #inicializa o calculo

#parte das estruturas de repetição do código
if len(numeros_input) != 2:
    print('Quantidade de entradas diferente de 2')
else:
    if operacao_input in '+/-*':
        if operacao_input == '+':
            resultado_calculo = soma(numeros_input)

        elif operacao_input == '/':
            resultado_calculo = divisao(numeros_input)

        elif operacao_input == '-':
            resultado_calculo = subtracao(numeros_input)

        elif operacao_input == '*':
            resultado_calculo = multiplicacao(numeros_input)

        print(f'Resultado: {resultado_calculo}')
    else:
        print(f'Operação {operacao_input} inválida')