import ConfigParser

class Config_parse(object):
    def __init__(self):
        self.config_file = './yhnote.conf'
        self.config = ConfigParser.ConfigParser()

    def parse(self):
        self.config.readfp(open(self.config_file, "rb"))

        self.db_host = self.config.get('DB', 'host')
        self.db_user = self.config.get('DB', 'user')
        self.db_passwd = self.config.get('DB', 'passwd')
