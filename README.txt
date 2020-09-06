# Quick guide

- Run docker-compose up to build the project

- Create the database "starwars" for the project:
	'docker exec -it starwarsapi_db_1 psql -U postgres'
	'create dabase "starwars"'

- Run migrations:
	docker exec -it starwarsapi_web_1 bash
	python manage.py migrate

- To run automated tests:
	docker exec -it starwarsapi_web_1 bash
	python manage.py test


# Api Documentation
	GET localhost:8000/planets/name/'planetName' = Returns planet with given name
	DELETE localhost:8000/planets/name/'planetName' = Deletes planet with given name

	GET localhost:8000/planets/id/'planetId' = Returns planet with given id
	DELETE localhost:8000/planets/id/'planetId' = Deletes planet with given id
	
	GET localhost:8000/planets/	= Returns all planets
	POST localhost:8000/planets/ (args:['name','terrain','climate']) = Adds a planet with given parameters 