## Descrição

A classe CustomStack implementa uma pilha com funcionalidades básicas, como push, pop, peek, is_empty e size. Além disso, o projeto inclui a classe NumberAscOrder, que pode ordenar os números armazenados na pilha em ordem ascendente.

## Execução do Projeto

### Utilizando o Terminal:

Siga as instruções abaixo para executar o projeto no seu ambiente local.

#### 1. Criação do Ambiente Virtual:

Abra um terminal na raiz do projeto e execute o seguinte comando para criar um ambiente virtual:

```bash
python -m venv venv
```

### 2 Ativação do Ambiente Virtual:

Ative o ambiente virtual com o comando apropriado para o seu sistema operacional:

#### No Windows:

```bash
.\venv\Scripts\activate
```
#### No MAC:

```bash
source venv/bin/activate
```

### 3. Instalação das Dependências:

Instale as dependências do projeto utilizando o seguinte comando:

```bash
pip install -r requirements.txt
```

### 4. Execução dos Testes e Cobertura:

Execute os testes e obtenha uma cobertura do código com o seguinte comando:

```bash
pytest --cov .\test\
```

### 5. Resultado da Cobertura:

Após a execução dos testes, você verá um resumo da cobertura do código:

| Arquivo                   | Linhas de Código | Linhas Ausentes | Cobertura |
|---------------------------|------------------|-----------------|-----------|
| test\__init__.py          | 0                | 0               | 100%      |
| test\custom_stack_test.py | 55               | 0               | 100%      |
| **Total**                 | **55**           | **0**           | **100%**  |

(Passou em 7)


