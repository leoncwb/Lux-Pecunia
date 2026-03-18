import re

def identificar_gasto(frase):
    # Base de conhecimento baseada na sua planilha
    categorias = {
        "CUSTOS FIXOS": ["aluguel", "escola", "faculdade", "plano de saúde", "seguro", "internet", "luz", "água"],
        "CONFORTO": ["diarista", "netflix", "spotify", "assinatura", "supermercado", "ifood básico"],
        "PRAZERES": ["restaurante", "madero", "cinema", "teatro", "bar", "cerveja", "viagem", "uber", "99", "balada"],
        "INVESTIMENTOS": ["ações", "fundo", "tesouro", "reserva", "liberdade financeira"]
    }

    # 1. Extrair valor numérico (procura por números seguidos ou precedidos de R$, $ ou apenas o dígito)
    valor_match = re.search(r'(\d+(?:[.,]\d{1,2})?)', frase)
    valor = valor_match.group(1) if valor_match else "0.00"
    
    # 2. Identificar a categoria por palavras-chave
    frase_lower = frase.lower()
    categoria_encontrada = "OUTROS / NÃO CATEGORIZADO"
    
    for categoria, palavras in categorias.items():
        if any(palavra in frase_lower for palavra in palavras):
            categoria_encontrada = categoria
            break
            
    return {
        "original": frase,
        "valor": valor,
        "categoria": categoria_encontrada
    }

# --- TESTE DO MOTOR ---
entradas = [
    "Gastei 50 reais no Uber para o trabalho",
    "Mensalidade da faculdade 1200",
    "Jantar no Madero 150.50",
    "Compra no mercado 400",
    "Netflix 55.90"
]

print(f"{'ENTRADA':<40} | {'VALOR':<10} | {'CATEGORIA'}")
print("-" * 75)
for item in entradas:
    res = identificar_gasto(item)
    print(f"{res['original']:<40} | {res['valor']:<10} | {res['categoria']}")
