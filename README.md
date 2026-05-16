# ✨ Igreja Luz e Esperança

Sistema web desenvolvido para gerenciamento e divulgação de informações da Igreja Luz e Esperança utilizando Python, Flask, Bootstrap, JavaScript e MySQL.

O sistema permite gerenciar eventos, pedidos de oração, autenticação administrativa e exibição de conteúdos institucionais da igreja de forma moderna, organizada e responsiva.

---

# 🚀 Tecnologias Utilizadas

## 🐍 Python

Responsável pela lógica principal do sistema.

## 🌐 Flask

Framework web utilizado para criação das rotas e páginas.

## 🎨 HTML5

Estruturação das páginas do sistema.

## 🎨 CSS3

Estilização personalizada da interface.

## 📱 Bootstrap 5

Framework utilizado para responsividade e componentes modernos.

## ⚡ JavaScript

Responsável pelas interações dinâmicas da interface.

## 🗄️ MySQL

Banco de dados utilizado no armazenamento das informações.

## 🔐 Flask-Login

Gerenciamento de autenticação administrativa.

---

# 📌 Funcionalidades do Sistema

## 🏠 Página Inicial

* Carousel de imagens
* Missão da igreja
* Informações da comunidade
* Exibição de eventos

## 📖 Página Sobre

* História da igreja
* Visão institucional
* Valores da igreja

## 📅 Agenda de Eventos

* Listagem de eventos cadastrados
* Exibição de data e horário

## 🙏 Pedido de Oração

* Formulário para envio de pedidos
* Armazenamento no banco de dados

## 📞 Página de Contato

* Informações da igreja
* Integração com Google Maps
* Redes sociais

## 🔐 Área Administrativa

* Login administrativo
* Dashboard
* Cadastro de eventos
* Edição de eventos
* Exclusão de eventos
* Visualização de pedidos de oração

## 📱 Responsividade

* Interface adaptada para celulares, tablets e computadores.

---

# 🛠 Como Rodar o Projeto Localmente

## 1️⃣ Clonar o Repositório

```bash
https://github.com/AlliferLopes27/SiteIgreja
```

---

## 2️⃣ Configurar o Banco de Dados

Instale um servidor local:

* XAMPP
* WampServer
* Laragon

Inicie:

* Apache
* MySQL

Acesse:

```text
http://localhost/phpmyadmin/
```

Crie o banco de dados:

```sql
CREATE DATABASE igreja_db;
```

---

## 3️⃣ Instalar as Dependências

Abra o terminal na pasta do projeto:

```bash
pip install flask flask_sqlalchemy flask_login pymysql werkzeug
```

---

## 4️⃣ Executar o Projeto

No terminal:

```bash
python app.py
```

Acesse no navegador:

```text
http://localhost:5000
```

---

# 🔐 Criando um Usuário Administrador

Após configurar o banco de dados e executar o projeto, é necessário criar um usuário administrador para acessar o painel administrativo.

Execute no terminal:

```bash
python criar_admin.py
```

Após executar o arquivo, o usuário administrador será salvo no banco de dados.

---

## 📌 Exemplo de Login

```text
Email: admin@admin.com
Senha: 12345@
```

---

## 🌐 Acesso Administrativo

Acesse no navegador:

```text
http://localhost:5000/admin/login
```

---

## 🔒 Segurança

As senhas são armazenadas utilizando hash de segurança através do Werkzeug.

---

# 📂 Estrutura do Projeto

```text
projeto-igreja/
│
├── models/
│   ├── evento.py
│   ├── pedido.py
│   └── usuario.py
│
├── routes/
│   ├── admin_routes.py
│   └── site_routes.py
│
├── services/
│   ├── auth_service.py
│   ├── evento_service.py
│   └── oracao_service.py
│
├── static/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── img/
│   │   └── imagens.png
│   │
│   └── js/
│       └── scripts.js
│
├── templates/
│   │
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── editar_evento.html
│   │   ├── eventos.html
│   │   ├── login.html
│   │   ├── novo_evento.html
│   │   └── pedidos.html
│   │
│   ├── agenda.html
│   ├── base.html
│   ├── contato.html
│   ├── index.html
│   ├── oracao.html
│   └── sobre.html
│
├── app.py
├── banco.py
├── config.py
├── criar_admin.py
├── extensions.py
└── requirements.txt
```

---

# 👨‍💻 Autor

Projeto desenvolvido por Allifer para fins acadêmicos, estudos e portfólio.
