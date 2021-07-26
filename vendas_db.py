import os
import pathlib
import sqlite3
from banco import Query,SingletonMeta

class DatabaseVenda(Query, metaclass=SingletonMeta):

    def __init__(self):

        self._db_path = pathlib.Path(__file__).parent.absolute()
        self._db_path = os.path.join(self._db_path, "vendas.db")

        if not os.path.isfile(self.get_caminho_db):
            conn = sqlite3.connect(self.get_caminho_db)
            exec = conn.cursor()
            exec.execute(super().criar_tabela())

    @property
    def get_caminho_db(self):
        return self._db_path

    def get_venda(self):
        conn = sqlite3.connect(self.get_caminho_db)
        exec = conn.cursor()
        exec.execute(super().obter_dados())
        dados = []
        for venda in exec.fetchall():
            dados.append(venda)
        return dados

    def salvar_venda(self, codigo, nome, qtd, preco, tipo, genero):
        conn = sqlite3.connect(self.get_caminho_db)
        exec = conn.cursor()
        exec.execute(super().salvar(), (codigo, nome, qtd, preco, tipo, genero))
        conn.commit()
