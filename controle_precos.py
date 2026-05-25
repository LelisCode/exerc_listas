# Exercício 2 — Controle de preços
#      Solicite 5 preços e:
#      armazene em uma lista;
#      exiba o maior preço;
#      exiba o menor preço.

lista_p = []


for i in range(5):
    P = float(input("Digite os preço: "))
    lista_p.append(P)
    
    print("Preço máximo")
    print(max(lista_p))
    print("Preço mínimo")
    print(min(lista_p))
