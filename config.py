import os


class Config:
    # Em produção, defina SECRET_KEY como variável de ambiente.
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-apenas-para-mensagens-da-aula")
