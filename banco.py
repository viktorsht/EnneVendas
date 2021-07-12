import sqlite3
class Query:
    @staticmethod
    def query_criar_tabela():
        return """
                CREATE TABLE IF NOT EXISTS Cosmeticos
                (
                    codigo VARCHAR(15) NOT NULL PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    qtd INTEGER NOT NULL,
                    preco REAL NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    genero VARCHAR(50) NOT NULL
                );
                """

    @staticmethod
    def query_salvar():
        return  """
                INSERT INTO Cosmeticos (codigo, nome,  qtd, preco, tipo, genero)
                VALUES (?, ?, ?, ?, ?, ?)
                """

    @staticmethod
    def query_atualizar():
        return  """
                UPDATE Cosmeticos
                SET qtd = ?, nome = ?, preco = ?,tipo = ?,genero = ?
                WHERE codigo = ?
                """
    @staticmethod
    def query_delete():
        return  """
                DELETE FROM Cosmeticos WHERE codigo = ?
                """

    @staticmethod
    def query_obter_dados():
        return  """
                    SELECT * FROM Cosmeticos
                """

class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instancias:
            instance = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instance
        return cls._instancias[cls]
