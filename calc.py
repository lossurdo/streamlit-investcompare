import math


def calcular_curva_alteracao_cdi(cdi_inicial: float, cdi_final: float, periodos: int, converter_ao_mes: bool) -> dict:
    """
    Calcula a curva de alteração de CDI para um período.
    Leva em consideração o fato de o CDI ir mudando gradualmente
    ao longo dos meses até chegar a um valor alvo, embora seja
    sabido que a mudança da Selic ocorre a cada 45 dias. É apenas
    uma estimativa.

    :param cdi_inicial: Ex. 10.0
    :param cdi_final: Ex. 12.0
    :param periodos: 24 (meses)
    :param converter_ao_mes: true para converter a taxa ao mês, false para manter a taxa ao ano
    """
    curva = {}
    incremento = (max(cdi_inicial, cdi_final) - min(cdi_inicial, cdi_final)) / periodos
    for i in range(periodos):
        if cdi_inicial < cdi_final:
            incremento = abs(incremento)
        else:
            incremento = -abs(incremento)
        v = cdi_inicial + (incremento * i)
        if converter_ao_mes:
            curva[i] = converter(v, 1 / 12.0)
        else:
            curva[i] = v
    return curva


def converter(taxa: float, expoente: float) -> float:
    """
    Converte uma taxa de um período para outro.

    :param taxa: ex. 12.68 (12.68%)
    :param expoente: ex. 1/12.0 (De 12,68% ao ano para a taxa ao mês)
    """
    return (math.pow(1 + taxa / 100.0, expoente) - 1) * 100.0


def fv(taxa: float, periodo: float, valor_inicial: float) -> float:
    """
    Calcula o valor futuro de um investimento, dados a taxa,
    o valor inicial e o período. Utilizado para calcular o
    valor futuro de um investimento, sem aportes.

    :param taxa: ex. 1.0 (1%)
    :param periodo: ex. 12.0 (12 meses)
    :param valor_inicial: ex. 1000.0
    """
    return valor_inicial * math.pow(1 + taxa / 100.0, periodo)


def calcular_imposto_renda(vlr_periodo_dias: int) -> float:
    """
    Calcula o imposto de renda para um período de dias.

    :param vlr_periodo_dias: ex. 365 (dias)
    """
    if vlr_periodo_dias <= 180:
        return 22.5
    elif vlr_periodo_dias <= 360:
        return 20.0
    elif vlr_periodo_dias <= 720:
        return 17.5
    else:
        return 15.0
