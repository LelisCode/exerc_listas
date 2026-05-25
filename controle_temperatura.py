# Exercício 4 - Controle de temperaturas
#      Solicite temperaturas em graus Celsius até o usuário digitar "sair";
#      Converta as temperaturas da lista em graus Celsius para uma nova lista de temperaturas em graus Fahrenheit;
#      Calcule e exiba as médias de ambas as temperaturas.



while True:

    lt = []
    lm = []
    T = input("Digite a temperatura em graus celsius, e sair ao finalizar: ")

    if T == "sair":
        break

    else:
      T = float(T)  	
      tf = (T * 9 / 5) + 32 
      lt.append(tf)
      print("Valor convertido em Fahrenheit")
      print(lt)
      tm = T + (tf / len(lt))
      
      lm.append(tm)
      print("A média entre as temperaturas")
      print(lm) 
