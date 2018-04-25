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
    print('Config located at:"%s"' % conf_path)
    basedir = os.path.dirname(r)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

config_parser = RawConfigParser()
SECTION_NAME = 'global'
OPTION_NAME = 'index-url'
OPTION_VALUE = 'https://pypi.tuna.tsinghua.edu.cn/simple'
# FIND_LINKS_NAME = 'find-links'
# FIND_LINKS_VALUE = '''http://pypi.douban.com
#      https://pypi.tuna.tsinghua.edu.cn
#      http://pypi.v2ex.com/'''

# TRUSTED_NAME = 'trusted-host'
# TRUSTED_VALUE = '''pypi.douban.com
#      pypi.tuna.tsinghua.edu.cn
#      pypi.v2ex.com'''   

with open(conf_path,'w+') as f:
    config_parser.readfp(f)
    if not config_parser.has_section(SECTION_NAME):
        config_parser.add_section(SECTION_NAME)
    if not config_parser.has_option(SECTION_NAME, OPTION_NAME) or config_parser.get(SECTION_NAME, OPTION_NAME)!=OPTION_VALUE:
        config_parser.set(SECTION_NAME,OPTION_NAME,OPTION_VALUE)
    # if not config_parser.has_option(SECTION_NAME, FIND_LINKS_NAME) or config_parser.get(SECTION_NAME, FIND_LINKS_NAME)!=FIND_LINKS_VALUE:
    #     config_parser.set(SECTION_NAME,FIND_LINKS_NAME,FIND_LINKS_VALUE)
    # if not config_parser.has_option(SECTION_NAME,TRUSTED_NAME) or config_parser.get(SECTION_NAME, TRUSTED_NAME)!=TRUSTED_VALUE:
    #     config_parser.set(SECTION_NAME,TRUSTED_NAME,TRUSTED_VALUE)
    config_parser.write(f) 
with open(conf_path,'r') as f:
    content = f.read()
    print("Final configuration:\n%s" % content)

