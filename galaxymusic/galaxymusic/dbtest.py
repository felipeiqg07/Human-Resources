import getpass

import oracledb

un = 'ADMIN'
cs = 'tcps://adb.sa-santiago-1.oraclecloud.com:1522/g3e3e35c1f9d6b9_pruebasruby21014_low.adb.oraclecloud.com?wallet_location=G:\Oracle\network\admin&retry_count=20&retry_delay=3'

pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)