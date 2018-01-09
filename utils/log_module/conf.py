from configure import ProductionConfig

__conf = ProductionConfig()

log_config = {
    'loggers': {
        'app': {
            'level': 'INFO',
            'propagate': False,
            'handlers': [
                'handler_error',
                'handler_debug',
                'handler_info'
            ]
        }
    },
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'handler_error': {
            'formatter': 'simple',
            'backupCount': 7,
            'level': 'ERROR',
            'interval': 1,
            'when': 'midnight',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': __conf.BASE_DIR + '/logs/error.log'},
        'handler_debug': {
            'formatter': 'simple',
            'backupCount': 7,
            'level': 'DEBUG',
            'interval': 1,
            'when': 'midnight',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': __conf.BASE_DIR + '/logs/debug.log'
        },
        'handler_info': {
            'formatter': 'simple',
            'backupCount': 7,
            'level': 'INFO',
            'interval': 1,
            'when': 'midnight',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': __conf.BASE_DIR + '/logs/info.log'
        }
    },
    'root': {
        'level': 'NOTSET',
        'handlers': ['handler_info']
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(funcName)s:%(lineno)s] [%(levelname)s] %(message)s'
        },
        'full': {
            'format': '%(asctime)s [%(levelname)s] [%(funcName)s:%(lineno)s] %(process)d %(thread)d %(message)s'
            }
        }
    }
