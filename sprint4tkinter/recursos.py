import requests
from PIL import Image, ImageTk
import io
from requests import RequestException

def descargar_imagen(url, size):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))

        image = image.resize(size, Image.ANTIALIAS)

        return ImageTk.PhotoImage(image)
    except RequestException:
        print(f"Error: URL no válida -> {url}")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
    return None
