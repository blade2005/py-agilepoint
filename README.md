# py-agilepoint
Python integration for AgilePoint

TODO: Create script to regenerate code

```
from agilpoint import AgilePoint
ap = AgilePoint(host, path, username, password)
db_info = ap.admin.get_database_info()
# Responses in json usually have a primary key indicating what AgilePoint class the response has.
for key, value in db_info['GetDatabaseInfoResult'].items():
    print('{}: {}'.format(key,value))

```
