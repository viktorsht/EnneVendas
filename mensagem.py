class Mensagens:
    def __init__(self):

        #mensagens de erro e advertencia
        self.not_found = "\033[41m" + "\nCosmético não encontrado!\n" + "\033[0;0m"
        self.venda_impossivel = "\033[41m" + "\nVENDA NÃO REALIZADA! NÃO HÁ A QUANTIDADE ESTOQUE DISPONÍVEL\n" + "\033[0;0m"
        self.senha_errada = "\033[41m" + "\nSENHA INVÁLIDA!\n" + "\033[0;0m"
        self.entrada_invalida = "\033[41m" + "\nErro! Entrada Invalida\n" + "\033[0;0m"
        self.reposicao = "\033[41m" + "\nPOR FAVOR, REPOR ESTOQUE\n" + "\033[0;0m"
        self.inteiro = "\033[41m" + "\nDIGITE UM NÚMERO INTEIRO!\n" + "\033[0;0m"
        self.float = "\033[41m" + "\nDIGITE UM NÚMERO REAL!\n" + "\033[0;0m"
        self.nova_senha_invalida_msg = "\033[41m" + "\nSENHA ANTERIOR DEDECTADA! DIGITE UMA SENHA DIFERENTE!\n" + "\033[0;0m"

        #mensagens de sucesso!
        self.ok_atualizado = "\033[42m" + "\nAtualização concluída\n" + "\033[0;0m"
        self.produto_vendido = "\033[42m" + "\nVenda realizada com sucesso!\n" + "\033[0;0m"
        self.produto_cadastrado = "\033[31m" + "Produto já cadastrado" + "\033[0;0m"



    def not_found_msg(self):
        return self.not_found

    def venda_impossibilitada(self):
        return self.venda_impossivel

    def senha_invalida(self):
        return self.senha_errada

    def invalida(self):
        return self.entrada_invalida

    def reposicao_produto(self):
        return self.reposicao

    def inteiro_entrada(self):
        return self.inteiro

    def float_entrada(self):
        return self.float

    def nova_senha_invalida(self):
        return self.nova_senha_invalida_msg

    def msg_atualizar(self):
        return self.ok_atualizado

    def venda_realizada(self):
        return self.produto_vendido

    def produto_cadastrado_msg(self):
        return self.produto_cadastrado


    def welcome(self):
            print(
            "\033[35m" +
            '''
                        Welcome!

            ||||||| ||    | ||    | |||||||
            |       | |   | | |   | |
            ||||||| |  |  | |  |  | |||||||
            |       |   | | |   | | |
            ||||||| |    || |    || |||||||

            '''
            + "\033[0;0m"
            )

    def dashboard(self):
        print(
        '''
            [ 0 ] - Sair
            [ 1 ] - Novo produto
            [ 2 ] - Estoque
            [ 3 ] - Atualizar Dados
            [ 4 ] - Dashboard de Vendas
            [ 5 ] - Nova Venda
            [ 6 ] - Nova Senha
        '''
        )

    def dashboard_atualizacao(self):
        print(
        '''
                DASHBOARD DE ATUALIZAÇÃO DE DADOS

            [ 1 ] - Produto
            [ 2 ] - Estoque
            [ 3 ] - Preço
            [ 4 ] - Tipo
            [ 5 ] - Gênero
        '''
        )

    def voltar_menu(self):
        print(
        '''

                    Voltar ao menu?
                [Digite 1 para voltar!]
        '''
        )

    def sair_programa(self):
        print(
        '''
                Deseja Finalizar o programa?
                [Digite 0 para finalizar!]

        '''
        )
        if(input("[ X ]: ") == "0"):
            exit()
