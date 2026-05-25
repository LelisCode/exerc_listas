# Exercício 1 — Lista de convidados
# Crie um programa que:
#      Cadastre 5 convidados;
#      Exiba todos os convidados;
#      Informe quantos convidados existem.

lc = []
for i in range(5):
    C = input("Digite o seu nome: ")
    lc.append(C)
    print("Convidados")
    print(lc)   
    print("Número de convidados")
    print(len(lc))          