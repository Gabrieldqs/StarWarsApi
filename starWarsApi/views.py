from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from starWarsApi.models import Planet
import json
import requests

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def getDeletePlanet(request, planet_id = None, planet_name = None):
	if planet_id is None:
		try:
			planet = Planet.objects.get(name=planet_name)
		except:
			response = json.dumps([{ 'Error': 'No planet with name: ' + planet_name}])
			return HttpResponse(response, content_type='text/json')

	if planet_name is None:
		try:
			planet = Planet.objects.get(pk=planet_id)
		except:
			response = json.dumps([{ 'Error': 'No planet with id: ' + planet_id}])
			return HttpResponse(response, content_type='text/json')

	if request.method == 'GET':
		response = json.dumps([{ 
			'Planet': planet.name, 
			'Climate': planet.climate, 
			'Terrain': planet.terrain, 
			'Films': planet.films}])

	if request.method == 'DELETE':
		response = json.dumps([{ 'Success': 'Planet deleted successfully!'}])
		planet.delete()

	return HttpResponse(response, content_type='text/json')

@csrf_exempt
def addGetPlanets(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        planetName = payload['name']
        planetClimate = payload['climate']
        planetTerrain = payload['terrain']
        planetFilmCount = getPlanetFilmCount(planetName)
        planet = Planet(name=planetName, climate=planetClimate, terrain=planetTerrain, films=planetFilmCount)

        try:
            planet.save()
            response = json.dumps([{ 'Success': 'Planet added successfully!'}])
        except Exception as e:
            response = json.dumps([{ 'Error': 'Planet could not be added: ' + str(e)}])

    if request.method == 'GET':
    	planet = Planet.objects.all()
    	response = buildResponseJson(planet)

    return HttpResponse(response, content_type='text/json')

def buildResponseJson(planetList):
	response = '{"results": ['

	for item in planetList.iterator():
		if item == planetList.last() and len(planetList)>1:
			response += ',' 
		response += json.dumps({ 
			'Planet': item.name, 
			'Climate': item.climate, 
			'Terrain': item.terrain, 
			'Films': item.films})
	response += ']}'

	return response

def getPlanetFilmCount(planetName):
	name = planetName
	url = 'https://swapi.dev/api/planets/'
	response = requests.get(url, params={'search': name}).json()

	if len(response['results']) > 0:
		return len(response['results'][0]['films'])
		
	return 0