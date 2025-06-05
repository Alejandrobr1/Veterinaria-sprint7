import unittest
import Controller, Models
from GestorVeterinaria.MascotaNotFoundError import MascotaNotFoundError

# Clase de pruebas unitarias
class MyTestCase(unittest.TestCase):

    # Prueba la capitalización de nombres de mascotas
    def test_ingreso_datos(self):
        self.assertEqual('boby'.strip().capitalize(), 'Boby')

    # Prueba la validación de la edad de la mascota
    def test_validar_edad(self):
        self.assertRaises(ValueError, Models.Mascota.validar_edad, -1)
        self.assertRaises(ValueError, Models.Mascota.validar_edad, 'abc')
        self.assertTrue(Models.Mascota.validar_edad(5))

    # Prueba la validación del teléfono del dueño
    def test_validar_telefono(self):
        self.assertRaises(ValueError, Models.Duenho.validar_telefono, -123456789)
        self.assertRaises(ValueError, Models.Duenho.validar_telefono, 'abc')
        self.assertTrue(Models.Duenho.validar_telefono(123456789))

    # Prueba la creación del archivo de mascotas
    def test_crear_archivo_mascotas(self):
        Controller.crear_archivo_mascotas()
        with open("mascotas.csv", "r") as file:
            self.assertTrue(file.readable())

    # Prueba la creación del archivo de dueños
    def test_crear_archivo_duenhos(self):
        Controller.crear_archivo_duenhos()
        with open("duenhos.csv", "r") as file:
            self.assertTrue(file.readable())

    # Prueba la creación del archivo de consultas
    def test_crear_archivo_consultas(self):
        Controller.crear_archivo_consultas()
        with open("consultas.json", "r") as file:
            self.assertTrue(file.readable())


    # Prueba la validación de existencia de mascota y dueño
    def test_validar_existencia_mascota_duenho(self):
        Controller.crear_archivo_mascotas()
        Controller.crear_archivo_duenhos()
        Controller.registrar_mascota_duenho("Oto", "Perro", "Labrador", 5, "Roma", 123456789, "Calle Falsa 123")
        self.assertTrue(Controller.validar_existencia_mascota_duenho("Oto", "Roma"))
        self.assertFalse(Controller.validar_existencia_mascota_duenho("Boby", "Maria Lopez"))


    # Prueba la validación de existencia de mascota en consultas
    def test_validar_existencia_mascota_consulta(self):
        Controller.crear_archivo_mascotas()
        Controller.registrar_mascota_duenho("Oto", "Perro", "Labrador", 5, "Roma", 123456789, "Calle Falsa 123")
        self.assertTrue(Controller.validar_existencia_mascota_consulta("Oto"))
        self.assertFalse(Controller.validar_existencia_mascota_consulta("Max"))


    # Prueba el registro de una consulta veterinaria
    def test_registrar_consulta(self):
        Controller.crear_archivo_mascotas()
        Controller.crear_archivo_consultas()
        Controller.registrar_mascota_duenho("Oto", "Perro", "Labrador", 5, "Roma", 123456789, "Calle Falsa 123")
        consulta = Controller.registrar_consulta("10-01-2023", "Chequeo general", "Todo en orden", "Oto")
        self.assertEqual(consulta.fecha, "10-01-2023")
        self.assertEqual(consulta.motivo, "Chequeo general")
        self.assertEqual(consulta.diagnostico, "Todo en orden")
        self.assertEqual(consulta.mascota_relacionada, "Oto")


    # Prueba la función de listar mascotas
    def test_listar_mascotas(self):
        Controller.crear_archivo_mascotas()
        Controller.registrar_mascota_duenho("Boby", "Perro", "Labrador", 5, "Juan Perez", 123456789, "Calle Falsa 123")
        Controller.listar_mascotas()


    # Prueba la función de listar dueños
    def test_listar_duenhos(self):
        Controller.crear_archivo_duenhos()
        Controller.registrar_mascota_duenho("Boby", "Perro", "Labrador", 5, "Juan Perez", 123456789, "Calle Falsa 123")
        Controller.listar_duenhos()


    # Prueba la búsqueda de una mascota
    def test_buscar_mascota(self):
        Controller.crear_archivo_mascotas()
        Controller.registrar_mascota_duenho("Boby", "Perro", "Labrador", 5, "Juan Perez", 123456789, "Calle Falsa 123")
        self.assertTrue(Controller.buscar_mascota("Boby"))
        self.assertFalse(Controller.buscar_mascota("Max"))


    # Prueba la carga de consultas desde un archivo JSON
    def test_cargar_consultas_json(self):
        Controller.crear_archivo_consultas()
        Controller.crear_archivo_mascotas()
        Controller.registrar_mascota_duenho("Boby", "Perro", "Labrador", 5, "Juan Perez", 123456789, "Calle Falsa 123")
        Controller.registrar_consulta("10-01-2023", "Chequeo general", "Todo en orden", "Boby")
        consultas = Controller.cargar_consultas_json("Boby")
        self.assertTrue(consultas)
        self.assertFalse(not consultas)


    # Prueba la excepción personalizada cuando no se encuentra una mascota
    def test_mascota_not_found_error(self):
        with self.assertRaises(MascotaNotFoundError):
            raise MascotaNotFoundError("La mascota no fue encontrada")


# Ejecuta las pruebas si el archivo es ejecutado directamente
if __name__ == '__main__':
    unittest.main()
