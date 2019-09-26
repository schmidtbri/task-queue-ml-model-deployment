"""Configuration settings for the celery application."""

models = [
    {
        "module_name": "iris_model.iris_predict",
        "class_name": "IrisModel"
    }
]


class Config(object):
    """Configuration for all environments."""

    pass


class ProdConfig(Config):
    """Configuration for the prod environment."""

    backend = 'redis://localhost:6379/0',
    broker = 'redis://localhost:6379/0'


class BetaConfig(Config):
    """Configuration for the beta environment."""

    backend = 'redis://localhost:6379/0',
    broker = 'redis://localhost:6379/0'


class TestConfig(Config):
    """Configuration for the test environment."""

    backend = 'redis://localhost:6379/0',
    broker = 'redis://localhost:6379/0'


class DevConfig(Config):
    """Configuration for the dev environment."""

    backend = 'redis://localhost:6379/0',
    broker = 'redis://localhost:6379/0'
