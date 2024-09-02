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
def teste3(arquivo_json):
    # vamos abrir o arquivo 
    with open (arquivo_json, r) as f:
        dados = json.laod(f)


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

    for estado, valor in dados.items():
        percentual = (valor/totalv)*100
        print (f'{estado}: {percentual:.2f}%')
        
    




def main ():
    import json

    #print(f'1° teste {teste1()}')
    #print(f'2° teste {teste2()}')
    print(f'3° teste {teste3()}')

    return 0


if __name__ == "__main__":
    main()