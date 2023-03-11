
def trim_auto(df):
    columns = [2, 8, 9, 21, 22]
    df.drop(df.columns[columns], axis=1, inplace=True)
    df = df.fillna('')
    df.rename(columns={'TMNL_L(Semi-auto).1':'TMNL_R(Semi-auto)'}, inplace=True)
    # print(df.columns)
    df.to_excel('corte.xlsx', index=False)
    return df



def apps(df):
    columns = [2, 4, 5, 6, 7, 8]
    df.drop(df.columns[columns], axis=1, inplace=True)
    df_list = df.values.tolist()
    df.sort_values(by=['Almacen'], inplace=True)
    maqs = df['Almacen'].unique()
    appList = {} 
    for i in maqs:
        appList[i] = []
        for a in range(len(df_list)):
            if i == df_list[a][2]:
                appList[i].append(df_list[a][:-1])
    # for i in appList['A001']:
    #     print(i)
    return appList

def specificStatus(corte, aplicadores):
    corte = corte.to_dict('list')
    for i in corte:
        print(i)

