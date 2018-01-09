#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conf import log_config
import logging
import logging.config


class LogManager():
    def __init__(self, logger_name):
        self.logger_name = logger_name

    def get_logger(self):
        logger = None
        try:
            logging.config.dictConfig(log_config)
            logger = logging.getLogger(self.logger_name)
        except Exception as err:
            print err
            pass
        return logger