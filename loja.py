from produto import Produto
from estoque_db import DatabaseEstoque
from vendas_db import DatabaseVenda
from mensagem import Mensagens
from vendas import Vendas

class Loja:
    def __init__(self):
        self._estoque = {}
        self._venda = {}
        self.m = Mensagens()
        self.count = 0

    def abrir_loja(self):
        self.salvar_cosmeticos_bd()
        self.salvar_venda()

    def salvar_cosmeticos_bd(self):
        db = DatabaseEstoque()
        dados = db.get_cosmeticos()

        for prod in dados:
            produto = Produto()
            produto.set_produto(prod[0], prod[1], prod[2], prod[3],prod[4],prod[5])
            self._estoque[prod[0]] = produto

    def salvar_venda(self):
        v = DatabaseVenda()
        dados_vendas = v.get_venda()
        k = 0
        for i in dados_vendas:
            vendido = Vendas()
            vendido.set_venda(i[0],i[1],i[2],i[3],i[4],i[5])
            self._venda[k] = vendido
            k += 1

    def adcionar_venda(self,codigo,cosmetico,quantidade,preco,tipo,genero):
        vendido = Vendas()
        vendido.set_venda(codigo,cosmetico,quantidade,preco,tipo,genero)
        self._venda[self.count] = vendido
        self.count += 1

    def le_quantidade(self):
        tf = False
        try:
            q = input("[ Quantidade ]: ")
        except :
            pass
        while tf == False:
            try:
                q = int(q)
                if(q >= 0):
                    tf = True
                else:
                    print(self.m.inteiro_entrada())
                    q = input("[ Quantidade ]: ")
            except ValueError:
                print(self.m.inteiro_entrada())
                q = input("[ Quantidade ]: ")
        return q

    def le_preco(self):
        tf = False
        try:
            q = input("[ Preço ]: ")
        except :
            pass
        while tf == False:
            try:
                q = float(q)
                if(q >= 0.0):
                    tf = True
                else:
                    print(self.m.float_entrada())
                    q = input("[ Preço ]: ")
            except ValueError:
                print(self.m.float_entrada())
                q = input("[ Preço ]: ")
        return q

    def adcionar_cosmetico(self):
        codigo = input("[ Codigo produto ]: ")

        if codigo not in self._estoque:
            cosmetico = input("[ Nome ]: ")
            quantidade = self.le_quantidade()
            preco = self.le_preco()
            tipo = input("[ Tipo ]: ")
            genero = input("[ Gênero ]: ")
            produto = Produto()
            produto.set_produto(codigo, cosmetico, quantidade, preco, tipo, genero)
            self._estoque[codigo] = produto
        else:
            print(self.m.produto_cadastrado_msg())

    def mostrar_vendas(self):
        i = 1
        for v in self._venda.values():
            print(f"        VENDA = {i}")
            print("------------------------------------------------------------")
            print(f"        Codigo: {v.get_codigo}")
            print(f"        Nome: {v.get_nome}")
            print(f"        Preço: {v.get_preco}")
            print(f"        Quantidade: {v.get_qtd}")
            print(f"        Tipo: {v.get_tipo}")
            print(f"        Genero: {v.get_genero}")
            print("----------------------------------------------------------\n")
            i += 1

    def mostrar_estoque(self):
        for cosmetico in self._estoque.values():
            print("------------------------------------------------------------")
            print(f"        Codigo: {cosmetico.get_codigo}")
            print(f"        Nome: {cosmetico.get_nome}")
            print(f"        Preço: {cosmetico.get_preco}")
            print(f"        Quantidade estoque: {cosmetico.get_qtd}")
            print(f"        Tipo: {cosmetico.get_tipo}")
            print(f"        Genero: {cosmetico.get_genero}")
            print("----------------------------------------------------------\n")

    def atualizar_cosmeticos(self):
        codigo = input("[ Codigo produto ]: ")

        if codigo in self._estoque:

            self.m.dashboard_atualizacao() #printa menu de atualizações

            op = input("[ x ]: ")

            if op == "1":
                nome = input("[ Produto ]: ")
                self._estoque[codigo].atualizar_nome(nome)

            elif op == "2":
                quantidade = self.le_quantidade()
                self._estoque[codigo].atualizar_qtd(quantidade)

            elif op == "3":
                preco = self.le_preco()
                self._estoque[codigo].atualizar_preco(preco)


            elif op == "4":
                tipo = input("[ Tipo ]: ")
                self._estoque[codigo].atualizar_tipo(tipo)

            elif op == "5":
                genero = input("[ Gênero ]: ")
                self._estoque[codigo].atualizar_genero(genero)

            print(self.m.msg_atualizar())
        else:
            print(self.m.not_found_msg())


    def registro_venda(self):
        #self.salvar_venda()
        c = input("[ Codigo produto ]: ")

        if c in self._estoque:

            if self._estoque[c].get_qtd > 0:
                qtd = self.le_quantidade()

                if(qtd <= self._estoque[c].get_qtd):
                    self.adcionar_venda(c,self._estoque[c].get_nome,qtd,self._estoque[c].get_preco,self._estoque[c].get_tipo,self._estoque[c].get_genero)
                    self._estoque[c].decrementar_qtd(qtd)
                    print(self.m.venda_realizada())
                else:
                    print(self.m.venda_impossibilitada())
                if self._estoque[c].get_qtd == 0:
                    print(self.m.reposicao_produto())

            else:
                print('\n'+self.m.reposicao_produto())
        else:
            print(self.m.not_found_msg())
