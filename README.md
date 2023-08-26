# AIFlow Twitter Dados

Este repositório contém dados coletados do Twitter para serem usados no projeto AIFlow. O projeto tem como objetivo explorar e analisar tendências e padrões de tweets relacionados a um determinado tópico, utilizando o Python 3.11 e o Apache Airflow 2.6.3.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados antes de prosseguir:

- Python 3.11: [Download](https://www.python.org/downloads/release/python-311/)
- Apache Airflow 2.6.3: Você pode instalá-lo usando o seguinte comando:
  ```bash
  pip install apache-airflow==2.6.3
  ```

## Configuração do Ambiente Virtual

Recomendamos criar um ambiente virtual para isolar as dependências deste projeto. Siga as etapas abaixo para criar o ambiente virtual e configurá-lo:

1. Navegue até o diretório do projeto:

```bash
cd aiflow_twitter_dados
```

2. Crie um ambiente virtual com Python 3.11 (certifique-se de ter o `venv` instalado):

```bash
python3.11 -m venv venv
```

3. Ative o ambiente virtual:

- No Linux ou macOS:

```bash
source venv/bin/activate
```

- No Windows:

```bash
venv\Scripts\activate
```

4. Instale as dependências do projeto, incluindo o Apache Airflow 2.6.3:

```bash
pip install apache-airflow==2.6.3
```

## Como Usar

Após configurar o ambiente virtual, você pode executar seus scripts ou análises usando os arquivos de dados fornecidos.

## Conjunto de Dados

Os conjuntos de dados são arquivos CSV contendo tweets coletados usando a API do Twitter. Cada arquivo contém as seguintes colunas principais:

- `id`: ID único do tweet.
- `texto`: O texto do tweet.
- `data_criacao`: A data de criação do tweet.
- ...

## Contribuindo

Se você deseja contribuir para este projeto, siga estas etapas:

1. Fork este repositório.
2. Crie uma nova branch para sua contribuição:
```bash
git checkout -b sua-feature
```
3. Faça suas alterações e commit:
```bash
git commit -m "Adicionar nova feature"
```
4. Envie suas alterações para o seu repositório fork:
```bash
git push origin sua-feature
```
5. Abra um pull request neste repositório.
