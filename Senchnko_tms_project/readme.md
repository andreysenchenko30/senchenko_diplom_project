Django CRM website for enterprises

About this project:

CRM system can be used in big & small firms for internal and external communication (communication with employees and with customers). With the help of this CRM you can see actual tasks for every employee in the company, crate, delete and assign them. Also you can communicate with your customers with the help of e-mail form.

Installation and setting up Clone the project from: https://github.com/andreysenchenko30/senchenko_diplom_project

In PyCharm Professional, open the cloned project.

Create a virtual environment for the project. To do this, follow the steps provided below:

a. Open File->Settings->Project:TestDiploma->Python Interpreter.

b. In Python Interpreter dialog, click the Settings icon, and then click Add.

c. In the Add Python Interpreter dialog that appears, select Virtual Environment, and then click OK.

Make sure, that Django support is enabled for your project. To do this, in Settings->Languages & Frameworks, select Django, and then select the Enable Django Support check-box. After that, define Django project root (cloned project root), settings (TestDiploma\settings.py), and set folder pattern to track files (migrations).

Install the project dependencies: pip install -r requirements.txt.

Add project debug configuration:

a. In PyCharm toolbar, click Add Configuration.

b. In the Run/Debug Configuration dialog that appears, click the Add icon (+), and then select Django Server.

c. Enter a name for a new configuration, and then in the Environment variables field, add DJANGO_SETTINGS_MODULE=TestDiploma.settings. Click OK.

Create a psql database and a user:

a. Create a user, writing into the PostgreSQL terminal:

create user user_name with password 'password';
alter role user_name set client_encoding to 'utf8';
alter role user_name set default_transaction_isolation to 'read committed';
alter role user_name set timezone to 'UTC';
b. Then create a new database.

create database django_db owner user_name;
Enter this Database in Pycharm. In the Create Database dialog that appears, specify a name for a new database(for example: mydb) and owner (admin), and then click Save.

In TestDiploma\settings.py, set the database settings, as in the example below:

  DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'mydb',
       'USER': 'admin',
       'PASSWORD': '11111',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
} Make migrations to connect to the created database. In PyCharm terminal, run:

python manage.py makemigrations

python manage.py migrate

Start the development server: python manage.py runserver. Open http://127.0.0.1:8000/ on your browser to view the app.

Create a superuser to be able to fill in the database table with content. In PyCharm terminal, run:python manage.py createsuperuser Enter superuser credentials. Make sure to remember them to be able to login to the admin page.

On your web browser, open http://127.0.0.1:8000/admin, and feel free to add content to the database tables.

Troubleshooting I cannot apply migrations to the database If you experience problems with applying migrations to the database, in PyCharm project tree, right-click the vevn root folder, and then click Clean Python Compiled Files.