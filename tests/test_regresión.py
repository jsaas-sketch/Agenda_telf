from src.agenda import AgendaTelefonica
import pytest

@pytest.fixture
def agenda():
    return AgendaTelefonica()


def test_regresion_eliminar_y_consultar(agenda):
    """
    Prueba de regresión:
    Antes, si se eliminaba un contacto y luego se consultaba, 
    podía devolver un error o resultado incorrecto.
    Ahora verificamos que funcione bien.
    """
    # Agregar y eliminar un contacto
    agenda.agregar_contacto("Carlos Diaz", "0991112222")
    agenda.eliminar_contacto("Carlos Diaz")

    # Consultar después de eliminar → debe decir "no se encontró"
    resultado = agenda.consultar_contacto("Carlos Diaz")
    assert "No se encontró" in resultado