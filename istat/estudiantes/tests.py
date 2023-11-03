from django.test import TestCase
from .models import Estudiante
from gestion.models import Persona  # Asegúrate de importar el modelo Persona

class EstudianteModelTestCase(TestCase):
    def setUp(self):
        # Crea una instancia de Persona para asociar con el Estudiante
        self.persona = Persona(nombre="Juan", apellido_paterno="Pérez", apellido_materno="González")
        self.persona.save()

        self.estudiante = Estudiante(persona=self.persona, codigo="12345")

    def test_nombre_apellido_materno_aparecen_en_str(self):
        self.assertEqual(
            str(self.estudiante), "Juan Pérez González",
            "El método __str__ no devuelve el formato esperado."
        )

    def test_codigo_max_length(self):
        max_length = 50
        codigo_field = self.estudiante._meta.get_field("codigo")

        self.assertEqual(
            codigo_field.max_length, max_length,
            "La longitud máxima del campo 'codigo' no es la esperada."
        )