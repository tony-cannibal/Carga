import pandas as pd


def trim_auto(df):
    columns = [2, 8, 9, 21, 22]
    df.drop(df.columns[columns], axis=1, inplace=True)
    df = df.fillna("")
    df.rename(
        columns={"TMNL_L(Semi-auto).1": "TMNL_R(Semi-auto)"}, inplace=True)
    # print(df.columns)
    df.to_excel("corte.xlsx", index=False)
    return df


def apps(df):
    columns = [2, 4, 5, 6, 7, 8]
    df.drop(df.columns[columns], axis=1, inplace=True)
    df_list = df.values.tolist()
    df.sort_values(by=["Almacen"], inplace=True)
    maqs = df["Almacen"].unique()
    appList = {}
    for i in maqs:
        appList[i] = []
        for a in range(len(df_list)):
            if i == df_list[a][2]:
                appList[i].append(df_list[a][1])
    # for i in appList['A001']:
    #     print(i)
    # print(appList['A001'])
    return appList


def app(maquina, terminal, con):
    cur = con.cursor()
    res = cur.execute(
        """
                SELECT * FROM applicadores WHERE maquina = ? and app = ?;
                """,
        (maquina, terminal[0:10]),
    )
    res = res.fetchall()
    if res:
        return True
    else:
        return False


def specificStatus(corte, con):
    d_corte = corte.to_dict("list")
    d_corte["appAutoL"] = []
    for i in range(len(d_corte["Maquina"])):
        maquina = d_corte["Maquina"][i]
        terminal = d_corte["TMNL_L(Auto)"][i]
        # if terminal != "":
        #     if d_corte["Maquina"][i] != "SLD1":
        #         if app(maquina, terminal, con):
        #             d_corte["appAutoL"].append("ok")
        #         else:
        #             d_corte["appAutoL"].append("err")
        #     else:
        #         d_corte["appAutoL"].append("n/a")
        # else:
        #     d_corte["appAutoL"].append("ok")
        if terminal == '':
            d_corte["appAutoL"].append('')
        else:
            if app(maquina, terminal, con):
                d_corte["appAutoL"].append("ok")
            else:
                d_corte["appAutoL"].append("err")

    d_corte["appAutoR"] = []
    for i in range(len(d_corte["Maquina"])):
        maquina = d_corte["Maquina"][i]
        terminal = d_corte["TMNL_R(Auto)"][i][0:10]
        # if terminal != "":
        #     if d_corte["Maquina"][i] != "SLD1":
        #         if app(maquina, terminal, con):
        #             d_corte["appAutoR"].append("ok")
        #         else:
        #             d_corte["appAutoR"].append("err")
        #     else:
        #         d_corte["appAutoR"].append("n/a")
        # else:
        #     d_corte["appAutoR"].append("ok")
        if terminal == '':
            d_corte["appAutoR"].append('')
        else:
            if app(maquina, terminal, con):
                d_corte["appAutoR"].append("ok")
            else:
                d_corte["appAutoR"].append("err")

    o_corte = pd.DataFrame.from_dict(d_corte)
    return o_corte
