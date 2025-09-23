servicos = {
    "formatação": 80,
    "limpeza geral": 50,
    "remoção de vírus": 60,
    "instalação de programas": 40
}

estoque = {
    "memória RAM": 10,
    "HD": 5,
    "SSD": 7,
    "fonte": 4,
    "placa de vídeo": 3
}

reparos = []

def listar_servicos():
    print("\n--- Lista de Serviços ---")
    for nome, preco in servicos.items():
        print(f"{nome} - R$ {preco}")
    print("-------------------------")

def adicionar_reparo():
    cliente = input("Nome do cliente: ")
    descricao = input("Descrição do reparo (ex: formatação, troca de SSD, etc): ")
    preco = float(input("Preço do serviço (R$): "))
    tecnico = input("Técnico responsável: ")
    reparo = {
        "cliente": cliente,
        "descricao": descricao,
        "preco": preco,
        "tecnico": tecnico,
        "status": "em análise"
    }
    reparos.append(reparo)
    print(f"\n[OK] Reparo adicionado para {cliente}.")

def atualizar_status():
    cliente = input("Nome do cliente: ")
    novo_status = input("Novo status (ex: em manutenção, finalizado): ")
    for r in reparos:
        if r["cliente"] == cliente:
            r["status"] = novo_status
            print(f"[OK] Status atualizado para '{novo_status}'.")
            return
    print("[ERRO] Cliente não encontrado.")

def consultar_status():
    cliente = input("Nome do cliente: ")
    for r in reparos:
        if r["cliente"] == cliente:
            print(f"O computador de {cliente} está: {r['status']}")
            return
    print("[ERRO] Cliente não encontrado.")

def vender_peca():
    nome_peca = input("Nome da peça: ")
    quantidade = int(input("Quantidade a vender: "))
    if nome_peca in estoque:
        if estoque[nome_peca] >= quantidade:
            estoque[nome_peca] -= quantidade
            print(f"[OK] {quantidade}x {nome_peca} vendida(s). Restam {estoque[nome_peca]}.")
            if estoque[nome_peca] <= 2:
                print(">>> Atenção: estoque baixo, faça reposição!")
        else:
            print("[ERRO] Quantidade maior do que no estoque.")
    else:
        print("[ERRO] Peça não encontrada.")

def gerar_relatorio():
    print("\n--- Relatório ---")
    print(f"Total de reparos: {len(reparos)}")
    tecnicos = {}
    for r in reparos:
        t = r["tecnico"]
        tecnicos[t] = tecnicos.get(t, 0) + 1
    print("Serviços por técnico:")
    for t, qtd in tecnicos.items():
        print(f" - {t}: {qtd} serviços")
    print("-----------------")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Listar serviços")
        print("2. Adicionar reparo")
        print("3. Atualizar status de reparo")
        print("4. Consultar status de reparo")
        print("5. Vender peça")
        print("6. Gerar relatório")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_servicos()
        elif opcao == "2":
            adicionar_reparo()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            consultar_status()
        elif opcao == "5":
            vender_peca()
        elif opcao == "6":
            gerar_relatorio()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida, tente novamente.")

menu()

1. Gerenciar serviços oferecidos

O sistema deve listar os tipos de serviços disponíveis e seus valores.



2. Cadastrar reparos

O sistema deve permitir adicionar um reparo, com informações do cliente, descrição, preço, técnico responsável e status inicial.



3. Atualizar status do reparo

O sistema deve permitir atualizar em qual fase o equipamento do cliente está (ex.: em análise, em manutenção, finalizado, pronto para retirar).



4. Consultar status do reparo

O cliente (ou funcionário) pode consultar em que status está o serviço.



5. Gerenciar estoque de peças

O sistema deve controlar a quantidade de peças em estoque, registrar saídas (venda/troca) e avisar quando o estoque está baixo.



6. Gerar relatórios

O sistema deve gerar relatórios com:

Quantidade total de reparos cadastrados

Serviços realizados por cada técnico

Possibilidade de incluir futuramente: tempo médio de reparo, defeitos mais comuns, faturamento.




7. Cobrança de taxas adicionais (pode ser adicionado depois)

Taxa de orçamento (R$ 30 quando o cliente não aprova).

Taxa de armazenamento após 30 dias sem retirada (R$ 10/dia).



8. Menu interativo

O sistema deve possuir um menu para navegar entre as opções de forma simples.

diagrama 
flowchart TD
    A[Cliente] -->|Solicita orçamento| B[Adicionar Reparo]
    A -->|Consulta andamento| C[Consultar Status]
    A -->|Retira equipamento| F[Fim do serviço]

    D[Técnico] -->|Executa serviço| B
    D -->|Atualiza progresso| E[Atualizar Status]
    D -->|Vende peça| G[Vender Peça]
    D -->|Gera relatório| H[Gerar Relatório]

    B --> E
    E --> C
    G --> H
