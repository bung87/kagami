import os
import commands
from six.moves.configparser import RawConfigParser,ParsingError,NoSectionError,NoOptionError,DuplicateSectionError

support_os_name = ['nt','posix','mac']

if os.name not in support_os_name:
    raise Exception

conf_path = globals().get('f',None)
if not conf_path:
    #Inside a virtualenv:
    VIRTUAL_ENV = os.environ.get('VIRTUAL_ENV',None)
    vir_path = [r'%VIRTUAL_ENV%\pip.ini','$VIRTUAL_ENV/pip.conf','$VIRTUAL_ENV/pip.conf']
    vir_path_map = dict(zip(support_os_name,vir_path))

    #Per-user:
    path = ['$HOME/.config/pip/pip.conf','$HOME/Library/Application Support/pip/pip.conf','%APPDATA%\pip\pip.ini']
    path_map = dict(zip(support_os_name,path))

    conf_path = vir_path_map[os.name] if VIRTUAL_ENV else path_map[os.name]

    code,r = commands.getstatusoutput("echo %s" % conf_path)
    if code != 0:
        raise Exception(r)
    else:
        conf_path = r

    basedir = os.path.dirname(r)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

resource_dir =  globals()['RESOURCE_DIR']
temp_conf = os.path.join(resource_dir,'python/pip/pip.conf')

config_parser = RawConfigParser()
SECTION_NAME = 'global'
OPTION_NAME = 'index-url'
OPTION_VALUE = 'http://pypi.douban.com/simple/'

with open(conf_path,'w+') as f:
    config_parser.readfp(f)
    if not config_parser.has_section(SECTION_NAME):
        config_parser.add_section(SECTION_NAME)
    if not config_parser.has_option(SECTION_NAME, OPTION_NAME) or config_parser.get(SECTION_NAME, OPTION_NAME)!=OPTION_VALUE:
        config_parser.set(SECTION_NAME,OPTION_NAME,OPTION_VALUE)
    config_parser.write(f) 

