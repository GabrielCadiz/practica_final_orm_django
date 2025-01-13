from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Test",
            ciudad="Ciudad Test",
            pais="País Test"
        )
    
    def test_model_data(self):
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Test")
        self.assertEqual(laboratorio.ciudad, "Ciudad Test")
        self.assertEqual(laboratorio.pais, "País Test")
    
    def test_lista_laboratorios_url(self):
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEqual(response.status_code, 200)
    
    def test_lista_laboratorios_template_and_content(self):
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/lista_laboratorios.html')
        self.assertContains(response, "Información de Laboratorios")
    
    

