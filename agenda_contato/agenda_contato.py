# Função para adicionar um novo contato ( dicionário) dentro da lista
def salvar_contato(contatos, nome_contato, numero_contato):
  # Criamos um dicionário para representar o contato
  contato = {"nome":nome_contato,"numero": numero_contato, "favorito": False}
  # Adiciona esse dionário ao final da nossa lista de contatos
  contatos.append(contato)
  print(f"✅ Contato de {nome_contato} foi salvo com sucesso!")
  return

# Função para percorrer a lista e mostrar nome e número 
def listar_contato(contatos):
  print(f"\n<--Lista de contatos-->")
  # o enumerate nos dá o índice ( posição) começando em 1 e o conteúdo (contato)
  for indice, contato in enumerate(contatos, start=1):
    # Acessamos os valores pelas chaves do dicionário
    nome = contato["nome"]
    numero = contato["numero"]
    # Verifica se o contato é favorito para adicionar um ícone
    favorito = "⭐" if contato["favorito"] else""
    print(f"{indice}. Nome:{nome} - Número: ({numero}) {favorito}")
  return

def editar_contato(contatos):
  # Mostra a lista de contatos para ver qual contato quer editar 
  listar_contato(contatos)

  # Confere se tem contatos adicionados
  if not contatos:
    return
  
  # Cria um um try exception para ter uma excessao de erros e o programa nao quebrar 
  try:
    # o usuario escolhe qual numero da lista quer editar 
    indice_para_deletar = int(input("Digite qual o índice do contato que você deseja editar: "))
    # Ajusta o indice para não dar conflito com o indice do usuario e o índice do programa
    indice_ajustado = indice_para_deletar - 1

    # Verifica se o indice existe na lista 
    if 0 <= indice_ajustado < len(contatos):
      print(f"Editando o contato de : {contatos[indice_ajustado]['nome']}")

      # Pedimos os novos dados do contato 
      novo_nome = input("Digite o novo nome do contato, (ou precione enter para manter o atual):")
      novo_numero = input("Digite o novo número do contato, (ou precione enter para manter o atual):")

      # atualizamos os campos apenas se o usuário digitou algo 
      if novo_nome:
        contatos[indice_ajustado]["nome"] = novo_nome
      elif novo_numero:
        contatos[indice_ajustado]["numero"] = novo_numero
      print(f"✅ Contato editado com sucesso!")
    else:
      print("Índice inválido")
  except ValueError:
    print("⚠️ Por favor, digite um número válido")
  return
      

# Função para deletar um contato baseado na posição da lista
def deletar_contato(contatos):
  # Mostrando a lista para o usuário saber qual número escolher
  listar_contato(contatos)

  if len(contatos) == 0:
    return 
  
  try:
    # O usuário escolhe o número que vê na tela (1, 2, 3...)
    indice_para_deletar = int(input("\nDigite o índice do contato que você deseja deletar:"))
    # Ajustamos para o índice do python ( que começa em 0)
    indice_ajustado = indice_para_deletar - 1

    # Verfique se o número digitado existe na lista
    if 0 <= indice_ajustado < len(contatos):
      # .pop() remove o item da lista na posição indicada 
      contato_removido = contatos.pop(indice_ajustado)
      print(f"🗑️ Contato de {contato_removido['nome']} deletado com sucesso!")
    else:
      print("Número de contato inválido.")
  except ValueError:
    print("⚠️ Por favor, digite um número válido.")
  return

def favoritar_contato(contatos):
  listar_contato(contatos)
  # Escolher um número para favoritar 
  indice_para_favoritar = int(input("\nDigite o índice do contato que você deseja favoritar:"))
  indice_ajustado = indice_para_favoritar - 1
  contatos[indice_ajustado]["favorito"]= True
  print(f"Contato de {contatos[indice_ajustado]['nome']} favoritado com sucesso!")
  return


# --- Programa principal ---
# Lista global que armazenará nossos dicionários 
contatos = [] 
while True:
  print(f"\nAgenda")
  print(f"1- Salvar contato")
  print(f"2- listar contato")
  print(f"3- Editar contato")
  print(f"4- Deletar contato")
  print(f"5- Favoritar contato")
  print(f"6- Sair")

  escolha = input("Digite a opção desejada: ")

  match escolha:
    case "1":
      nome_contato = input("Digite o nome do contato que deseja salvar:")
      numero_contato = int(input("Digite o numero do contato que deseja salvar:"))
      salvar_contato(contatos, nome_contato, numero_contato)

    case "2":
      listar_contato(contatos)
    
    case "3":
      editar_contato(contatos)

    case "4":
      deletar_contato(contatos)
  
    case "5":
      favoritar_contato(contatos)
    
    case "6":
      break
print("Programa finalizado!")


 
