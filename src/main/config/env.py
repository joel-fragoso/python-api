from dotenv import dotenv_values

env = {"database_url": dotenv_values(".env.DATABASE_URL") or ""}
