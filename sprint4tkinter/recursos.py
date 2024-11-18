import requests
import PIL
import io

from PIL import Image
from requests import RequestException


def descargar_imagen(url, size):
    response =requests.get(url)
    try:
        response.raise_for_status()


    except RequestException:
        print("Error, url no válida: "+url)
        return None

