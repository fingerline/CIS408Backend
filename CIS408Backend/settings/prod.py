DEBUG = True

ALLOWED_HOSTS = ['limitless-lake-64230.herokuapp.com', '127.0.0.1']

DATABASES = {
    'default': {
    }
}
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)