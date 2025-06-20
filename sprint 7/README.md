# Sistema de Gestión Veterinaria "Amigos Peludos" 

## Descripción
Sistema de gestión para la Clínica Veterinaria "Amigos Peludos", desarrollado en Python. Esta aplicación permite administrar el registro de mascotas, sus dueños y el historial de consultas médicas, facilitando la gestión diaria de la clínica veterinaria.

## Características Principales 
- Registro completo de mascotas y sus dueños
- Gestión de consultas veterinarias
- Visualización de historiales médicos
- Listado de mascotas registradas

## Estructura del Proyecto 
El proyecto está organizado en los siguientes módulos:
- `Veterinaria.py`: Módulo principal con el menú y funciones core
- `Animales.py`: Gestión de mascotas
- `Personas.py`: Gestión de dueños
- `Historias.py`: Gestión de consultas médicas

## Funcionalidades Detalladas 

### 1. Registro de Mascotas
- Nombre de la mascota
- Especie
- Raza
- Edad
- Información del dueño

### 2. Registro de Dueños
- Nombre completo
- Teléfono de contacto
- Dirección

### 3. Gestión de Consultas
- Fecha de la consulta
- Motivo de la visita
- Diagnóstico veterinario
- Registro asociado a la mascota

### 4. Consulta de Información
- Listado completo de mascotas
- Datos de contacto de dueños
- Historial médico por mascota

La aplicación tiene en cuenta que un dueño puede tener 1 o mas mascotas y con esta lógica se presenta el 
proyecto, además al registrar una consulta, se necesita tener ya la mascota registrada o sino no se podrá registrar
Si se registra la misma mascota y el mismo dueño, el programa muestra un mensaje diciendo que ya esta registrada la 
mascota.

## Sistema de Almacenamiento de Datos

El sistema utiliza diferentes formatos de archivo para almacenar la información de manera organizada y eficiente:

### 5. Archivos CSV (Comma-Separated Values)

#### mascotas.csv
- Almacena la información básica de cada mascota
- Estructura: nombre,especie,raza,edad,dueño
- Modo de acceso: lectura/escritura (append)
- Se utiliza para registros permanentes y consultas rápidas

#### duenhos.csv
- Contiene los datos de contacto de los dueños
- Estructura: nombre,telefono,direccion
- Modo de acceso: lectura/escritura (append)
- Permite mantener un registro actualizado de los propietarios

### 6. Archivo JSON (JavaScript Object Notation)

#### consultas.json
- Almacena el historial médico y consultas
- Estructura:  "consultas": [
        {
            "Fecha de la consulta": "DD-MM-AAAA",
            "Motivo": "Texto",
            "Diagnostico": "Texto",
            "Mascota": "Texto"
        }
}


## Manejo de Errores y Logging

### Sistema de Logs
El sistema implementa un registro detallado de eventos utilizando el módulo `logging` de Python. 
Los logs se almacenan en el archivo `clinica_veterinaria.log` con la siguiente configuración:

1. **INFO**: Registra operaciones normales del sistema
   - Inicio y cierre del programa
   - Registro exitoso de mascotas
   - Registro de consultas

2. **WARNING**: Registra situaciones anómalas no críticas
   - Intentos de acceder a mascotas inexistentes
   - Listas de registros vacías
   - Validaciones fallidas

3. **ERROR**: Registra errores críticos del sistema
   - Errores en entrada de datos
   - Fallos en búsqueda de mascotas
   - Opciones de menú inválidas

#Pruebas Unitarias
El proyecto incluye una suite de pruebas unitarias ubicada en GestorVeterinaria/test_veterinaria.py utilizando el módulo unittest de Python.
Estas pruebas cubren:


Validación de datos de entrada (edad, teléfono)
Creación y lectura de archivos de datos
Registro y búsqueda de mascotas, dueños y consultas
Manejo de errores personalizados
Integridad de las operaciones principales del sistema

Para ejecutar las pruebas, usa el siguiente comando en la terminal desde la raíz del proyecto:
python -m unittest GestorVeterinaria/test_veterinaria.py