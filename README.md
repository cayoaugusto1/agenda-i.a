# Agenda Inteligente com Assistente Virtual

## Descrição

Projeto em Python que funciona como uma agenda para gerenciar tarefas de forma inteligente. Possui funcionalidades para adicionar, listar, concluir tarefas e um assistente que sugere qual tarefa fazer primeiro com base em prazo e prioridade.

## Funcionalidades

- Cadastro, edição e remoção de tarefas com prazos e níveis de prioridade.
- Listagem de todas as tarefas ou apenas as pendentes.
- Conclusão de tarefas pelo número na lista.
- Sugestão automática da próxima tarefa a ser feita, priorizando prazo e urgência.
- Persistência dos dados em arquivo JSON.
- Interface simples via terminal para fácil interação.

## Requisitos

- Python 3.x

## Como usar

1. Clone ou faça download do projeto.
2. No terminal, navegue até a pasta do projeto.
3. Execute o arquivo principal:

   ```bash
   python agenda_inteligente.py
Use o menu para interagir com a agenda.

Estrutura do Código
Tarefa: classe que representa uma tarefa com título, descrição, prazo, prioridade e status.

Agenda: classe que gerencia as tarefas, incluindo salvar e carregar de um arquivo JSON.

Função menu(): interface de texto para interação com o usuário.

Possíveis melhorias
Interface gráfica usando Tkinter ou PyQt.

Integração com banco de dados para maior escalabilidade.

Algoritmos avançados para sugerir tarefas usando IA.

Notificações e alertas via sistema operacional.

Autor
Cayo Augusto- hz-01

Projeto aberto para modificações e melhorias.
