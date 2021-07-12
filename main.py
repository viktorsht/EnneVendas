import os
import pathlib

from estoque_db import DatabaseEstoque
from loja import Loja
from mensagem import Mensagens
from senha import Senha

if __name__ == "__main__":

    msg = Mensagens()
    s = Senha()
    loja = Loja()

    path = pathlib.Path(__file__).parent.absolute()
    path = os.path.join(path, "arquivo.json")

    if not os.path.isfile(path):
        msg.welcome()
        senha = input("[ Cadastre uma senha para o programa ]: ")
        s.criar_arquivo_senha_json(senha)

    menu = "1"
    while menu == "1":

        msg.welcome()
        msg.dashboard()

        op = input("[ X ]: ")

        loja.abrir_loja()

        if op == "0":
            msg.sair_programa()

        elif op == "1":
            senha = input("[ Senha Obrigatória ]: ")
            if(s.validar_senha(senha) == True):
                print()
                loja.adcionar_cosmetico()
            else:
                print(msg.senha_invalida())

        elif op == "2":
            loja.mostrar_estoque()

        elif op == "3":
            senha = input("[ Senha Obrigatória ]: ")
            if(s.validar_senha(senha) == True):
                print()
                loja.atualizar_cosmeticos()
            else:
                print(msg.senha_invalida())

        elif op == "4":
            loja.mostrar_vendas()

        elif op == "5":
            senha = input("[ Senha Obrigatória ]: ")
            if(s.validar_senha(senha) == True):
                print()
                loja.registro_venda()
            else:
                print(msg.senha_invalida())

        elif op == "6":

            senha_antiga = input("[ Senha Atual ]: ")
            if(s.validar_senha(senha_antiga) == True):
                print()
                senha_nova = input("[ Nova Senha ]: ")
                while(senha_antiga == senha_nova):
                    print(msg.nova_senha_invalida())
                    senha_nova = input("[ Nova Senha ]: ")
                    print()
                s.criar_arquivo_senha_json(senha_nova)
                print(msg.msg_atualizar())
            else:
                print(msg.senha_invalida())

        else:
            print(loja.m.invalida())

        msg.voltar_menu()
        menu = input("[ VOLTAR AO MENU ]: ")

        while(menu != "1"):
            print(msg.invalida())
            menu = input("[ VOLTAR AO MENU ]: ")
