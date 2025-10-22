import re

# Utilidades de validación
# Nota: No se usa en los endpoints (intencionado para que el candidato lo note).

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")  # simplista

def is_valid_email(email: str) -> bool:
    # TODO: mejorar validación (dominios, TLD, etc.)
    return bool(EMAIL_REGEX.match(email))