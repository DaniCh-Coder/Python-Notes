import pandas as pd
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_rename_excel(file_path, new_column_names):
    """
    Lee un archivo Excel y renombra las columnas.

    Args:
        file_path (str): Ruta al archivo Excel.
        new_column_names (list): Lista con los nuevos nombres de las columnas.

    Returns:
        pd.DataFrame o str: DataFrame con los datos del archivo Excel y columnas renombradas,
                            o un mensaje de error en caso de falla.
    """
    try:
        # Leer el archivo Excel, especificando que la primera fila contiene los nombres de columna
        df = pd.read_excel(file_path, header=0)
        logging.info(f"Archivo '{file_path}' leído exitosamente.")

        # Verificar que el número de nuevos nombres de columnas coincida con el número de columnas del DataFrame
        if len(new_column_names) != df.shape[1]:
            raise ValueError("El número de nuevos nombres de columnas no coincide con el número de columnas en el archivo Excel.")
        
        # Renombrar las columnas
        df.columns = new_column_names
        logging.info("Columnas renombradas exitosamente.")
        
        return df
    except FileNotFoundError:
        error_message = f"Error: El archivo '{file_path}' no fue encontrado."
        logging.error(error_message)
        return error_message
    except ValueError as ve:
        error_message = f"Error: {ve}"
        logging.error(error_message)
        return error_message
    except Exception as e:
        error_message = f"Se produjo un error inesperado: {e}"
        logging.error(error_message)
        return error_message
