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

def updateHelper(prensas, apps, con):
    cur = con.cursor()
    cur.execute('DELETE FROM applicadores;')
    cur.execute('DELETE FROM prensas;')
    prensas = prensas.values.tolist()
    for i in prensas:
        cur.execute('''
            INSERT INTO prensas (
                lot, pn, terminal_union, circuito,
                terminal_l, terminal_r,
                sub_material, maquina, proceso
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?
            );''', (i[1], i[2], i[3], i[7], i[12], i[13], i[14], i[15], i[17]))
        con.commit()

    apps = apps.values.tolist()
    for i in apps:
        cur.execute('''
            INSERT INTO applicadores (
                maquina, app, codigo_app
            ) VALUES (
                ?, ?, ?
            );''', (i[3], i[1], i[0]))
        con.commit()
    cur.close()
    con.close()



