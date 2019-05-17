class Config(object):
    """base config"""

class ProdConfig(Config):
    """prodcution config"""
    ENV = 'production'
    DEBUG = False

class DevConfig(Config):
    """development config"""
    ENV = 'development'
    DEBUG = True

class TestConfig(Config):
    """test config"""
    ENV = 'test'
    TESTING = True
    DEBUG = True
