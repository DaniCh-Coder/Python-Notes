# 🚀 Welcome to Pydantic
### Gracias por visitar mi repositorio de Pydantic

Este repositorio contiene una serie de notebooks y scripts de Python que he creado para aprender y enseñar Pydantic.


## Pydantic: guia introductoria
Pydantic es una librería de Python que permite definir y validar modelos de datos. 
+ Es muy útil para definir esquemas de datos y validarlos. Pydantic es muy útil para trabajar con APIs REST, bases de datos, etc.
  + La versión actual de Pydantic es la 2.10.6 y está en un repositorio de github.
    + Sin embargo, todas las releases de la versión 2 pueden servir para aprender Pydantic.

Esta guía cubre desde conceptos básicos hasta temas avanzados sobre el uso de **Pydantic**, una biblioteca poderosa para validación de datos en Python.

### 1. Introducción
* 🚀 [Introducción a Pydantic](p00_pydantic_intro.ipynb)  
  Explicación general de Pydantic: ¿qué es, para qué sirve y cómo se usa?

### 2. Modelos
* 🚀 [Modelos en Pydantic](p01_models.ipynb)  
  Creación y uso de modelos de datos con Pydantic.
* 📝 [Modelos Anidados](p02_nested_models.ipynb)  
  Cómo estructurar modelos dentro de otros modelos.

### 3. Tipos de Datos y Validaciones
* 🚀 [Tipos de Datos en Pydantic](p04_types.ipynb)  
  Descripción y uso de los distintos tipos de datos disponibles.
* 📝 [Tipos y Validaciones](p04_types.py)  
  Implementación práctica de validaciones con Pydantic.

### 4. Configuración de Tipos Personalizados
* 🚀 [Configuración de Tipos](p05_custom_types.ipynb)  
  Definir y trabajar con tipos de datos personalizados en Pydantic.
* 📝 [Tipos Configurados](p05_custom_types.py)  
  Ejemplos prácticos de configuración de tipos.

### 5. Validaciones Avanzadas
* 🚀 [Validaciones de Tipos y Modelos](p06_field_model_validation.md)  
  Exploración de validaciones a nivel de campos y modelos completos.
* 📝 [Ejercicio de Validaciones](p06_field_model_validation.py)  
  Práctica con validaciones.
* 📝 [Type Hints y Validaciones](p07_type_hints_validation.ipynb)  
  Uso de **type hints** para mejorar la validación de datos.

### 6. Serialización
* 🚀 [Serialización en Pydantic](p08_serialization.ipynb)  
  Cómo convertir modelos a formatos como JSON.
* 📝 [Más sobre Serialización](p09_serialization.py)  
  Serialización avanzada y casos de uso.
* 📝 [JSON Schema](p10_JSON_Schema.ipynb)  
  Generación de **JSON Schema** desde modelos Pydantic.

### 7. Modelos Circulares y Anidados
* 🚀 [Modelos Circulares y Anidados](p11_nested_circular_models.ipynb)  
  Cómo manejar modelos que hacen referencia entre sí mismos.

---

## 🔧 Requisitos
Para seguir esta guía, asegúrate de tener **Python 3.8+** instalado. Luego, instala Pydantic ejecutando:
```bash
pip install pydantic
```

Opcionalmente, puedes instalar **Jupyter Notebook** si deseas ejecutar los archivos `.ipynb`:
```bash
pip install notebook
```

---

## 🌟 Autor
Este tutorial fue desarrollado por [[Daniel Christello](https://github.com/DaniCh-Coder)].

Si tienes preguntas, sugerencias o mejoras, no dudes en abrir un **issue** o un **pull request**.

---

## 📄 Licencia
Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.

```text
MIT License
Copyright (c) 2024
Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 🚀 Contribuir
Si quieres contribuir a esta guía:
1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-mejora`).
3. Realiza tus cambios y haz un **commit** (`git commit -m 'Agrega nueva funcionalidad'`).
4. Envía un **pull request**.

Toda ayuda es bienvenida. ¡Gracias por tu interés en mejorar este contenido! 🚀


