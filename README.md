

# Projeto de Gerenciamento de EPIs

Este é um sistema web desenvolvido em Django para gerenciar o controle de Equipamentos de Proteção Individual (EPIs), usuários, empréstimos, devoluções e informações de colaboradores.

---


---

##  Principais Funcionalidades

* **Registrar dados**: Permite registrar informações em todas as tabelas do sistema.
* **Listar dados**: Exibe uma lista de todos os registros (colaboradores, equipamentos, empréstimos).
* **Atualizar dados**: Permite a edição de registros existentes.
* **Excluir dados**: Possibilita a remoção de registros.
* **Página de Login**: Autenticação de usuários para acesso seguro ao sistema.

---

###  Como executar o projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo.

####  Requisitos

Certifique-se de que os seguintes programas estão instalados em seu computador:

* **Python 3.10+**
* **Git**
* **Pip**
* (Opcional) **Virtualenv**

### ✅ 1. Clone o repositório

Abra o seu terminal (Git Bash, PowerShell, etc.) e clone o projeto do GitHub.   



```bash
git clone (https://github.com/petersonwagner16/Gerenciamento-EPI.git)
cd Gerenciamento-EPI
```

✅ 2. Crie e ative o ambiente virtual
É uma boa prática isolar as dependências do projeto em um ambiente virtual.

```Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate


# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
✅ 3. Instale as dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no arquivo requirements.txt.

```Bash

pip install -r requirements.txt
```
✅ 4. Execute as migrações
Este passo cria e aplica as migrações para que a estrutura do seu banco de dados seja criada com base nos seus modelos do Django.

Bash

python manage.py makemigrations
python manage.py migrate
✅ 5. Carregue os Dados Iniciais
Para que o projeto funcione corretamente, ele precisa de alguns dados essenciais que já vêm com o sistema. Esses dados incluem os tipos de status de equipamentos, status de empréstimos e níveis de acesso, que são a base para o funcionamento das outras partes do sistema.

Para carregar esses dados, execute os comandos abaixo. Eles vão preencher o seu banco de dados com as informações necessárias:

```Bash

python manage.py loaddata status_equipamento.json
python manage.py loaddata status_emprestimo.json
python manage.py loaddata niveis_acesso.json
```
✅ 6. Crie um Superusuário
Crie um usuário com privilégios de administrador para acessar a área de administração do Django.

```Bash

python manage.py createsuperuser
```
Siga as instruções para definir e-mail e senha.

✅ 7. Inicie o servidor
Agora, você pode iniciar o servidor de desenvolvimento do Django.

```Bash

python manage.py runserver
```
O projeto estará acessível em seu navegador no seguinte endereço:

http://127.0.0.1:8000/
