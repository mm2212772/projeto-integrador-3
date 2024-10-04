# Projeto Integrador em Computação II

Código fonte do *software* apresentado na disciplina de Projeto Integrador II
para o curso de Bacharelado em Tecnologia da Informação da Universidade Virtual
do Estado de São Paulo (UNIVESP).

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes itens instalados em seu sistema:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Passo 1: Clonar o Repositório

1. Abra o terminal (ou prompt de comando).
2. Navegue até o diretório onde deseja clonar o repositório.
3. Use o comando abaixo para clonar o repositório:
```bash
git clone https://github.com/mm2212772/projeto-integrador-2.git
```
4. Navegue para o diretório do projeto:

```bash

cd projeto-integrador-2
```

## Passo 2: Criar um Ambiente Virtual

É recomendável criar um ambiente virtual para isolar as dependências do projeto.

1. Crie um ambiente virtual:
```bash
python3 -m venv env
```
2. Ative o ambiente virtual:
- No Windows:
```bash
.\env\Scripts\activate
```
- No macOS/Linux:
```bash
source env/bin/activate
```
### Passo 3: Instalar Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
### Passo 4: Configurar o Banco de Dados

Aplique as migrações:
```bash
python manage.py migrate
```
### Passo 5: Executar o Servidor

Por fim, inicie o servidor de desenvolvimento do Django:
```bash
python manage.py runserver
```
Agora você pode acessar o projeto no seu navegador em http://127.0.0.1:8000/.
