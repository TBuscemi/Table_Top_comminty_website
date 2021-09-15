DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'community_database',
        "USER":'root',
        'PASSWORD':'password',
        'Host':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'autocommit': True
        }
    }   
}