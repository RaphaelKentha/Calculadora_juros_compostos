# Definindo as variáveis
patrimonio = float(input("Digite o seu patrimônio inicial: R$ "))
aporte_mes = float(input("Digite o valor dop aporte mensal: "))
rentabilidade = float(input("Digite a taxa de rentabilidade anual do seu investimento: "))
tempo = int(input("Digite o tempo de investimento em anos: "))

# Convertendo as taxas para decimais
rentabilidade = (rentabilidade / 100) / 12
tempo = tempo*12

def calcular_valor_futuro(aporte_mes, rentabilidade, tempo, patrimonio):
    """
    Calcula o valor futuro com base na fórmula de juros compostos com aportes mensais.
    
    Parâmetros:
    PMT (float): Aporte mensal.
    i (float): Taxa de juros mensal (em decimal, por exemplo, 5% é 0.05).
    n (int): Número de meses.
    Pv (float): Patrimônio inicial.
    
    Retorna:
    float: Valor futuro.
    """
    Fv = ((aporte_mes * ((1 + rentabilidade) ** tempo - 1)) / rentabilidade) + patrimonio * (1 + rentabilidade) ** tempo
    return Fv

Fv = calcular_valor_futuro(aporte_mes, rentabilidade, tempo, patrimonio)
print(f"O valor futuro após {tempo} meses será de R${Fv:.2f}")
