
from ariadne import QueryType

query = QueryType()

@query.field("hello")
def resolve_hello(*_):
    return "¡Hola, Mundo desde GraphQL!"

@query.field("user")
def resolve_user(*_, id):
    # Simulando un usuario
    users = {
        "1": {"id": "1", "name": "Juan Pérez", "email": "juan.perez@example.com"},
        "2": {"id": "2", "name": "María López", "email": "maria.lopez@example.com"},
    }
    return users.get(id)
