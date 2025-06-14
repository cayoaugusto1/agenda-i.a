import json
from datetime import datetime, timedelta

class Tarefa:
    def __init__(self, titulo, descricao, prazo, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        # prazo é string no formato 'YYYY-MM-DD'
        self.prazo = datetime.strptime(prazo, "%Y-%m-%d")
        self.prioridade = prioridade  # 1 (alta) a 5 (baixa)
        self.criada_em = datetime.now()
        self.concluida = False

    def __repr__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.titulo} | Prazo: {self.prazo.date()} | Prioridade: {self.prioridade} | {status}"

class Agenda:
    def __init__(self, arquivo="agenda.json"):
        self.arquivo = arquivo
        self.tarefas = []
        self.carregar()

    def carregar(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa(**t) for t in dados]
        except FileNotFoundError:
            self.tarefas = []

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([t.__dict__ for t in self.tarefas], f, default=str, indent=4)

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        self.salvar()

    def listar_tarefas(self, mostrar_todas=True):
        if mostrar_todas:
            for i, t in enumerate(self.tarefas, 1):
                print(f"{i}. {t}")
        else:
            pendentes = [t for t in self.tarefas if not t.concluida]
            for i, t in enumerate(pendentes, 1):
                print(f"{i}. {t}")

    def concluir_tarefa(self, indice):
        try:
            self.tarefas[indice-1].concluida = True
            self.salvar()
            print("Tarefa concluída com sucesso.")
        except IndexError:
            print("Índice inválido.")

    def sugerir_proxima(self):
        # Sugere tarefa com maior prioridade e prazo mais próximo
        pendentes = [t for t in self.tarefas if not t.concluida]
        if not pendentes:
            print("Nenhuma tarefa pendente!")
            return
        pendentes.sort(key=lambda t: (t.prioridade, t.prazo))
        proxima = pendentes[0]
        print("Tarefa sugerida para fazer agora:")
        print(proxima)

def menu():
    agenda = Agenda()
    while True:
        print("\n=== Agenda Inteligente ===")
        print("1. Adicionar tarefa")
        print("2. Listar todas tarefas")
        print("3. Listar tarefas pendentes")
        print("4. Concluir tarefa")
        print("5. Sugerir próxima tarefa")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            prazo = input("Prazo (AAAA-MM-DD): ")
            prioridade = int(input("Prioridade (1=Alta, 5=Baixa): "))
            tarefa = Tarefa(titulo, descricao, prazo, prioridade)
            agenda.adicionar_tarefa(tarefa)
            print("Tarefa adicionada!")
        elif escolha == "2":
            agenda.listar_tarefas()
        elif escolha == "3":
            agenda.listar_tarefas(mostrar_todas=False)
        elif escolha == "4":
            agenda.listar_tarefas(mostrar_todas=False)
            i = int(input("Número da tarefa para concluir: "))
            agenda.concluir_tarefa(i)
        elif escolha == "5":
            agenda.sugerir_proxima()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()