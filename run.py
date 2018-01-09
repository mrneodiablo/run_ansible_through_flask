from api import app
from configure import ProductionConfig


if __name__ == '__main__':
    conf = ProductionConfig()

    app.run(
            host=conf.HOST_LISTEN,
            port=conf.PORT_LISTEN,
            debug=conf.DEBUG
    )
