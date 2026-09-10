<p align="center">
  <img
    src="./assets/portada-passforge.png"
    alt="PassForge — Generador de contraseñas en Python"
    width="100%"
  />
</p>

<p align="center">
  Generador de contraseñas por consola desarrollado en Python que documenta
  la evolución de una implementación educativa basada en <code>random</code>
  hacia una versión mejorada utilizando <code>secrets</code>.
</p>

<p align="center">
  <img
    src="https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white"
    alt="Python 3.6+"
  />
  <img
    src="https://img.shields.io/badge/Interfaz-CLI-181717?style=for-the-badge"
    alt="CLI"
  />
  <img
    src="https://img.shields.io/badge/Licencia-MIT-2ea44f?style=for-the-badge"
    alt="Licencia MIT"
  />
  <img
    src="https://img.shields.io/badge/Estado-En%20desarrollo-f59e0b?style=for-the-badge"
    alt="Estado: En desarrollo"
  />
</p>

---

## Sobre PassForge

PassForge comenzó como un proyecto básico para practicar Python mediante la creación de un generador de contraseñas por consola.

La primera versión (`v1`) utilizaba el módulo `random`. Posteriormente revisé esa implementación desde una perspectiva de seguridad y detecté que su fuente de aleatoriedad no era apropiada para generar valores que deban ser difíciles de predecir.

A partir de esa revisión desarrollé una segunda versión (`v2`) utilizando `secrets`, junto con una longitud mínima y reglas básicas sobre los caracteres generados.

El repositorio conserva ambas versiones con un propósito educativo:

> Mostrar cómo una solución funcional puede evolucionar cuando se revisan sus decisiones de diseño y seguridad.

---

## Inicio rápido

### Requisitos

- Python 3.6 o superior.
- No requiere dependencias externas.

### Ejecutar la versión actual

```bash
python src/v2_generador_seguro.py
```

El programa solicita la longitud de la contraseña y aplica una longitud mínima de **12 caracteres**.

> [!WARNING]
> La versión ubicada en `legacy/` se conserva únicamente como referencia educativa. Para utilizar el generador, ejecuta la versión disponible en `src/`.

---

## Estructura del proyecto

```text
pass-forge/
├── assets/
│   └── portada-passforge.png
├── legacy/
│   └── v1_generador_base.py
├── src/
│   └── v2_generador_seguro.py
├── .gitignore
├── LICENSE
└── README.md
```

- `legacy/` contiene la implementación original.
- `src/` contiene la versión actual del generador.
- `assets/` almacena los recursos visuales utilizados por el repositorio.

---

## Evolución del proyecto

### v1 — Implementación original

La primera versión utilizaba `random.choice()` para seleccionar los caracteres de la contraseña.

```python
import random

def generador():
    caracter = (
        '@#$_&-+()/*:;!?~`£¢€¥^°%'
        'abcdefghijklmnñopqrstuvwxyz'
        'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        '1234567890'
    )

    acumulador = ''
    entrada = int(
        input('Longitud de la contraseña (mayor a 9 caracteres): ')
    )

    for i in range(0, entrada):
        acumulador += random.choice(caracter)

    print('Su contraseña generada:', acumulador)

generador()
```

### ¿Cuál era el problema?

El módulo `random` de Python utiliza **Mersenne Twister**, un generador pseudoaleatorio adecuado para simulaciones y otros usos generales, pero no está diseñado para generar valores que necesiten ser resistentes frente a predicción.

Una contraseña puede parecer aleatoria visualmente y aun así proceder de una fuente que no es apropiada para este propósito.

Además, la primera implementación:

- no garantiza la presencia de diferentes clases de caracteres;
- mezcla la lógica del generador con `input()` y `print()`;
- tiene margen de mejora en validación y experiencia de uso.

---

## v2 — Implementación mejorada

La segunda versión sustituye `random` por `secrets`.

```python
import secrets
import string

def generador():
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    caracteres = letras + numeros + simbolos

    # longitud mínima: 12
    # generación utilizando secrets
    # validación de diferentes clases de caracteres
