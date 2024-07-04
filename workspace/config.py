import os


class DevelopmentConfig:
    # Development configurations
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'seven_infrastructure'
    # Add other development configurations here


class ProductionConfig:
    # Production configurations
    DEBUG = False
    # Add other production configurations here


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}