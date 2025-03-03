# Validadores Personalizados en Pydantic

Además de la validación automática basada en anotaciones de tipo, Pydantic nos permite crear validadores personalizados para definir reglas de validación más específicas. 
Esto es muy útil cuando:
- necesitamos validar datos que no se pueden validar simplemente con los tipos de datos básicos.
- necesitamos agregar restricciones adicionales a los campos de nuestro modelo.

## Validadores de Campo (@field_validator)
Los validadores de campo, decorados con `@field_validator`, se utilizan para validar campos individuales de un modelo. Se ejecutan después de que Pydantic ha realizado la validación básica de tipos.
Por ejemplo, podemos usar un validador de campo para asegurarnos de que un nombre de usuario cumpla con ciertos criterios, como longitud mínima y caracteres permitidos.

## Validadores de Modelo (@model_validator)
Los validadores de modelo, decorados con @model_validator, se utilizan para validar el modelo en su conjunto, permitiéndonos realizar validaciones que involucran múltiples campos.
Por ejemplo, podemos usar un validador de modelo para verificar que la contraseña de un usuario no contenga su nombre de usuario.

## Potencia de los Validadores Personalizados
Pydentic tiene dos formas basicas de enriquecer y reforzar los tipos y sus validaciones
+ Validación de campos: **@fieldvalidator**
+ Validación de modelos: **@model_validator**

Tal como su nombre sugiere:
- Con @fieldvalidator se pueden configurar métodos que refuercen (agreguén restricciones y características) a un campo una clase.
- Con @model_validator se pueden configurar métodos que refuercen varios campos de manera combinada.

Entonces con fieldvalidator se puede controlar que un campo cumpla con ciertas características. 
    Es decir se controla la validez campo a campo.
Y con model_validator se puede controlar que varios campos cumplan con ciertas características. 
    Es decir se puede controlar la instancia completa de una clase.

Por ejemplo para el caso de un loguin de un usuario en un sitema:
- Con @fieldvalidator podría enviar un mensaje al usuario que luego de no ingresar el nombre de usuario diga:
    - "el usuario no puede ser nulo, debe cargar un nombre de usuario"
- Con @model_validator podría enviar un mensaje que diga al usuario: "Usuario o password incorrecto" 
    - después de chequear con logica 'or' ambos campos y para no dar presiciones que afecten la seguridad de una cuenta.

En el archivo ..................... se puede ver un ejemplo de como se puede usar @fieldvalidator y @model_validator.

Para el caso de @fieldvalidator se controla que el formato del nombre sea el correcto.
```python
    @field_validator('name')
    def validate_name(value: str) -> str:
        if not VALID_NAME_REGEX.match(value):
            raise ValueError(
                "Nombre invalido: debe contener solo letras y tener al menos 2 caracteres"
            )
        return value
´´´

Para el caso de @model_validator se controla dos campos de manera combinada: nombre de usuario y password.
Esto se hace con el objeto de verificar que la password y el nombre de usuario no sean nulos pero ademas,
que la password no contenga el nombre de usuario.
```python
    @model_validator(mode="before")                      
    def validate_user_pre(v: dict[str, any]) -> dict[str, any]:
        if "name" not in v or "password" not in v:
            raise ValueError("Nombre y contraseña son obligatorios")
        if v["name"].casefold() in v["password"].casefold():
            raise ValueError("La clave no puede contener el nombre")
        if not VALID_PASSWORD_REGEX.match(v["password"]):
            raise ValueError(
                "Clave Invalida: debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un dígito"
            )
        v["password"] = hashlib.sha256(v["password"].encode()).hexdigest()
        return v
´´´
Cabe destacar que el uso de @model_validator lleva consigo la especificación de si este control se ejecuta antes o después de la validación de los campos propia de pydantic.
```python
    @model_validator(mode="before")                      
    def validate_user_pre(v: dict[str, any]) -> dict[str, any]:
´´´
Por esta razón, se puede ver que en el ejemplo anterior se especifica que se ejecute antes de la validación de los campos.
En consecuencia, si los datos son correctos entonces se inicializa una instancia de la clase sin problemas.
```python
    user = User(name="Juan", password="12345678Aa"....
´´´
- Si los datos no son correctos entonces se informarán dos errores, uno manejado que indica que la clave no puede contener el nombre.
    - Acto segguido otro que da error al intentar inicializar una instancia de la clase (esto porque los datos están mal).
- Si los datos son correctos entonces se encodifica la password con hashlib.sha256
    - Y se inicializa una instancia de la clase sin problemas.


