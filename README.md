# How to use it
## Setting up
call to the 'set_settings' method

then use the Base, ENGINE and SESSION_MAKER in models as you need

## Alembic cmds

```alembic init alembic```

```alembic upgrade head```

```alembic revision --autogenerate -m "migration comment"```

```alembic revision -m "migration comment"```

```alembic downgrade```

for more alembic cmds [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

