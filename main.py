print("Bem-vindo ao sistema de vendas de ingressos para o jogo do Flamengo!")

usuarios_cadastrados = [
    {
        "nome": "joao",
        "cpf": "123.456.789-00",
        "email": "joao@email.com"
    },
    {
        "nome": "maria",
        "cpf": "987.654.321-11",
        "email": "maria@email.com"
    }
]  # Lista de usuários cadastrados

login = input("Digite seu Nome: ").strip().lower()

# Variável para controlar se a gente achou o usuário ou não
usuario_encontrado = False

# Passando por cada dicionário da lista para conferir o nome
for usuario in usuarios_cadastrados:
    if usuario["nome"] == login:
        usuario_encontrado = True
        break  # Achou, pode parar de procurar

# Agora a gente valida o resultado com base na bandeirinha (usuario_encontrado)
if usuario_encontrado:
    print("Login realizado com sucesso! Seja bem-vindo!")
else:
    nao_possui_cadastro = input("Você não possui cadastro, deseja se cadastrar? (sim/não): ").strip().lower()

    if nao_possui_cadastro == "sim":
        print("\n--- FAÇA SEU CADASTRO ---")
        
        nome_cad = input("Digite seu Nome: ").strip().lower()
        sobrenome_cad = input("Digite seu Sobrenome: ").strip().lower()
        
        # CPF sem int() para aceitar pontos e traços como texto
        cpf_cad = input("Digite seu CPF: ").strip()
        
        email_cad = input("Digite seu E-mail: ").strip().lower()
        
        # Idade blindada para não quebrar se vier vazia ou texto
        while True:
            try:
                idade_cad = int(input("Digite sua Idade: "))
                break
            except ValueError:
                print("⚠️ Digite apenas números inteiros válidos para a idade!")
        
        # Adicionando o novo dicionário na lista
        usuarios_cadastrados.append({
            "nome": nome_cad,
            "sobrenome": sobrenome_cad,
            "cpf": cpf_cad,
            "email": email_cad,
            "idade": idade_cad
        })
        print("Cadastro realizado com sucesso!")
        
    else:
        print("Cadastro cancelado.")