from notas_model import NotasModel
from vista_notas import VistaNotas
from controlador_notas import ControladorNotas

if __name__ == "__main__":
    modelo = NotasModel()
    vista = VistaNotas()  # Creamos la vista sin pasar el controlador
    controlador = ControladorNotas(modelo, vista)
    vista.set_controlador(controlador)  # Ahora configuramos el controlador en la vista
