class ContaBancaria:
    def __init__ (self, numero, nome, tipo):
        self.numero = numero
        self.n = nome
        self.tipo = tipo
        self.saldo = 0
        self.status = False
        self.limite = 0

    def ativar(self):
        if self.status == False:
            print ("Conta ativada! ")
            self.status = True
        else:
            print ("A conta já está ativada.")

    def depositar(self, deposito):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        else:
            print(f"valor depositado: {deposito}")
            self.saldo += deposito


    def sacar(self, saque):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        elif (self.saldo + self.limite) < saque:
            print(f"Saque indisponível. Valor disponível: {self.saldo}")
        else:
            print (f"{self.n} sacou {saque} reais")
            self.saldo -= saque

    def consulta(self):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        else:
            print (f"Seu saldo é {self.saldo}")

    def criarLimite(self, novolimite):
        self.limite += novolimite
        print (f"Seu novo limite é {self.limite}")

class ToDoList:
    def __init__(self):
        self.lista=[
    "Estudar Python por 1 hora",
    "Organizar a mesa de trabalho",
    "Responder e-mails importantes",
    "Fazer 30 minutos de caminhada",
    "Ler um capítulo de um livro"
        ]
        self.menu = 0

    def iniciandoMenu(self):
        print("Sejá bem vindo a To Do List \n")
        self.menu = int(input("1-Visualizar a lista\n2-Inserir um intem na lista\n3-deletar um item na lista\n4- sair\nDigite um dos números: "))

        while True:
            try:
                if self.menu == 1:
                    self.visualizar()
                    break
                elif self.menu == 2:
                    self.inserir()
                    break
                elif self.menu == 3:
                    self.deletar()
                    break
                elif self.menu == 4:
                    print("Saindo da operação")
                    break
                else:
                    print("Digite um Número entre 1-4")
                    self.menu = int(input("Digite novamente:"))
            except ValueError:
                print("Digite um Número entre 1-4")
                self.menu = int(input("Digite novamente:"))

    def visualizar(self):
        for i, item in enumerate(self.lista, start=1):
            print(f"{i} - {item}")
        self.retornar()
    def inserir(self):
        item = input("Escreva a nova tarefa: ")
        self.lista.append(item)
        self.retornar()
    def deletar(self):
        delt = int(input("Digite o numero da tarefa que deseja deletar: "))
        delt -= 1
        x = len(self.lista)
        if delt <= x:
            self.lista.pop(delt)
        else:
            print("não existe esse item na lista")
            self.retornar()

        self.retornar()
    def retornar(self):
        resposta = input(" Deseja voltar pro menu? (s/n)")
        while True:
            try:
                if resposta == "s":
                    self.iniciandoMenu()
                    break
                elif resposta == "n":
                    print("Tchau Tchau")
                    break
                else:
                    print("Digite apenas s ou n")
                    resposta = input(" Deseja voltar pro menu? (s/n)")
            except ValueError:
                print("Digite apenas s ou n")
                resposta = input(" Deseja voltar pro menu? (s/n)")
