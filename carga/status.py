import pandas as pd


def status(maquinas, df, turno):
    err_maq = []
    for i in df['Maquina'].unique():
        if i not in maquinas:
            err_maq.append(i)
    input = []
    for i in maquinas:
        input.append(df[df['Maquina'] == i]['Cantidad'].sum())
    uph = []
    for i in maquinas:
        try:
            uph.append(maquinas[i]['uph'])
        except KeyError:
            uph.append(0)
    cap_a = []
    for i in range(len(maquinas)):
        cap_a.append(uph[i] * turno['A'])
    cap_b = []
    for i in range(len(maquinas)):
        cap_b.append(uph[i] * turno['B'])
    cap_total = []
    for i in range(len(maquinas)):
        cap_total.append(cap_a[i] + cap_b[i])
    dif = []
    for i in range(len(maquinas)):
        dif.append(cap_total[i] - input[i])

    status = pd.DataFrame(list(zip(
        maquinas, uph, cap_a, cap_b, cap_total, input, dif)), columns=[
        'Mauqinas', 'UPH', 'Capacidad A', 'Capacidad B',
        'Capacidad Total', 'Input', 'Dif'])
    status.to_excel('output.xlsx', index=False)
    return status
