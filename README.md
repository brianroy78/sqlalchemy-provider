# How to use it

## Alembic cmds

```
alembic init alembic
```
```
alembic upgrade head
```
```
alembic revision --autogenerate -m "migration comment"
```
```
alembic revision -m "migration comment"
```
```
alembic downgrade
```

For more alembic cmds [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

## Quick Copy & paste cmds

This must be on the `alembic/env.py` file.
```
from database.tables import Base
```

```
target_metadata = Base.metadata
```

Do not forget to implement the URL setting in the `database/sessions.py` file.

Create a new session by calling `get_session` from `database/sessions.py`