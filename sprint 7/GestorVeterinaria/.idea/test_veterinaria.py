import unittest
from GestorVeterinaria import Controller, Models, View


class MyTestCase(unittest.TestCase):
    def test_ingreso_datos(self):
        self.assertEqual('boby'.strip().capitalize(), 'Boby')# add assertion here

    def test_validar_edad(self):
        self.assertRaises(ValueError, GestorVeterinaria.Mascota.validar_edad, -1)
        self.assertRaises(ValueError, GestorVeterinaria.Mascota.validar_edad, 'abc')
        self.assertTrue(GestorVeterinaria.Mascota.validar_edad(5))


if __name__ == '__main__':
    unittest.main()
