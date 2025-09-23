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