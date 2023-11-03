from django.test import TestCase
from gestion.models import Persona

class PersonaModelTest(TestCase):
    def test_str_method(self):
        persona = Persona(nombre="Juan", apellido_paterno="Pérez", apellido_materno="González")
        self.assertEqual(str(persona), "Juan Pérez González")

    def test_nombre_max_length(self):
        max_length = Persona._meta.get_field("nombre").max_length
        self.assertEqual(max_length, 50)

    def test_apellido_paterno_max_length(self):
        max_length = Persona._meta.get_field("apellido_paterno").max_length
        self.assertEqual(max_length, 50)

    def test_apellido_materno_max_length(self):
        max_length = Persona._meta.get_field("apellido_materno").max_length
        self.assertEqual(max_length, 50)

    def test_nombre_required(self):
        with self.assertRaises(Exception):
            # Intentar guardar una instancia de Persona sin nombre debería generar una excepción
            persona = Persona(apellido_paterno="Pérez", apellido_materno="González")
            persona.full_clean()

    def test_apellido_paterno_required(self):
        with self.assertRaises(Exception):
            # Intentar guardar una instancia de Persona sin apellido_paterno debería generar una excepción
            persona = Persona(nombre="Juan", apellido_materno="González")
            persona.full_clean()

    def test_apellido_materno_required(self):
        with self.assertRaises(Exception):
            # Intentar guardar una instancia de Persona sin apellido_materno debería generar una excepción
            persona = Persona(nombre="Juan", apellido_paterno="Pérez")
            persona.full_clean()