```

### `secrets`

`secrets` está diseñado para generar valores que no deberían resultar predecibles, como:

- contraseñas;
- tokens;
- credenciales temporales;
- otros valores sensibles.

Este es el cambio más importante entre ambas versiones.

### Longitud mínima

La versión actual utiliza una longitud mínima de **12 caracteres**.

Si el usuario introduce una longitud inferior, el programa la ajusta al mínimo establecido.

### Reglas de composición

La contraseña generada incluye al menos:

- una letra mayúscula;
- una letra minúscula;
- un número;
- un símbolo.

Estas reglas evitan resultados que, por azar, contengan únicamente una clase de caracteres.

---

## Comparación entre versiones

| Característica | v1 | v2 |
|---|---|---|
| Fuente de aleatoriedad | `random` | `secrets` |
| Tipo de generador | PRNG de propósito general | CSPRNG |
| Longitud mínima | 10 | 12 |
| Mayúsculas | No garantizadas | Garantizadas |
| Minúsculas | No garantizadas | Garantizadas |
| Números | No garantizados | Garantizados |
| Símbolos | No garantizados | Garantizados |
| Uso dentro del proyecto | Referencia educativa | Versión actual |

---

## ¿Por qué no basta con usar más caracteres?

La primera versión ya permitía utilizar un conjunto amplio de caracteres.

Eso aumenta el espacio de combinaciones posibles, pero no resuelve el problema principal: **la fuente de aleatoriedad**.

Aumentar el número de caracteres disponibles no convierte un generador pseudoaleatorio de propósito general en uno criptográficamente adecuado.

Por eso el cambio fundamental de PassForge no fue añadir más símbolos, sino pasar de:

```python
random.choice(...)
```

a una generación basada en:

```python
secrets
```

---

## Ejemplo de ejecución

```text
Longitud de la contraseña: 16

Tu contraseña: ***************
```

La contraseña mostrada arriba es únicamente ilustrativa.

Si se introduce una longitud inferior al mínimo:

```text
Longitud de la contraseña: 8

Por seguridad, ajustaremos la longitud a 12.
Tu contraseña: ************
```

---

## Consideraciones de seguridad

PassForge es principalmente un **proyecto educativo**.

La versión `v2` mejora la implementación original utilizando una fuente de aleatoriedad apropiada para generar valores sensibles, pero el proyecto no pretende sustituir un gestor de contraseñas completo.

Entre otras cosas, un sistema completo de gestión de credenciales también debe considerar aspectos como:

- almacenamiento seguro;
- protección del portapapeles;
- manejo de datos sensibles;
- integración con otros sistemas;
- políticas y requisitos específicos del entorno donde se utilice.

---

## Próximos pasos

Algunas mejoras planteadas para futuras versiones:

- [ ] Permitir seleccionar los conjuntos de caracteres utilizados.
- [ ] Permitir excluir determinados símbolos.
- [ ] Separar mejor la lógica de generación de la interfaz CLI.
- [ ] Añadir validaciones de entrada adicionales.
- [ ] Incorporar pruebas automatizadas.
- [ ] Mejorar la experiencia de uso desde consola.

---

## Aprendizajes del proyecto

PassForge me permitió practicar y reforzar conceptos como:

`Python` · `random` · `secrets` · `string` · `CLI` · `validación` · `aleatoriedad` · `código seguro`

También sirvió como ejercicio para revisar una solución anterior y documentar su evolución en lugar de reemplazarla sin conservar el razonamiento detrás de los cambios.

---

## Autor

**Josué Chacae**

<p>
  <a href="https://josuechacae.dev">
    <img
      src="https://img.shields.io/badge/Portafolio-josuechacae.dev-0f766e?style=flat-square"
      alt="Portafolio"
    />
  </a>
  <a href="https://www.linkedin.com/in/chacae-josue">
    <img
      src="https://img.shields.io/badge/LinkedIn-Josué_Chacae-0A66C2?style=flat-square&logo=linkedin&logoColor=white"
      alt="LinkedIn"
    />
  </a>
  <a href="https://github.com/chacaejosue">
    <img
      src="https://img.shields.io/badge/GitHub-chacaejosue-181717?style=flat-square&logo=github&logoColor=white"
      alt="GitHub"
    />
  </a>
</p>

---

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).

Puedes utilizarlo, modificarlo y distribuirlo respetando los términos de la licencia.
