"""
    Module for config , vars
"""
from envparse import Env

env = Env(
    ELASTICSEARCH_HOST=str,
    ELASTICSEARCH_USER=dict(cast=str, default='elastic'),
    ELASTICSEARCH_PASSWORD=str,
    ELASTICSEARCH_SSL=dict(cast=bool, default=True),
    EMAIL_DOMAIN=str,
    EMAIL_USER=dict(cast=str, default='josephfranckmarc@gmail.com'),
    EMAIL_PASS=str,
    TO=dict(cast=list, default='walidlwaraq@gmail.com'),
    PAGE_SMS=dict(cast=bool, default=True),
    IPTOEARTH_API_KEY=str,
)
env.read_envfile()


# Elastic search configuration -------

# HOST = "https://6a5e284d512b822bb1b259a620352f2c.eu-west-1.aws.found.io:9243"

# host of the cluster
ELASTICSEARCH_HOST = env('ELASTICSEARCH_HOST')

# the user of the cluster
ELASTICSEARCH_USER = env('ELASTICSEARCH_USER')

# the password of the cluster
ELASTICSEARCH_PASSWORD = env('ELASTICSEARCH_PASSWORD')

# use ssl in auth to the cluster
ELASTICSEARCH_SSL = env('ELASTICSEARCH_SSL')

# End -------

# Email send provider configuration

EMAIL_USER = env('EMAIL_USER')

EMAIL_PASS = env('EMAIL_PASS')

TO = env('TO')

PAGE_SMS = env('PAGE_SMS')

IP_TO_EARTH_KEY = env('IPTOEARTH_API_KEY')
