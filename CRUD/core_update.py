from sqlalchemy import update
from core import user_table, engine

conn = engine.connect()

u = update(user_table).where(user_table.c.nome == 'Ismael de Sousa Barros')
#u = u.values(nome='Ismael de Sousa Barros')

u = u.values(idade=(user_table.c.idade - 2))

result = conn.execute(u)

print(result.rowcount)
