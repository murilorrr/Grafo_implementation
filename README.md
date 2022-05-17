# 🎉 Boas vindas ao meu repositório
#### Este repositório esta sendo implementado para o estudo de grafos como estrutura de dados.

## 🤝 Caso queira contribuir:
Todos os tipos de contribuições são muito bem vindas

- ⭐️ Estrelando o projeto
- 🐛 Achando e reportando bugs
- 📥 Submição de PR e adição de novas features


## iniciando o desenvolvimento:

### Pre-requisites

- _Python:_ `3.7` or higher.
- _Pip:_ `21.2` or higher.
- _Git:_ `2.25.1` or higher.

Para executar os testes, lembre-se de primeiro criar e ativar o ambiente virtual, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

``` bash
python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r dev-requirements.txt
```
O arquivo requirements.txt contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um package.json de um projeto Node.js.

Executando testes:
```bash
pytest ./
```

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:
```bash
python3 -m flake8
```