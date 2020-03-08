# Medicar
Sistema para gestão de consultas em uma clínica médica


Para Inicializar o sistema deverá **Fazer!**:
instalar o pipenv em sua env.
	
	>>> pip install --user pipenv
	
depois entrar na pasta de backend e inicializar o pipenv:
	   
	>>> pipenv shell
	>>> pipenv install
depois de instalados os pacotes, vamos criar o super usuário	 
	
	>>> python manage.py createsuperuser
	
depois cria um "token" de acesso para as requisições da api:
	
	>>> python manage.py drf_create_token nomedousuario
depois execute o sistema :
		
	>>> python manage.py runserver

url:

	http://127.0.0.1:8000/admin/




