from core import user_table, engine

conn = engine.connect()

ins = user_table.insert()

# new_user = ins.values(nome='Ismael',
#                       idade=34,
#                       senha='123456')

# # conn.execute(new_user)

conn.execute(user_table.insert(), [
    {'nome': 'Maira', 'idade': 32, 'senha': 'xuzinha20'},
    {'nome': 'Isabel', 'idade': 25, 'senha': 'bel2020'},
    {'nome': 'Christian', 'idade': 29, 'senha': 'cristo29'},
    {'nome': 'Daniel', 'idade': 33, 'senha': 'danimore12'},
    {'nome': 'jaqueline', 'idade': 30, 'senha': 'jaquesilveira'},
])
