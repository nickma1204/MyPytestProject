from configparser import ConfigParser


class ConfigHandler(ConfigParser):

    def __init__(self, configpath):
        self.configpath = configpath

    def readconf(self, section, option):
        cp = ConfigParser()
        cp.read(self.configpath, encoding='utf-8')
        value = cp.get(section, option)
        return value


confvalue = ConfigHandler('../confs/conf.ini')

if __name__ == '__main__':
    cp = ConfigHandler('../confs/conf.ini')
    str = cp.readconf('api', 'mapurl')
    print(str)
