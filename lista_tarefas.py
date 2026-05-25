# Exercício 3 — Lista de tarefas
#      Crie um programa que:
#      permita cadastrar tarefas;
#      finalize quando o usuário digitar “fim”;
#      exiba todas as tarefas
ta = []
while True:



    t = input("Digite suas tarefas, quando as finalizar, digite fim: ")
    
    if t == "fim":
        break

    else:
     ta.append(t)
    
    print(ta)