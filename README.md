# 🐍 Prácticas de Python: Backend Developer & Desarrollo Inteligente con IA

---

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-green)
![Python Version](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Udemy Course](https://img.shields.io/badge/Curso-Backend%20Developer%20(Udemy)-ec1c24?logo=udemy&logoColor=white)
![Santander Course](https://img.shields.io/badge/Curso-Cursor%20con%20Python%20(Santander)-002F6C)

---

## 📖 Descripción del Proyecto
Este repositorio reúne el conjunto de prácticas, ejercicios y desarrollos realizados a lo largo de mi trayectoria de aprendizaje en el ecosistema de Python. Está estructurado en dos secciones principales que representan hitos clave en mi especialización como desarrollador backend:

1. **Curso de Backend Developer (Udemy):** Un recorrido integral por los fundamentos del lenguaje, estructuras de datos avanzadas, modularización mediante paquetes y programación orientada a objetos (POO) aplicada a la resolución de problemas lógicos y manipulación de archivos del sistema.
2. **Curso de "Cursor con Python: desarrollo inteligente con IA" (Santander Open Academy):** Prácticas especializadas ubicadas en la carpeta [Cursor](./Cursor), enfocadas en el flujo de desarrollo moderno utilizando el IDE Cursor. Esto incluye la implementación de tipado estático estricto (PEP 695 / Python 3.12+), testing automatizado con `pytest`, manejo de errores personalizado y análisis/visualización de datos mediante `pandas` y `matplotlib`.

---

## 🎯 Objetivo
Consolidar el dominio técnico del lenguaje de programación Python bajo estándares profesionales de desarrollo de software, logrando:
- Diseñar soluciones robustas y modulares aplicando los principios de la **Programación Orientada a Objetos (POO)**.
- Integrar metodologías modernas de desarrollo co-piloteado por **Inteligencia Artificial (IA)** mediante el IDE Cursor para aumentar la eficiencia y mantenibilidad del código.
- Implementar arquitecturas de testing unitario y análisis de datos robustos, garantizando la estabilidad de los scripts backend.

---

## 🛠️ Requerimientos Técnicos / Temas Cubiertos
Este proyecto cumple con los estándares exigidos para el aprendizaje integral de ambas formaciones:

### 1. Fundamentos & Backend en Python (Prácticas de Udemy)
- ✅ **Sintaxis y Tipos de Datos:** Operaciones matemáticas, manipulación de cadenas de texto y conversiones de tipos.
- ✅ **Estructuras de Control:** Condicionales complejos, bucles (`while`, `for`), bucles anidados y expresiones ternarias.
- ✅ **Estructuras de Datos:** Colecciones mutables e inmutables (Listas, Tuplas, Conjuntos y Diccionarios) y sus métodos integrados.
- ✅ **Modularidad y Funciones:** Funciones de primer orden, lambdas, paso de funciones como argumentos, closures y decoradores.
- ✅ **Programación Orientada a Objetos (POO):** Clases, constructores (`__init__`), encapsulamiento de atributos/métodos, herencia simple/múltiple, llamadas a superclases, métodos mágicos (`__str__`, `__repr__`, `__len__`) y clases abstractas.
- ✅ **Control de Excepciones:** Bloques `try/except/finally`, manejo de excepciones específicas y definición de errores personalizados.
- ✅ **Persistencia y Archivos:** Lectura/escritura de archivos de texto plano, procesamiento de archivos CSV, serialización binaria con Pickle y manipulación de imágenes/archivos binarios.

### 2. Desarrollo Inteligente con IA (Prácticas de Santander Open Academy / Cursor)
- ✅ **Tipado Estático Moderno:** Uso de `typing` y la sintaxis PEP 695 (`type Alias = Tipo`) de Python 3.12 para un código autodocumentado y seguro.
- ✅ **Análisis de Datos:** Carga y procesamiento dinámico de conjuntos de datos con la librería `pandas` en `Cursor/analisis.py`.
- ✅ **Visualización de Datos:** Generación y renderizado de gráficos de dispersión (Scatter Plots) con la interfaz orientada a objetos de `matplotlib`.
- ✅ **Testing Unitario:** Automatización del control de calidad de software mediante la suite `pytest` para la verificación del comportamiento de los módulos.
- ✅ **Asistencia de IA:** Uso estratégico de prompts y refactorización inteligente provista por Cursor para optimizar el código y documentar procesos técnicos de forma eficiente.

---

### Estructura del Proyecto

```
be_python/ (Python/)
│
├── datos.csv                      # Base de datos CSV para pruebas de persistencia en Udemy
├── datos.pkl                      # Archivo serializado con Pickle
├── foto_copia.png                 # Imagen resultante de pruebas binarias
├── imagen1.png                    # Imagen original para pruebas binarias
├── mensaje.txt                    # Archivo de texto plano de entrada
├── salida.txt                     # Archivo de texto plano de salida
│
├── ej_01_hola.py                  # Práctica de bienvenida e impresión en consola
├── ej_02_tipos_datos.py           # Operaciones básicas y tipos de datos
├── ...                            # (Ejercicios intermedios de sintaxis y colecciones)
├── ej_22_error_personalizado.py   # Creación de excepciones personalizadas de negocio
├── ej_23_poo.py                   # Modelado básico de objetos
├── ej_26_encapsulamiento.py       # Aplicación de getters, setters y atributos privados
├── ej_28_superclases.py           # Uso avanzado de super() y herencia estructurada
├── ej_32_abstract.py              # Definición e instanciación de clases abstractas
├── ej_33_archivos.py              # Operaciones básicas I/O con open()
├── ej_34_csv_archivo.py           # Lectura y escritura manual de archivos CSV
├── ej_35_pickle.py                # Serialización y deserialización de objetos
├── ej_36_copia_imagenes.py        # Lectura y clonación binaria de archivos multimedia
│
├── mi_proyecto/                   # Estructura modular de proyecto local
│   ├── main.py                    # Punto de entrada
│   └── calculadora.py             # Lógica de utilidades matemáticas
│
├── paquete/                       # Demostración del empaquetado nativo en Python
│   ├── main.py                    # Script de importación y ejecución de paquetes
│   └── operaciones/               # Subcarpeta con scripts auxiliares
│
└── Cursor/                        # 🌟 EJERCICIOS CURSO SANTANDER OPEN ACADEMY (IA)
    ├── datos.csv                  # Dataset para análisis de datos
    ├── analisis.py                # Script principal de análisis con pandas y matplotlib (OOP)
    ├── calculadora.py             # Calculadora robusta con tipado estático
    ├── contador.py                # Analizador y contador de palabras de un archivo de texto
    ├── contador.txt               # Texto de muestra para pruebas
    ├── fizzbuzz.py                # Algoritmo clásico FizzBuzz optimizado
    ├── prueba_cursor.py           # Ejercicios varios de programación asistida
    ├── test_contador.py           # Casos de prueba unitaria utilizando pytest
    └── scatter_columnas.png       # Gráfico de dispersión generado dinámicamente
```

---

## 🚀 Cómo Empezar / Instalación

Para ejecutar cualquiera de los scripts del proyecto o la suite de pruebas unitarias, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/jltamayocabello-droid/be_python.git
cd be_python
```

### 2. Configurar el Entorno Virtual
Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias
Las prácticas de la carpeta `Cursor/` requieren librerías de análisis y testing:
```bash
pip install pandas matplotlib pytest
```

### 4. Ejecución de Scripts
- **Ejercicios base (Udemy):**
  ```bash
  python ej_23_poo.py
  ```
- **Análisis de datos (Cursor):**
  ```bash
  python Cursor/analisis.py
  ```
- **Ejecutar Pruebas Unitarias (pytest):**
  ```bash
  pytest Cursor/test_contador.py
  ```

---

## 🧠 Decisiones de Diseño / Aprendizajes Clave

### Tipado Estático Avanzado
**Decisión:** Utilizar de manera exhaustiva anotaciones de tipo (`Type Hints`) y alias de tipo (`PEP 695`) en las tareas asistidas por la IA de Cursor.
**Justificación:** Aumenta exponencialmente la robustez del código backend, permitiendo a los analizadores estáticos como MyPy detectar inconsistencias de datos antes de la ejecución y mejorando el autocompletado en el editor.

### Arquitectura de Manejo de Errores Orientada a Objetos
**Decisión:** Implementar jerarquías de excepciones personalizadas heredando de `Exception` (por ejemplo, `ErrorCargaDatos`, `ErrorGuardadoGrafico` en `analisis.py`).
**Justificación:** Permite aislar y documentar fallos específicos de entrada/salida o procesamiento de datos, asegurando que el backend pueda recuperarse de manera controlada y devolver mensajes limpios al usuario o consola.

### Testing Automatizado
**Decisión:** Incorporar pruebas unitarias utilizando el framework moderno `pytest`.
**Justificación:** Garantiza un flujo donde cualquier refactorización del código de producción asistida por la IA pueda validarse de forma inmediata, evitando regresiones en la lógica de negocio.

---

## 📱 Áreas Técnicas Destacadas

| Área Técnica | Herramientas Utilizadas | Descripción |
| :--- | :--- | :--- |
| 🐍 **Backend Core** | Sintaxis Python 3.12+ | Implementación completa de las bases sintácticas del lenguaje. |
| 🧱 **Programación Orientada a Objetos** | Clases, Herencia, Abstract | Modelos de datos estructurados, reutilizables y con encapsulamiento estricto. |
| 📂 **Manipulación de Archivos** | `open()`, `csv`, `pickle` | Persistencia y almacenamiento de datos locales en múltiples formatos. |
| 📊 **Análisis & Data Science** | `pandas` | Limpieza, estructuración y cálculo estadístico automatizado de conjuntos de datos. |
| 📈 **Visualización Gráfica** | `matplotlib` | Generación autónoma de gráficos tipo Scatter Plot de alta fidelidad. |
| 🧪 **Garantía de Calidad (QA)** | `pytest` | Suite de pruebas unitarias enfocadas a garantizar la estabilidad del software. |
| 🤖 **Ingeniería con IA** | Cursor IDE, Prompts | Code-pairing asistido para agilizar el diseño de algoritmos limpios y legibles. |

---

## ✒️ Autor
**Jorge Tamayo Cabello**
*Diseñador Front-End*

---

## 📄 Licencia
Este repositorio es de carácter estrictamente académico y educativo. Todo el contenido es libre de ser consultado con fines de aprendizaje y referencia técnica.

---

## 🙏 Agradecimientos
- A **Udemy** por la excelente formación en desarrollo backend y fundamentos de Python.
- A **Santander Open Academy** por la beca y el acceso al programa de desarrollo inteligente con IA.
- A la **comunidad de Python** por mantener la documentación y librerías open-source que facilitan la creación de software potente.
