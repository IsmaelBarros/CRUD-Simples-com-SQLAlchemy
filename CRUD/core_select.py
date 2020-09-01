from pprint import pprint
from core import user_table
from sqlalchemy import select

s = select([user_table])

for row in s.execute():
    pprint(row)
