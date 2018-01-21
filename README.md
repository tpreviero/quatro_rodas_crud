# Desafio Grupo Abril CRUD

## Procedimentos
### Clone o repositório

```console
git clone git@github.com:tpreviero/quatro_rodas_crud.git code
cd code
```

### Crie um virtualenv com Python 3.6 e ative
```console
virtualenv .env -p python3
source .env/bin/activate
```

### Dependências
```console
pip install -r requirements.txt
```

### Subindo banco
```console
./manage.py migrate
```

### Rodar o servidor
```console
./manage.py runserver
```

### Acesso
```console
Usuário: admin
Senha: admin123
```

### Produção
https://quatrorodascrud.herokuapp.com/admin/

### Local
http://127.0.0.1:8000/admin/
