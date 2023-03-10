import pandas as pd
# from tqdm import tqdm


def appChange(data, maquina, index, col_M, col_T):
    if maquina == data[index][col_M]:
        if index == 0:
            if data[index][col_T] != '':
                return True
            else:
                return False
        else:
            if data[index][col_T] != '':
                if data[index][col_T] != data[index - 1][col_T]:
                    return True
                else:
                    return False


def cambios(df, maquinas, tCambios):
    carga = df.values.tolist()
    maq = [i for i in maquinas]

    cam_cable = []
    for i in maq:
        total = 0
        for index in range(len(carga)):
            if i == carga[index][13]:
                if index == 0:
                    total += 1
                if carga[index][-1] != carga[index-1][-1]:
                    total += 1
        cam_cable.append(total)
    cam_app_L = []
    for m in maq:
        total = 0
        for i in range(len(carga)):
            if appChange(data=carga, maquina=m, index=i, col_M=13, col_T=7):
                total += 1
        cam_app_L.append(total)

    cam_app_R = []
    for m in maq:
        total = 0
        for i in range(len(carga)):
            if appChange(data=carga, maquina=m, index=i, col_M=13, col_T=8):
                total += 1
        cam_app_R.append(total)

    t_cambios = []
    for i in range(len(maq)):
        tAppTotal = (cam_app_L[i] + cam_app_R[i]) * tCambios['app']
        tCableTotal = cam_cable[i] * tCambios['cable']
        t_cambios.append( tAppTotal + tCableTotal )

    tPorHora = []
    for i in t_cambios:
        tPorHora.append(round(i / 16.4, 2))

    velocidadReq = []
    for i in range(len(maq)):
        if tPorHora[i] == 0:
            velocidadReq.append(0)
        else:
            vel = round((maquinas[maq[i]]['uph'] / (60 - tPorHora[i])) * 60, 2)
            velocidadReq.append(vel)

    cambios = pd.DataFrame(list(zip(maq, cam_cable, cam_app_L, cam_app_R, t_cambios, tPorHora, velocidadReq)),
                           columns=['Maquina', 'Cable', 'App L', 'App R', 'Setup', 'Setup X Hora', 'Velocidad Requerida'])
    return cambios
