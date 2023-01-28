import os

from flask_sslify import SSLify

from dotenv import load_dotenv

from smk import create_app

env = os.environ.get('APP_ENV', 'dev')

app = create_app(config_name=env)

if __name__ == "__main__":

    if env == 'dev':
        load_dotenv()
        sslify = SSLify(app, subdomains=True)
        app.run(debug=True, ssl_context=('devcert.pem','devkey.pem'))
    elif env == "test":
        load_dotenv()
        sslify = SSLify(app, subdomains=True)
        app.run(ssl_context=('cert.pem', 'key.pem'))
    elif env == "production":
        sslify = SSLify(app, subdomains=True)
        app.run(ssl_context=('cert.pem', 'key.pem'), port=443)
    else:
        app = None
        raise ValueError('Invalid environment')
    
    
