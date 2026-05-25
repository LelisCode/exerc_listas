# Exercício 5: Lista de compras
#      Exibir um menu de opções para esta d de compras: 

#              1 - Adicionar a d 
#              2 - Pesquisar item 
#              3 - Remover item
#              4 - Alterar item
#              5 - Listar produtos
#              6 - Sair

#      para a opção 1 solicitar ao usuário digitar produtos para compra até digitar a palavra "sair"
#      para a opção 2 solicitar um produto a ser pesquisado na lista se encontrar o produto, exibir o mesmo senão exibir produto não encontrado;
#      para  a opção 3 solicitar o nome do produto a ser removido da lista se encontrar, exibir na tela "produto encontrado" senão exibir "produto não encontrado";
#      para a opção 4 solicitar o nome do produto a ser alterado. se encontrar exibir na tela "produto alterado com sucesso" senão exibir "produto não encontrado"
#      para a opção 5 listar todos os produtos cadastrados. se não houver produtos cadastrados, exibir a mensagem "Lista vazia" senão exibir os produtos cadastrados.
#      para a opção 6 sair do programa e exibir na tela "Programa encerrado com sucesso!".
print("-" * 50)
print("PRODUTOS")
print("-" * 50)
d = {
 
    "Morango": 50.00,
  "Banana": 30.00,
  "Uva": 80.00,
  "Pessêgo": 90.00,
  "Laranja": 20.00

  }


def l(d):

     

    for frutas in d.items():
      
       print(f"{frutas}")


opcoes = {

    "Adicionar item": 1,
    "Pesquisar item": 2,
    "Remover item": 3,
    "Alterar item": 4,
    "Listar produtos": 5,
    "Sair": 6
}

def escolhas(opcoes):

    for chave, valor in opcoes.items():
        
        print(f"{valor} - {chave}")
        
   


l(d)

escolhas(opcoes)



def itens():
    p = input("Escolha um dos números acima: ")
    return p

opcao = itens()       
match opcao:
    case "1": 
        while True:
            p = input("Digite o produto (ou 'sair'): ")  
           
            if p == "sair":
                break
            
            v = float(input(f"Digite o preço de {p}: "))

            p_f = p.capitalize() 
                
            d[p_f] = v
            print (d)
    case "2":
        print()
        b = input("Buscar pelo produto: ")

        
        pp = b.capitalize() 

        if pp in d:
            print("Produto foi encontrado!")
           
            print(f"{pp}: R$ {d[pp]:.2f}")
        else:
            print("Produto não encontrado;")
    case "3":
        r = input("Digite o nome do produto a ser removido: ")
        pr = r.capitalize()

        if pr in d:
             del d[pr] 
             print("Produto removido")
             print(d)
        else:
            print("Produto não encontrado")
  
    case "4":
        print()
      
        pm = input("Digite o nome do produto que deseja modificar: ")
        
        m = pm.capitalize()
   
        if m in d:
        
            vm = float(input(f"Digite o novo valor para {m}: "))
            

            d[m] = vm
            print("Produto alterado com sucesso!")
            print(d)
        else:
            print("Produto não encontrado")



    case "5":
        print()
        
        if len(d) == 0:
            print("Lista vazia")
        else:
            print("--- PRODUTOS CADASTRADOS ---")
            
            for indice, (produto, preco) in enumerate(d.items(), start=1):
                print(f"{indice} - {produto}: R$ {preco:.2f}")

  
    case "6":
       while True:
        break
     
