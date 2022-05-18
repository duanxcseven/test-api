from configparser import ConfigParser
from common.handler_path import conf_dir
import os

class Conf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf-8')


conf = Conf(os.path.join(conf_dir,'wczj.ini'))
