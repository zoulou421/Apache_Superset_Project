import os

# 🌍 Langue par défaut
BABEL_DEFAULT_LOCALE = "fr"

# 🔑 Clé de sécurité (lue depuis ton .env)
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "changeme")

# 🗄️ Base interne Superset (métadonnées, utilisateurs, dashboards)
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:///superset.db"  # fallback si rien n'est défini
)

# 📊 Paramètres de cache (optionnel)
CACHE_CONFIG = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

# 🔐 Sécurité et authentification
AUTH_ROLE_PUBLIC = "Gamma"  # rôle par défaut pour les utilisateurs non connectés
ENABLE_PROXY_FIX = True     # utile si tu déploies derrière un proxy/Nginx

# 📈 Paramètres divers
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,   # permet d’intégrer des dashboards dans des apps externes
    "DASHBOARD_NATIVE_FILTERS": True,  # filtres modernes
}

#🔎 Explications
# BABEL_DEFAULT_LOCALE → met l’interface Superset en français.

# SECRET_KEY → lu depuis ton .env (sécurité des sessions).

# SQLALCHEMY_DATABASE_URI → connexion à la base interne Superset (PostgreSQL recommandé, mais SQLite possible pour test).

# CACHE_CONFIG → améliore les performances en mettant en cache certaines requêtes.

# AUTH_ROLE_PUBLIC → définit le rôle par défaut des utilisateurs non authentifiés.

# FEATURE_FLAGS → active des fonctionnalités modernes (filtres natifs, intégration).
