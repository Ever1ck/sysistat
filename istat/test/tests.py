from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from gestion.models import Persona   # Asegúrate de importar correctamente tu modelo

class PersonaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Crea datos de ejemplo en la base de datos para probar
        Persona.objects.create(nombre="Juan", apellido_paterno="Pérez", apellido_materno="Gómez")
        Persona.objects.create(nombre="María", apellido_paterno="López", apellido_materno="Martínez")

    def test_list_personas(self):
        # Prueba la solicitud GET para listar personas
        response = self.client.get('/app-gestion/persona/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_persona(self):
        # Prueba la solicitud POST para crear una nueva persona
        data = {'nombre': 'Nueva', 'apellido_paterno': 'Persona', 'apellido_materno': 'Test'}
        response = self.client.post('/app-gestion/persona/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Persona.objects.count(), 3)

    def test_retrieve_persona(self):
        # Prueba la solicitud GET para recuperar una persona específica
        persona = Persona.objects.get(nombre="Juan")
        response = self.client.get(f'/app-gestion/persona/{persona.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_persona(self):
        # Prueba la solicitud PUT para actualizar una persona existente
        persona = Persona.objects.get(nombre="Juan")
        data = {'nombre': 'Juan', 'apellido_paterno': 'Pérez', 'apellido_materno': 'Gómez García'}
        response = self.client.put(f'/app-gestion/persona/{persona.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        persona.refresh_from_db()
        self.assertEqual(persona.apellido_materno, 'Gómez García')

    def test_delete_persona(self):
        # Prueba la solicitud DELETE para eliminar una persona
        persona = Persona.objects.get(nombre="Juan")
        response = self.client.delete(f'/app-gestion/persona/{persona.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Persona.objects.count(), 1)