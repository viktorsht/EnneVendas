from estoque_db import DatabaseEstoque

class Produto():
    def __init__(self):
        self._nome = None
        self._codigo = None
        self._qtd = None
        self._preco = None
        self._tipo = None
        self._genero = None

    def set_produto(self,codigo, nome, quant, preco,tipo,genero):
        if self._codigo is None:
            self._nome = nome
            self._codigo = codigo
            self._qtd = quant
            self._preco = preco
            self._tipo = tipo
            self._genero = genero

            try:
                self.db_salvar(codigo, nome , quant, preco, tipo, genero)
            except:
                pass

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_codigo(self):
        return self._codigo

    @property
    def get_qtd(self):
        return self._qtd

    @property
    def get_preco(self):
        return self._preco

    @property
    def get_tipo(self):
        return self._tipo

    @property
    def get_genero(self):
        return self._genero

    def decrementar_qtd(self, qtd):
        self._qtd -= qtd
        self.db_atualizar()

    def atualizar_preco(self, novo_preco):
        self._preco = novo_preco
        self.db_atualizar()

    def atualizar_nome(self, nome):
        self._nome = nome
        self.db_atualizar()

    def atualizar_qtd(self, qtd):
        self._qtd = qtd
        self.db_atualizar()

    def atualizar_tipo(self,tipo):
        self._tipo = tipo
        self.db_atualizar()

    def atualizar_genero(self,genero):
        self._genero = genero
        self.db_atualizar()

    def db_salvar(self, codigo, nome, qtd, preco,tipo,genero):
        db = DatabaseEstoque()
        db.salvar(codigo, nome, qtd, preco,tipo,genero)

    def db_atualizar(self):
        db = DatabaseEstoque()
        db.atualizar(self.get_qtd, self.get_nome, self.get_preco,self.get_tipo,self.get_genero,self.get_codigo)
