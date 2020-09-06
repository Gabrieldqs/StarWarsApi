from django.test import TestCase, Client
from django.urls import reverse 
from starWarsApi.models import Planet
import json

class TestViews(TestCase):

	def setUp(self):
		self.planet = Planet.objects.create(
			name='testPlanet',
			climate='testClimate',
			terrain='testTerrain',
			films=0
		)

		self.client = Client()
		self.planets_url = reverse('planets')
		self.planetsId_url = reverse('planetsId',kwargs={'planet_id':self.planet.id})
		self.planetsInvalidId_url = reverse('planetsId',kwargs={'planet_id':self.planet.id+1})
		self.planetsName_url = reverse('planetsName',kwargs={'planet_name':self.planet.name})

	def test_planets(self):
		response = self.client.get(self.planets_url)
		self.assertEquals(response.status_code, 200)
		responseJson = json.loads(response.content)
		self.assertEquals(responseJson['results'][0]['Planet'],'testPlanet')

	def test_get_planet_id(self):
		response = self.client.get(self.planetsId_url)
		self.assertEquals(response.status_code, 200)
		responseJson = json.loads(response.content)
		self.assertEquals(responseJson[0]['Planet'],'testPlanet')

	def test_get_planet_name(self):
		response = self.client.get(self.planetsName_url)
		self.assertEquals(response.status_code, 200)
		responseJson = json.loads(response.content)
		self.assertEquals(responseJson[0]['Planet'],'testPlanet')

	def test_urls_DELETE_found(self):
		response = self.client.delete(self.planetsId_url)
		self.assertEquals(response.status_code, 200)
		responseJson = json.loads(response.content)
		self.assertEquals(responseJson[0]['Success'],'Planet deleted successfully!')

	def test_urls_DELETE_notFound(self):
		response = self.client.delete(self.planetsInvalidId_url)
		self.assertEquals(response.status_code, 200)
		responseJson = json.loads(response.content)
		self.assertEquals(responseJson[0]['Error'],'No planet with id: '+str(self.planet.id+1))