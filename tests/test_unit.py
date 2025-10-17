import pytest
from src.agenda import AgendaTelefonica

@pytest.fixture


def agenda():
    """Crea una agenda vacía para usar en las pruebas."""
    return AgendaTelefonica()

def test_agregar_contacto(agenda):
    """Prueba agregar contactos válidos e inválidos."""
    # Caso válido
    agenda.agregar_contacto("Juan Perez", "0987654321")
    assert "Juan Perez" in agenda.contactos
    assert agenda.contactos["Juan Perez"] == "0987654321"

    # Nombre inválido
    with pytest.raises(ValueError, match="solo puede contener letras y espacios"):
        agenda.agregar_contacto("Juan123", "0987654321")

    # Teléfono inválido
    with pytest.raises(ValueError, match="10 dígitos"):
        agenda.agregar_contacto("Maria Lopez", "12345")


def test_consultar_contacto(agenda):
    """Prueba consultar contactos existentes y no existentes."""
    # Caso válido
    agenda.agregar_contacto("Pedro Gómez", "0991234567")
    resultado = agenda.consultar_contacto("Pedro Gómez")
    assert "0991234567" in resultado

    # Caso inexistente
    resultado = agenda.consultar_contacto("No Existe")
    assert "No se encontró" in resultado


def test_eliminar_contacto(agenda, capsys):
    """Prueba eliminar contactos existentes y no existentes."""
    # Caso válido
    agenda.agregar_contacto("Laura Ruiz", "0912345678")
    agenda.eliminar_contacto("Laura Ruiz")
    captured = capsys.readouterr()
    assert "eliminado correctamente" in captured.out
    assert "Laura Ruiz" not in agenda.contactos

    # Caso inexistente
    agenda.eliminar_contacto("Fantasma")
    captured = capsys.readouterr()
    assert "No se encontró" in captured.out
