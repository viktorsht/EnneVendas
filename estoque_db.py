import os
import pathlib
import sqlite3
from banco import Query,SingletonMeta

class DatabaseEstoque(Query, metaclass=SingletonMeta):

    def __init__(self):

        self._db_path = pathlib.Path(__file__).parent.absolute()
        self._db_path = os.path.join(self._db_path, "dados.db")

        if not os.path.isfile(self.get_caminho_db):
            conn = sqlite3.connect(self.get_caminho_db)
            exec = conn.cursor()
            exec.execute(super().query_criar_tabela())

    @property
    def get_caminho_db(self):
        return self._db_path

    def get_cosmeticos(self):
        conn = sqlite3.connect(self.get_caminho_db)
        exec = conn.cursor()
        exec.execute(super().query_obter_dados())
        dados = []
        for produto in exec.fetchall():
            dados.append(produto)
        return dados

    def salvar(self, codigo, nome, qtd, preco, tipo, genero):
        conn = sqlite3.connect(self.get_caminho_db)
        exec = conn.cursor()
        exec.execute(super().query_salvar(), (codigo, nome, qtd, preco, tipo, genero))
        conn.commit()

    def atualizar(self, qtd, nome, preco,tipo,genero, codigo):
        conn = sqlite3.connect(self.get_caminho_db)
        exec = conn.cursor()
        exec.execute(super().query_atualizar(), (qtd, nome, preco, tipo, genero, codigo))
        conn.commit()
