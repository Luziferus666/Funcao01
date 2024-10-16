# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade(numero):
    if numero % 2 == 0:
        return("par")
    else:
        return("ímpar")
number = int(input("diga um numero"))
verificar_a_paridade = verificar_paridade(number)
print(f"o numero é {verificar_a_paridade}")