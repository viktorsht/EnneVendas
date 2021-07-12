from produto import Produto
from vendas_db import DatabaseVenda

class Vendas(Produto):

    def set_venda(self,codigo, nome, quant, preco,tipo,genero):

        if self._codigo is None:
            self._nome = nome
            self._codigo = codigo
            self._qtd = quant
            self._preco = preco
            self._tipo = tipo
            self._genero = genero
        try:
            self.db_salvar_venda(codigo, nome , quant, preco, tipo, genero)
        except:
            pass

    def db_salvar_venda(self, codigo, nome, qtd, preco,tipo,genero):
        db = DatabaseVenda()
        db.salvar_venda(codigo, nome, qtd, preco,tipo,genero)
