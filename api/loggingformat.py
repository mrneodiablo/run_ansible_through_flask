class FormatLog():

    def __init__(self, remote_addr, base_url, code, name, description, message):
        self.remote_addr = remote_addr
        self.base_url = base_url
        self.code = code
        self.name = name
        self.description = description
        self.message = message


    def formatter(self):
        return str(self.remote_addr) + '\t' + str(self.base_url) + '\t' + str(self.code) + '\t' + str(self.name) + \
               '\t' + str(self.description) + '\t' + str(self.message)