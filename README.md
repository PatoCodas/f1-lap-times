# F1 Lap Times

## Descrição

O projeto **F1 Lap Times** é uma aplicação web desenvolvida em Django feita para estudos dessa tecnologia, ela serve para registrar e visualizar os tempos de volta de diferentes pistas de Fórmula 1. Ele permite adicionar, visualizar e deletar tempos de volta.

## Funcionalidades

- Adicionar tempos de volta para diferentes pistas.
- Visualizar os tempos de volta registrados.
- Deletar tempos de volta.
- Alternar entre modo claro e modo noturno.

## Dependências

Para rodar este projeto, você precisará das seguintes dependências:

- Python 3.6+
- Django 3.2+
- Bootstrap 5.1.3
- Font Awesome 5.15.4

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/PatoCodas/f1-lap-times.git
    cd f1-lap-times
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

6. Acesse a aplicação no navegador:

    ```text
    http://127.0.0.1:8000/
    ```

## Estrutura do Projeto

```filetree
f1-laptimes/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── laptimes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_add_tracks.py
│   │   └── __init__.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── f1_lap_times.html
│   │   └── contact.html
├── manage.py
├── requirements.txt
└── venv/
```

## Contato
Para mais informações, entre em contato:

Email: miguelsilvaug@gmail.com
GitHub: PatoCodas

## Feito com ❤️ por PatoCodas