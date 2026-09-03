import os

# Langue par défaut
BABEL_DEFAULT_LOCALE = "fr"

# Sécurité
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "ADMVALUE_SUPERSET_KEY")

# Connexion DB interne
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@host:5432/superset_meta"
