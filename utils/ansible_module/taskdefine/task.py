from configure import ProductionConfig


class CopyFile(object):


    def __init__(self, filename):
        self.filename = filename
        self.conf = ProductionConfig()

    def get_task(self):

        return {
            'name': 'copy file: ' + self.filename,
            'action': {
                'module': 'copy',
                'args': 'src=' + self.conf.LOCAL_PATCH_DIR + self.filename + ' dest=' + self.conf.REMOTE_PATCH_DIR + ' force=yes mode=0644 '
                                                                             'owner=user00'
            }
        }


class ExecTCM(object):

    def __init__(self, command):
        self.conf = ProductionConfig()
        self.command = command

    def get_task(self):

        return {
            'name': 'RUN  ./tcmconsole -O ' + str(self.command),
            'action': {
                'module': 'shell',
                'args': './tcmconsole -O ' + '"' + str(self.command) + '"' + ' chdir=' + self.conf.TCM_COMMAND_DIR
            }
        }


