# 🚀 Django REST Framework Studies

Este repositório apresenta os principais conceitos necessários para construir **APIs profissionais com Django REST Framework**.

---

# 🎯 Objetivo do Material

Este material foi criado para permitir que o estudante:

- entender como funciona uma API
- aprender a arquitetura do Django
- construir APIs completas
- revisar conceitos rapidamente
- ensinar outras pessoas
- entender o fluxo completo de requisições

---

# 🔄 Fluxo de Funcionamento de uma API

Fluxo de uma requisição em **Django REST Framework**

```
CLIENTE (Browser / App / Postman)
        ↓
URL
        ↓
VIEW
        ↓
SERIALIZER
        ↓
MODEL
        ↓
BANCO DE DADOS
```

Depois o fluxo retorna:

```
BANCO DE DADOS
        ↓
MODEL
        ↓
SERIALIZER
        ↓
VIEW
        ↓
RESPOSTA JSON
```

---

# 🌐 Métodos HTTP Utilizados em APIs

| Método | Função |
|------|------|
| GET | Buscar dados |
| POST | Criar dados |
| PUT | Atualizar completamente |
| PATCH | Atualizar parcialmente |
| DELETE | Remover dados |

---

# 📁 Estrutura do Projeto Django

```
project/

├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── cursos/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
```

---

# ⚙ Arquivo `manage.py`

O arquivo **manage.py** executa comandos administrativos do Django.

Com ele podemos:

- iniciar servidor
- aplicar migrations
- criar usuários
- acessar shell do Django

Exemplo de uso:

```bash
python manage.py runserver
python manage.py migrate
```

Exemplo do código:

```python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

---

# ⚙ Arquivo `settings.py`

Arquivo responsável pelas configurações principais do projeto.

Principais configurações:

- banco de dados
- aplicativos instalados
- segurança
- middleware
- autenticação

Exemplo de configuração:

```python
INSTALLED_APPS = [

'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',

'rest_framework',
'rest_framework.authtoken',

'curso'

]
```

---

# 🗄 Arquivo `models.py`

Define as **tabelas do banco de dados**.

Cada classe representa uma tabela.

```python
from django.db import models

class Curso(models.Model):

    titulo = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.titulo
```

Explicação:

- `titulo` → campo de texto
- `url` → campo para links
- `__str__` → representação do objeto no admin

---

# 🔄 Arquivo `serializers.py`

Serializers convertem dados entre:

```
Python → JSON
JSON → Python
```

Exemplo:

```python
from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
```

`ModelSerializer` cria automaticamente os campos com base no model.

---

# 🧠 Arquivo `views.py`

As **views controlam a lógica da API**.

```python
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
```

`ModelViewSet` cria automaticamente:

- GET
- POST
- PUT
- PATCH
- DELETE

---

# 🔗 Arquivo `urls.py`

Responsável por conectar rotas às views.

```python
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet

router = DefaultRouter()

router.register(r'cursos', CursoViewSet)

urlpatterns = router.urls
```

Rotas geradas automaticamente:

```
/cursos/
/cursos/1/
```

---

# 🛠 Arquivo `admin.py`

Registra os models no painel administrativo.

```python
from django.contrib import admin
from .models import Curso

admin.site.register(Curso)
```

Depois disso o model aparecerá no painel:

```
http://127.0.0.1:8000/admin
```

---

# 🔐 Autenticação por Token

Usada para proteger APIs.

Cada usuário recebe um **token único**.

Exemplo de header:

```
Authorization: Token 123456789
```

---

# 🔑 Criando Token Manualmente

Abrir shell:

```bash
python manage.py shell
```

Importar models:

```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
```

Buscar usuário:

```python
orlando = User.objects.get(username="orlando")
```

Criar token:

```python
token, created = Token.objects.get_or_create(user=orlando)

print(token.key)
```

---

# ⚡ Comandos Importantes do Django

Rodar servidor:

```bash
python manage.py runserver
```

Rodar servidor em outra porta:

```bash
python manage.py runserver 8001
```

Criar migrations:

```bash
python manage.py makemigrations
```

Aplicar migrations:

```bash
python manage.py migrate
```

Criar superusuário:

```bash
python manage.py createsuperuser
```

Ativar ambiente virtual:

```bash
.venv\Scripts\activate
```

---

# 🌍 Endpoints de Teste

```
http://127.0.0.1:8000/api/v1/cursos/
http://127.0.0.1:8000/api/v1/avaliacoes/
```

---

# ✅ Checklist Final

✔ Projeto Django criado  
✔ Aplicação criada  
✔ Models criados  
✔ Serializers funcionando  
✔ Views configuradas  
✔ URLs registradas  
✔ Migrations aplicadas  
✔ Autenticação configurada  
✔ Endpoints funcionando  

---

# 👨‍💻 Autor

**Orlando Conceição**  
Backend Developer  

📧 orlandoconceicao94@gmail.com
