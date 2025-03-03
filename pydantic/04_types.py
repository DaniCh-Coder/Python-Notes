#----------------------------------------------------------------------------------------#
# Tipos de datos de python y pydantic
#----------------------------------------------------------------------------------------#
from pydantic import BaseModel, Field, SecretStr, EmailStr,ValidationError
from typing import Annotated
from enum import auto, IntFlag

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


# Ejemplo de uso
persona = Persona(
    name="Daniel",
    account_id=123,
    email="dani@some-email.com",
    password="SuperSecret",
    role=Role.Admin
)
print(persona)

# Primera prueba: si se comenta el código de test que viene a continuación se prueba e imprime el modelo.

# Segunda prueba: se descomenta el código de testeo para validar los datos de entrada.
# ----------------------------------------------------------------------------------------------#
# Código de testeo en tiempo de ejecución                                                       #
# ----------------------------------------------------------------------------------------------#
def validate(data: dict[str, any]) -> None:
    try:
        user = persona.model_validate(data)         # Valida los datos pasados a esta función.
        print(user)
    except ValidationError as e:                    # captura errores para no interrumpir app
        print("El usuario o persona es invalido:")
        for error in e.errors():
            print(error)


def main() -> None:
    # Setea un dicionario para validar datos ok
    good_data = {                                   
        "name": "Tulio",
        "account_id":456,
        "email": "example@maildomain.com",
        "password": "Password123",
    }
    
    # Setea un dicionario para validar datos que no estan ok
    bad_data = {"email": "<bad data>", "password": "<bad data>"}

    # Llama a control de validaciones
    print("\nPrueba de validación de datos OK\n")
    validate(good_data)
    
    print("\nPrueba de validación de datos mal seteados\n")
    validate(bad_data)


if __name__ == "__main__":
    main()
    
#----------------------------------------------------------------------------------------#
# En esta segunda prueba se valida el modelo de datos con datos correctos y con datos incorrectos.
# El código primero valida los datos correctos y luego los incorrectos.
# En el caso de los datos incorrectos se captura el error y se imprime en pantalla.
#----------------------------------------------------------------------------------------#