"""1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

k = 0 
indice = 13 
soma = 0

for k in range(indice):
    k + 1
    soma = soma + k
    print(soma)

