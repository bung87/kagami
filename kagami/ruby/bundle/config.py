import yaml
#http://bundler.io/v1.5/bundle_config.html
#BUNDLE_MIRROR__HTTPS://RUBYGEMS.ORG: https://ruby.taobao.org/
import os
from glob import glob
from os.path import expanduser,join

conf_path = globals().get('f',None)
if not conf_path:
    bundle_conf_l = glob('*.bundle/config')
    if bundle_conf_l:
        conf_path = bundle_conf_l[0]
    else:
        conf_path = join(expanduser('~'), '.bundle', 'config')

basedir = os.path.dirname(conf_path)
if not os.path.exists(basedir):
    os.makedirs(basedir)

with open(conf_path,'w+') as f:
    try:
        data = yaml.load(f)
    except IOError:
        data = {}
    data['BUNDLE_MIRROR__HTTPS://RUBYGEMS.ORG'] =' https://ruby.taobao.org/'
    dump_string = yaml.dump(data,explicit_start = True, default_flow_style = False)
    f.write(dump_string)
