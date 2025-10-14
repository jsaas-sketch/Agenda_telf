import pytest
from src.agenda import AgendaTelefonica

@pytest.fixture #crear datos comunes que se reutilizan en varias pruebas.
def agenda():
    """Crea una agenda vacía para las pruebas de integración."""
    return AgendaTelefonica()

def test_flujo_completo_agenda(agenda, capsys):
    """
    Prueba de integración:
    Verifica que agregar, consultar, eliminar y mostrar trabajen correctamente juntos.
    """
    # === Agregar varios contactos ===
    agenda.agregar_contacto("Juan Perez", "0987654321")
    agenda.agregar_contacto("Maria Lopez", "0991234567")
    agenda.agregar_contacto("Carlos Diaz", "0911112222")
    assert len(agenda.contactos) == 3

    # === Consultar un contacto existente ===
    resultado = agenda.consultar_contacto("Maria Lopez")
    assert "0991234567" in resultado

    # === Consultar un contacto inexistente ===
    resultado = agenda.consultar_contacto("Pedro Gomez")
    assert "No se encontró" in resultado

    # === Eliminar un contacto ===
    agenda.eliminar_contacto("Maria Lopez")
    captured = capsys.readouterr()
    assert "eliminado correctamente" in captured.out
    assert "Maria Lopez" not in agenda.contactos

    # === Intentar eliminar un contacto inexistente ===
    agenda.eliminar_contacto("Pedro Gomez")
    captured = capsys.readouterr()
    assert "No se encontró" in captured.out

    # === Validar estado final de la agenda ===
    assert len(agenda.contactos) == 2
    assert set(agenda.contactos.keys()) == {"Juan Perez", "Carlos Diaz"}