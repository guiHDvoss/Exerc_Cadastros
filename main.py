from contato import Contato
from tarefa import Tarefa
from agenda import Agenda

class Main:

    def __init__(self):
        self.contatos = []
        self.tarefas = []
        self.agenda = []

    def v_principal(self):
        resposta = 0
        while (resposta != 99):
            print("Menu de opções")
            print("-----------------------")
            print("-Cadastrar contato = 1")
            print("-Listar contatos = 2")
            print("-Excluir contato = 3")
            print("-Criar tarefa = 4")
            print("-Listar tarefas = 5")
            print("-Excluir tarefa = 6")
            print("-Sair = 99")
            print("-----------------------")
            resposta = input("Escolha a opção desejada")


            if(resposta == "1"):
                self.v_cadastrar_contato()
            elif(resposta == "2"):
                self.v_listar_contatos()
            elif(resposta == "3"):
                self.v_excluir_contato()
            elif(resposta == "4"):
                self.v_cadastrar_tarefa()
            elif(resposta == "5"):
                self.v_listar_tarefas()
            elif(resposta == "6"):
                self.v_excluir_tarefa()
            elif(resposta  == "99"):
                print("Programa encerrado")
                return

    def v_cadastrar_contato(self):
        cpf = input("Informe seu CPF")
        nome = input("informe o nome")
        email = input("informe o email")
        contato_informado = Contato(cpf, nome, email)
        self.contatos.append(contato_informado)

    def v_listar_contatos(self):
        for i in self.contatos:
            print("CPF: " + str(i.getCpf()))
            print('Nome: ' + str(i.getNome()))
            print('Email: ' + str(i.getEmail()))
            print("------------------------------")

    def v_excluir_contato(self):
        cpf = input("Qual CPF deseja excluir?")
        for i in self.contatos:
            if(i.getCpf() == cpf):
                print("Excluíndo " + i.getNome())
                self.contatos.remove(i)
                print("Excluído com sucesso")

    def v_cadastrar_tarefa(self):
        descricao = input("Informe a tarefa")
        status = False
        tarefa_informada = Tarefa(descricao, status)
        self.tarefas.append(tarefa_informada)

    def v_listar_tarefas(self):
        id = -1
        for i in self.tarefas:
            id = id + 1
            print("ID: " + str(id))
            print('Tarefa: ' + str(i.getDescricao()))
            print('Status: ' + str(i.getStatus()))
            print("------------------------------")

    def v_excluir_tarefa(self):
        id = input("Qual Id deseja excluir?")
        posicao = -1
        for i in self.tarefas:
            posicao = posicao + 1
            if(str(posicao) == id):
                print("Excluíndo " + i.getDescricao())
                self.tarefas.remove(i)
                print("Excluído com sucesso")



Main().v_principal()
