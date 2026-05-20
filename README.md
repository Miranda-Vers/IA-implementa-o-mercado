# Inteligência Artificial Simbólica aplicada ao SAGV

Este módulo detalha a análise de viabilidade e a lógica de implementação do motor de regras utilizado no **Sistema Administrativo de Gestão de Vencimentos (SAGV)** para o **Supermercado Yamauchi**.

## Análise de Viabilidade Técnica (Capítulo 9.2)

A aplicação de um algoritmo de **IA Simbólica** é considerada altamente viável e estratégica para otimizar o controle de estoque e validade na unidade da rede. Esta abordagem transforma dados brutos em decisões automatizadas de negócio.

### 1. Adequação ao Paradigma Simbólico

O projeto apresenta características ideais para o paradigma simbólico:


**Regras de Negócio Determinísticas**: O sistema utiliza faixas de vencimento claras ($7, 14 \text{ e } 21$ dias) com percentuais de desconto específicos, codificáveis diretamente em um motor de inferência.



**Auditabilidade e Explicabilidade**: Capacidade de explicar logicamente por que um lote recebeu determinada promoção, garantindo transparência em decisões financeiras e riscos legais.



**Estrutura de Dados Compatível**: O uso do **MongoDB** facilita a manipulação de símbolos e atributos que servem de entrada para as regras lógicas.



---

### 2. O Motor de Regras (Lógica de Implementação)

A IA atua como um motor de processamento que aplica lógica proposicional ($P \rightarrow Q$) sobre os dados de estoque:

| Status | Regra Lógica | Ação Recomendada |
| --- | --- | --- |
| **Risco Crítico** | SE $dias\_vencimento \leq 7$ 

 | Cor: **Vermelho** / Desconto: **30%** 

 |
| **Risco Médio** | SE $8 \leq dias\_vencimento \leq 14$ | Cor: **Amarelo** / Desconto: **20%** 

 |
| **Estratégico** | SE $dias\_vencimento > 21$ AND $estoque > ideal$ 

 | Alerta: **Avaliar devolução ao fornecedor** 

 |

---

### 3. Impacto e Benefícios


**Consistência**: Tratamento lógico padronizado para todos os lotes de uma mesma categoria.


  
**Baixo Custo Computacional**: Eficiência no processamento de grandes volumes (base de teste de **2 milhões de itens**) sem necessidade de hardware pesado.



**Integração Fluida**: Exportação em JSON pronta para consumo pelo ERP da empresa para atualização de preços.



---

## Expansão: Regras de Associação

Como evolução do sistema, propõe-se a análise de **Cesta de Compras** utilizando algoritmos como **FP-Growth**:


**Venda Cruzada (Cross-selling)**: Identificar padrões (ex: `{Vinho} => {Geleia}`) para criar kits promocionais com itens próximos ao vencimento.


 
**Aumento de Ticket Médio**: Utilizar as regras de associação para organizar o estoque físico e digital de forma estratégica.



> 
> **Conclusão**: A implementação da IA Simbólica no SAGV é uma solução de baixo risco e alto impacto, garantindo que o Supermercado Yamauchi reduza perdas financeiras e melhore a experiência do consumidor final.
> 
> 

---

### Como rodar o motor de regras

1. Certifique-se de ter o arquivo `estoque.json` na raiz.
2. Execute o script de IA: `python motor_regras.py`.
3. O resultado será um novo JSON pronto para integração.
