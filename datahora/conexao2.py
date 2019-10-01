# import cx_Oracle
import time

def convert(mes):
    if mes == 'janeiro':
        return 'jan'
    elif mes == 'fevereiro':
        return 'feb'
    elif mes == 'marco':
        return 'mar'
    elif mes == 'abril':
        return 'apr'
    elif mes == 'maio':
        return 'may'
    elif mes == 'junho':
        return 'jun'
    elif mes == 'julho':
        return 'jul'
    elif mes == 'agosto':
        return 'aug'
    elif mes == 'setembro':
        return 'sep'
    elif mes == 'outubro':
        return 'oct'
    elif mes == 'novembro':
        return 'nov'
    elif mes == 'dezembro':
        return 'dec'


def conecta(nota, data):
    uid="VILLE24"
    pwd="wt2ville24"
    db="(DESCRIPTION =(ADDRESS_LIST =(ADDRESS =(PROTOCOL = TCP)(Host = 192.168.15.244)(Port = 1521)))(CONNECT_DATA = (SID = WINT) ))"  # string de conexão do Oracle, configurado no


    connection=cx_Oracle.connect(uid + "/" + pwd + "@" + db)
    cursor=connection.cursor()

    # cursor.execute("select caixa,dtentrega from pcnfsaid where numnota=21018 and  dtsaida='17-sep-2019'")
    cursor.execute(f"select caixa,dtentrega from pcnfsaid where numnota={nota} and dtsaida='{data}'")
    result=cursor.fetchone()
    return result


