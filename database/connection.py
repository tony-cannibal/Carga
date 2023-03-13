import sqlite3
import pandas as pd


def connection(db):
    con = sqlite3.connect(db)
    return con


def deploydb(db):
    cur = db.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS maquinas (
                    maquina VARCHAR(6) PRIMARY KEY,
                    area VARCHAR(4),
                    subArea VARCHAR(30),
                    uph INT
                    );''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS turnos (
                    turno VARCHAR(3) PRIMARY KEY,
                    horas REAL
                    );''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS tiempo_cambio (
                    tipo VARCHAR(10) PRIMARY KEY,
                    minutos REAL
                    );''')
    cur.close()
    db.close()

def deploy_helper(db):
    cur = db.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS prensas (
                    lot VARCHAR(20),
                    pn VARCHAR(20),
                    terminal_union VARCHAR(15),
                    circuito VARCHAR(8),
                    terminal_l VARCHAR(15),
                    terminal_r VARCHAR(15),
                    sub_material VARCHAR(15),
                    maquina VARCHAR(5),
                    proceso VARCHAR(50)
                    );''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS applicadores (
                    maquina VARCHAR(5),
                    app VARCHAR(12),
                    codigo_app VARCHAR(10)
                    )
                ''')
    cur.close()
    db.close()


def populateMaquinas(db, data):
    df = pd.read_excel(data)
    df = df.values.tolist()
    cur = db.cursor()
    for i in df:
        cur.execute(f'''
                    INSERT INTO maquinas (
                        maquina, area, subArea, uph
                    ) VALUES (
                        ?, ?, ?, ?
                    );
                    ''', (i[0], i[1], i[2], i[3]))
        db.commit()
    cur.close()
    db.close()

def populateTurno(db):
    turnos = [
            ('A', 8.4),
            ('B', 8),
            ('C', 0)
            ]
    cur = db.cursor()
    for i in turnos:
        cur.execute(f'''
                    INSERT INTO turnos (
                        turno, horas
                    ) VALUES (
                        ?, ?
                    );
                    ''', i)
        db.commit()
    cur.close()
    db.close()

def populateTiempoCambio(db):
    tCambio = [
            ('app', 2),
            ('cable', 2)
            ]
    cur = db.cursor()
    for i in tCambio:
        cur.execute(f'''
                    INSERT INTO tiempo_cambio (
                        tipo, minutos
                    ) VALUES (
                        ?, ?
                    );
                    ''', i)
        db.commit()
    cur.close()
    db.close()

if __name__ == "__main__":
    pass
    # populatedb(connection(database), data)
