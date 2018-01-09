# -*- encoding: utf-8 -*-
import  os


class BaseConfig(object):
    BASE_DIR = os.path.dirname(__file__)
    HOST_LISTEN = "0.0.0.0"
    PORT_LISTEN = 9090
    DEBUG = True
    SECRET_KEY = ""
    SECRET_USER = ""
    ANSIBLE_CONFIG = {
        "become": True,
        "become_user": "abcd",
        "become_method": "sudo",
        "remote_user": "up",
        "private_key_file": BASE_DIR + ""
    }


class ProductionConfig(BaseConfig):
    URL_PATCH_DOWNLOAD = ""
    LOCAL_PATCH_DIR = BaseConfig.BASE_DIR + ""
    REMOTE_PATCH_DIR = ""
    TCM_COMMAND_DIR = ""
    HOST_GAME = ["172.31.0.101",
                    "172.31.0.102",
                    "172.31.0.111",
                    "172.31.0.112",
                    "172.31.0.121",
                    "172.31.0.122",
                    "172.31.0.131",
                    "172.31.0.132",
                    "172.31.0.133",
                    "172.31.0.151",
                    "172.31.0.152",
                    "172.31.0.153",
                    "172.31.0.154",
                    "172.31.0.155",
                    "172.31.0.156"
                    ]
    HOST_TCM = ["172.31.0.12"]