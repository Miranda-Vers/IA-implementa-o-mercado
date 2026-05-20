import json
from datetime import datetime


dados_estoque = [
    {
        "id": 101,
        "produto": "Iogurte Natural 500g",
        "categoria": "Laticínios",
        "validade": "2026-05-25",  # Ex proximo do vencimento
        "estoque_atual": 50,
        "nivel_ideal": 30
    },
    {
        "id": 102,
        "produto": "Arroz Integral 5kg",
        "categoria": "Mercearia",
        "validade": "2026-12-30",
        "estoque_atual": 100,
        "nivel_ideal": 80
    }
]

def motor_de_regras_simbolica(item):
    """
    Aplica a lógica de IA Simbólica (Se P então Q) baseada no projeto SAGV.
    """
    hoje = datetime.now()
    data_validade = datetime.strptime(item['validade'], "%Y-%m-%d")
    dias_para_vencer = (data_validade - hoje).days
    
    # Inicializa variáveis de decisão
    item['status_cor'] = "Verde"
    item['sugestao_desconto'] = 0
    item['alerta'] = "OK"

    # REGRA 1: Risco Crítico (7 dias ou menos)
    if dias_para_vencer <= 7:
        item['status_cor'] = "Vermelho"
        item['sugestao_desconto'] = 0.30  # 30% conforme RF05/IA
    
    # REGRA 2: Risco Médio (entre 8 e 14 dias)
    elif 8 <= dias_para_vencer <= 14:
        item['status_cor'] = "Amarelo"
        item['sugestao_desconto'] = 0.20  # 20% conforme premissas
        
    # REGRA 3: Negociação/Excesso de Estoque
    if dias_para_vencer > 21 and item['estoque_atual'] > item['nivel_ideal']:
        item['alerta'] = "Avaliar devolução ao fornecedor"

    return item

# Execução do processamento
resultados = [motor_de_regras_simbolica(produto) for produto in dados_estoque]

# Exibe o resultado formatado
print(json.dumps(resultados, indent=4, ensure_ascii=False))