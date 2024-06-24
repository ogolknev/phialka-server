"""
REST api routers based on fastapi
"""
from .files import files_router
from .profile import profile_routers, register_routers
from .authentification import auth_routers