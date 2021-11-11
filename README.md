# Serviço de Log

#### Funcionalidade 

Esse serviço será responsável para guardar logs no banco de dados e também retorna-los via Api Rest


## Como rodar

### *Linux*

**Máquina Virtual**

- Para instalar a Virtualenv, basta executar:

```
$ pip3 install virtualenv
```

- Para criar a Virtualenv do projeto, execute:

```
$ virtualenv -p python3 venv
```

- Para iniciar a Virtualenv:
```
$ source venv/bin/activate
```

- Instale as dependências do projeto:
```
$ venv/bin/pip3 install -r requirements.txt
```

- Agora rode o projeto:
```
$ python3 server.py
```

---



**Windows**

**Máquina Virtual**

- Para instalar a Virtualenv, basta executar:

```
pip3 install virtualenv
```

- Para criar a Virtualenv do projeto, execute:

```
virtualenv -p python3 venv
```

- Para iniciar a Virtualenv:
```
cd venv/Scripts/activate
```

- Instale as dependências do projeto:
```
cd ../..
pip3 install -r requirements.txt
```

- Agora rode o projeto:
```
$ python3 server.py
```


Acesse http://127.0.0.1:5005/

## Segue o Vídeo abaixo com a demosntração da execução do projeto
https://www.loom.com/share/f7a72762581143268b1f05d28b683985
