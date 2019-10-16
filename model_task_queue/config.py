"""Configuration settings for the celery application."""


class Config(object):
    """Configuration for all environments."""

    models = [
        {
            "module_name": "iris_model.iris_predict",
            "class_name": "IrisModel"
        }
    ]


class ProdConfig(Config):
    """Configuration for the prod environment."""

    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'


class BetaConfig(Config):
    """Configuration for the beta environment."""

    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'


class TestConfig(Config):
    """Configuration for the test environment."""

    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'


class DevConfig(Config):
    """Configuration for the dev environment."""

    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'
