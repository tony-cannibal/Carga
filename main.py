import pandas as pd
import carga
import carga.corte as corte
from database import connection as con
from functions import *


db = "carga.db"
help_db = "helper.db"


df = pd.read_excel("info/data.xlsx", sheet_name=None)

# carga.updateHelper(df['10500'], df['50160'], con(help_db))

# aplicadores = df['50160']
#
auto = trim_auto(df["10400"])
#
# # maquinas, turnos, tCambios = carga.allInfo(con(db), 'm1')
#
# # status = carga.status(maquinas, auto, turnos)
# # cambios = corte.cambios(auto, maquinas, tCambios)
#
# apps = apps(aplicadores)
genStatus = specificStatus(auto, con(help_db))

genStatus.to_excel('output.xlsx', index=False)

#
# # print(aplicadores)
