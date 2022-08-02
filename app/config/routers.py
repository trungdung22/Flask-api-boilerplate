""" Module for swagger collections """
from app.config.server import api
# Remove default namespace
api.namespaces.clear()

user_namespace = api.namespace(
    'Users',
    description='A Collection of User related endpoints',
    path='/users'
)

doctor_namespace = api.namespace(
    'Doctors',
    description='A Collection of Doctor related endpoints',
    path="/doctors"
)
