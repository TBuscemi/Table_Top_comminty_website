# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j#xqnw+$42gk$*(zq3rt%js=fm-hn@n!9a*v62sm!oz=ssk8br'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'bag_of_holding',
        "USER":'root',
        'PASSWORD':'R41nbow.uniCORN',
        'Host':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'autocommit': True
        }
    }   
}