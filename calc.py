import math

def calcular_curva_alteracao_cdi(cdi_inicial: float, cdi_final: float, periodos: int, converter_ao_mes: bool) -> dict:
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
    return (math.pow(1 + taxa / 100.0, expoente) - 1) * 100.0

def fv(taxa: float, periodo: float, valor_inicial: float) -> float:
    return valor_inicial * math.pow(1 + taxa / 100.0, periodo)

def imposto_renda(vlr_periodo_dias: int) -> float:
    if vlr_periodo_dias <= 180:
        return 22.5
    elif vlr_periodo_dias <= 360:
        return 20.0
    elif vlr_periodo_dias <= 720:
        return 17.5
    else:
        return 15.0