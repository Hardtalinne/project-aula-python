# Atividade Api em Python - Animais

Projeto Api em Python utilizando o fastApi para desenvolver conceitos basicos.

Obs.: Na raiz do projeto possui um arquivo example.json que pode ser usado para realizar testes.

## Dependências

Utilize o pip para baixar as dependências do projeto:

```
pip install -r requirements.txt
```

## Execução

Para executar use:

```
uvicorn main:app --reload 
```

Para gerar um arquivo SQLite com a tabela de animais execute  o arquivo cria_tabelas.py  

```
python3 cria_tabelas.py    
```

## Testes

Para executar os testes use:

```
pytest tests/
```

Para consultar a documentação da API, acesse http://localhost:8000/docs e para interomper a execução pressione «Ctrl»+«C».