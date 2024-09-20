from models.dispositivo import DispositivoDB

def calcular_gasto(dispositivos: list[DispositivoDB]):
    gasto_diario = sum(
        dispositivo.potencia * dispositivo.tempo_uso_diario
        for dispositivo in dispositivos
    )
    gasto_mensal = gasto_diario * 30
    gasto_anual = gasto_diario * 365

    return gasto_diario, gasto_mensal, gasto_anual
