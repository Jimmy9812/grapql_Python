from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from resolvers.query import query

# Cargar esquema desde el archivo schema.graphql
type_defs = load_schema_from_path("schema.graphql")

# Crear esquema ejecutable
schema = make_executable_schema(type_defs, query)

# Configurar servidor GraphQL
app = GraphQL(schema, debug=True)
