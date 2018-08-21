class Config:
    DEBUG = False
    APP_SECRET = "ju"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}