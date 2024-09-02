import json


def teste1():
    indice = int(13) 
    soma = int(0)
    k = int(0)

    while k < indice:
        k = k + 1
        soma = soma + k

    return (f'o valor da variavel soma é: {soma}')
def teste2():
    n = int(input("informe o número:")) # solicitanso ao usuário o numero há ser verificado
    a = int(0) # variavel inicial
    b = int(1) # variavel inicial
    aux = int(0) # variavel que ajuda a troca as variaveis

    while b <= n:
        if b == n: # verificando se b é igual ao numero informando 
            return (f'o numero {n} pertence a sequencia fibonacci')
        else:
            aux = a
            a = b
            b = aux + b # acrescentando o proximo numero da sequencia
    return (f'o numero {n} não pertence a sequencia fibonacci') # se o loop terminar sem encontrar o numero é porque ele não pertence a sequencia    
def teste3():


    # vamos abrir o arquivo 
    with open ('Estágio - São Paulo\\arquivo.json','r') as f:
        dados = json.load(f)


    fat = [] #criando a lista de faturamento 
    for dia in dados:
        if dia['valor'] > 0:
            fat.append(dia['valor'])

    menorv = min(fat) # verifica o menor valor do faturamento
    maiorv = max(fat) # verifica o maior valor do faturamento
    totalv = sum(fat) # verifica o valor total do faturamento para utilizar na media.
    dias = len(fat) # Esta contando quantos dias de faturamento
    media = totalv/dias # utilizando o valor total e a quantidade de dias para obter a media de faturamento.





    
    Dacima_media = 0 # variavel para contar quantos dias acima da media tivemos

    for valor in fat:
        if valor > media:
            Dacima_media = Dacima_media + 1

    print (f'Menor valor de faturameto: R${menorv:.2f}')
    print (f'Maior valor de faturameto: R${maiorv:.2f}')
    print (f'Numero de dias com faturameto acima da media: {Dacima_media:}')
def teste4(n):

    fattotal = sum(n.values())
    #calculando o percentual por estado
    for estado, valor in n.items():
        percentual = (valor/fattotal)*100
        print (f'{estado}: {percentual:.2f}%')
    
        
def main ():
    dados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53}
    #faturamento = ('Testes-e-vagas/Estágio - São Paulo/faturamento.json')
    #print(f'1° teste {teste1()}')
    #print(f'2° teste {teste2()}')
    #print(f'3° teste {teste3()}')
    #print(f'4° teste {teste4(dados)}')
    print(f'5° teste {teste5()}')


    return 0


if __name__ == "__main__":
    main()