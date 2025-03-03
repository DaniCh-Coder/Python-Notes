#----------------------------------------------------------------------------------------#
# Tipos de datos de python y pydantic
#----------------------------------------------------------------------------------------#
from pydantic import (
    BaseModel, 
    SecretStr, 
    EmailStr,
    ValidationError,
    Field, 
    field_validator, 
    model_validator 
)
import hashlib
from typing import Annotated
from enum import auto, IntFlag
import re

VALID_PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")
# ^ - Indica el inicio de la cadena
# (?=.*[a-z]) - Es un "lookahead positivo" que verifica que haya al menos una letra minúscula en cualquier parte de la cadena
# (?=.*[A-Z]) - Otro "lookahead positivo" que verifica que haya al menos una letra mayúscula
# (?=.*\d) - Un tercer "lookahead positivo" que verifica que haya al menos un dígito
#.{8,} - Coincide con cualquier carácter (excepto saltos de línea), y el {8,} indica que debe haber al menos 8 caracteres
# $ - Indica el final de la cadena

VALID_NAME_REGEX = re.compile(r"^[a-zA-Z]{2,}$")
# r"^[a-zA-Z]{2,}$" - Es la expresión regular en sí, con los siguientes elementos:
# r - Es un prefijo de string "raw" (crudo) en Python, que evita que los caracteres de escape como \ sean interpretados por Python.
# ^ - Indica el inicio de la cadena.
# [a-zA-Z] - Define un conjunto de caracteres que incluye todas las letras, tanto mayúsculas como minúsculas (a-z y A-Z).
# {2,} - Es un cuantificador que especifica que el elemento anterior (el conjunto de letras) debe aparecer al menos 2 veces, sin límite máximo.
# $ - Indica el final de la cadena.


# Clase complementaria que define roles posibles para una 'Persona'
# Utiliza como clase base IntFlag que es un tipo propio de python.
class Role(IntFlag):
    Author = auto()                                     # asigna un valor univoco a autor
    Editor = auto()                                     # asigna un valor univoco a editor
    Developer = auto()                                  # asigna un valor univoco a developer
    Admin = Author | Editor | Developer                 # admin podrá ser uno de los tres anteriores

# Definición de una clase 'Persona' tulizando dipos de datos de pydantic 2.0
# BaseModel implementa todas las bases de los controles y validaciones de los tipos de datos (python y propios de pydantic)
class Persona(BaseModel):
    name: Annotated[str, Field(min_length=1)]           # pydantic: min_lenth, especifica restricción de longitud mínima
    account_id: Annotated[int, Field(gt=0)]             # pydantic: gt, especifica mayor que
    email: Annotated[EmailStr, Field(                   # pydantic: EmailStr, que define un tipo de datos especial para e-mail
        examples=["dani@some-email.com"],               # pydantic: exapmples, opcional para contener un ejemplo
        description="The email address of the user",    # pydantic: desciption, opcional para aclarar de que se trata un dato
        frozen=True                                     # pydantic: fronzen, fuerza un valor en un dato que no se puede cambiar durante la app
    )]
    password: Annotated[SecretStr, Field(               # pydantic: SecretStr, tipo de dato para almacenar y ocultar el contenido de un campo.
        examples=["Password123"],
        description="The password of the user"
    )]
    role: Annotated[Role, Field(                        # python: utiliza un tipo de datos previamente definido en la clase 'Role'
        default=Role.Author,
        description="The role of the user"
    )]

    # Método de validación de datos de la clase 'Persona' para name
    @field_validator('name')
    def validate_name(value: str) -> str:
        if not VALID_NAME_REGEX.match(value):
            raise ValueError(
                "Nombre invalido: debe contener solo letras y tener al menos 2 caracteres"
            )
        return value
   
    # Método de validación de datos de la clase 'Persona' para password
    # No es necesario porque ya se hace en el model_validator before
    
    # pydantic: model_validator, valida datos antes de la creación de la instancia
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
    
    @model_validator(mode="after")
    def validate_user_post(v: dict[str, any]) -> dict[str, any]:
        if "role" == Role.Admin and "name" != "Dani":
            raise ValueError("Solo Dani puede ser admin")
        return v
    
    
# ----------------------------------------------------------------------------------------------#
# Código de testeo en tiempo de ejecución                                                       #
# ----------------------------------------------------------------------------------------------#
def validate(data: dict[str, any]) -> Persona:
    try:
        user = Persona.model_validate(data)
        print(user)
    except ValidationError as e:
        print("User is invalid:")
        print(e)
    return user

def main() -> None:
    # Setea un dicionario para validar datos ok
    good_data = {                                   
        "name": "Tulio",
        "account_id":456,
        "email": "example@maildomain.com",
        "password": "Password123"
    }
    
    user= validate(good_data)
    
    if user:
        print(
            "Contenido del objeto 'user':",
            user.model_dump(),
            sep="\n",
            end="\n\n",
        )    
    
# Si quito el comentario de las siguientes líneas, para cargar una password que contiene el nombre de usuario
# se generará una excepción de validación de datos
#
    # Setea un diccionario con una password que incluye el nombre
#    bad_data = {
#        "name": "Tulio",
#        "account_id": 456,
#        "email": "example@maildomain.com",
#        "password": "Tulio123"
#    }
#    user = validate(bad_data)
    
if __name__ == "__main__":
    main()    
   