from interface import Interface
import os.path

class Senha(Interface):

    def criar_arquivo_senha_json(self,senha):
        arquivo = open("arquivo.json","w")
        arquivo.write(senha)
        arquivo.close()

    def validar_senha(self,senha_verificacao):
        nome_arquivo = "arquivo.json"
        ok = False
        try:
            if(os.path.isfile(nome_arquivo)):
                arquivo = open(nome_arquivo, "r")
                senha = arquivo.read()
                if(senha_verificacao == senha):
                    ok = True
                arquivo.close()
        except:
            print("O arquivo não existe")
        return ok
