class AgendaTelefonica:
    def __init__(self):
        """Inicializa un diccionario vacío para almacenar los contactos."""
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        """Agrega un contacto nuevo si pasa las validaciones."""
        if not self._validar_nombre(nombre):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        if not self._validar_telefono(telefono):
            raise ValueError("El número de teléfono debe tener exactamente 10 dígitos.")
        self.contactos[nombre.strip().title()] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")

    def consultar_contacto(self, nombre):
        """Devuelve el número de teléfono de un contacto si existe."""
        nombre = nombre.strip().title()
        if nombre in self.contactos:
            return f"{nombre}: {self.contactos[nombre]}"
        else:
            return f"No se encontró el contacto '{nombre}'."

    def eliminar_contacto(self, nombre):
        """Elimina un contacto existente."""
        nombre = nombre.strip().title()
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"No se encontró el contacto '{nombre}' para eliminar.")

    def _validar_nombre(self, nombre):
        """Valida que el nombre contenga solo letras y espacios."""
        return all(c.isalpha() or c.isspace() for c in nombre)

    def _validar_telefono(self, telefono):
        """Valida que el teléfono tenga exactamente 10 dígitos."""
        return telefono.isdigit() and len(telefono) == 10