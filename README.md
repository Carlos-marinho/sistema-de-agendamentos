# Sistema de Agendamentos com Flask

Este projeto é um sistema de agendamento desenvolvido com Flask, que permite criar, editar, excluir e listar agendamentos. O sistema utiliza as melhores práticas de desenvolvimento com o uso do Factory Pattern, Blueprints e uma arquitetura modularizada.

## Funcionalidades

- **Criação de Agendamentos:** Registre novos agendamentos com data, horário, cliente e serviço.
- **Edição de Agendamentos:** Atualize informações dos agendamentos já cadastrados.
- **Exclusão de Agendamentos:** Remova agendamentos indesejados.
- **Listagem e Filtro:** Visualize os agendamentos com opções de filtragem por data, cliente e serviço.
- **Templates Reutilizáveis:** Estrutura de HTML e CSS padronizados para uma interface consistente.


## Requisitos

- Python 3.8 ou superior
  

## Instalação e Configuração

### 1. Clone o Repositório

No terminal, execute:
```bash
git clone https://github.com/Carlos-marinho/sistema-de-agendamentos
cd sistema-de-agendamentos
```

### 2. Crie e Ative um Ambiente Virtual
Linux/MacOS:
```
python3 -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as Dependências
```
pip install -r requirements.txt
```

### 4. Configuração do Banco de Dados
O projeto utiliza SQLite para armazenamento de dados. O arquivo de banco de dados (agendamento.db) será criado automaticamente quando a aplicação for iniciada.

### 5. Executando a Aplicação
Com o ambiente virtual ativado, inicie a aplicação executando:

```
python run.py
```

Acesse a aplicação em:

http://127.0.0.1:5000

### 6. Executando os Testes
Para rodar os testes unitários:

```
pytest -v --disable-warnings
```
