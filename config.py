import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY")
  #-----------------------------------------------------    
  # Recaptcha config 
  #-----------------------------------------------------    
  RECAPTCHA_USE_SSL = True 
  RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY") 
  RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
  RECAPTCHA_OPTIONS = {'theme': 'white'}
  #-----------------------------------------------------    
  # mail config 
  #-----------------------------------------------------    
  MAIL_SERVER = os.environ.get("MAIL_SERVER") 
  MAIL_PORT = os.environ.get("MAIL_PORT") 
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
  @staticmethod
  def init_app(app):
    pass
  
class DevelopmentConfig(Config):
  DEBUG = True
  
class TestingConfig(Config):
  TESTING = True
  WTF_CSRF_ENABLED = False
  
class ProductionConfig(Config):
  TESTING = True
  WTF_CSRF_ENABLED = True
  PREFERRED_URL_SCHEME = 'https'
  SESSION_COOKIE_SECURE = True
  
config = {
  'dev': DevelopmentConfig,
  'test' : TestingConfig,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}