# Django Python Blog

This is a Django project to create a Blog site containing a Django app called Post which implements Create, Read, Update and Delete operations (CRUD).

This app was built using Django 2.1 and MaterializeCSS with Google Material Icons for templates. Also implements the layout UI Pattern.


## Server Dependencies

Python 3.6 or greater
Writing/Reading permissions for sqlite3 DB

## Install

1. Clone the repository into a python environment
	https://github.com/edisnake/userAPI.git
	
2. Go to Django cloned folder and run migrations into the database
	python manage.py migrate
	
3. (Optional) If you haven't a Django superuser yet, you can create one with this command. In that way you will be able to access the Django admin console.
	This command will prompt for a password
	python manage.py createsuperuser --username=adminuser --email=adminuser@gmail.com 
	
4. Run the server
	python manage.py runserver 8000


## Using the App

1. Go to your browser and copy-paste the URL "http://localhost:8000/"
2. In the main page, you will find a button to create a new post as well as a list of latest 10 created post, you can edit or query them one by one.

	Some considerations:

	2.1 When you click on the post's title, going to be redirected to another page where you can just see the post's info, in this case, you will not be able to modify nor delete the post.
	
	2.2 When you click on a post's pencil icon, going to be redirected to another page where you will have the ability to update its data or delete the post.
	

## Author

Edwuin Gutierrez
edwinguti86@gmail.com


## License

Copyright(c) 2018
MIT License
