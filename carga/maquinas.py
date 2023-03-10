def maquinas(con, area):
    cur = con
    res = cur.execute('SELECT * FROM maquinas where area = ?;', (area,))
    res = res.fetchall()
    res = [ list(i) for i  in res]
    maquinas = {}
    for i in res:
        maquinas[i[0]]= {}
        maquinas[i[0]]['area'] = i[1]
        maquinas[i[0]]['sub area'] = i[2]
        maquinas[i[0]]['uph'] = i[3]
    # for i, x in maquinas.items():
    #     print(i, x)
    return maquinas

def turnos(con):
    cur = con
    res = cur.execute('SELECT * FROM turnos;')
    res = res.fetchall()
    turnos = dict(res)
    return turnos


def tiemposDeCambio(con):
    cur = con
    res = cur.execute('SELECT * FROM tiempo_cambio;')
    res = res.fetchall()
    tCambio = dict(res)
    return tCambio

def allInfo(db, area):
    maq = maquinas(db, area)
    turn = turnos(db)
    tCam = tiemposDeCambio(db)
    return maq, turn, tCam



