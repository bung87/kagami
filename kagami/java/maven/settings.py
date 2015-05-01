import commands
import os
from xml.dom.minidom import parse, parseString,Comment
import shutil
from kagami.settings import kagami_resources

code,r = commands.getstatusoutput("mvn -v|awk -F ':' '{if($1==\"Maven home\"){print $2}}'")
if code != 0:
    raise Exception(r)

settings_file = 'conf/settings.xml'
settings_path = os.path.join(r.strip(),settings_file)

osc_main_mirror = kagami_resources.read(os.path.join('java/maven/mirrors/nexus-osc.xml'))
osc_thirdparty_mirror = kagami_resources.read(os.path.join('java/maven/mirrors/nexus-osc-thirdparty.xml'))
osc_profile = kagami_resources.read(os.path.join('java/maven/profiles/osc.xml'))

osc_main_mirror_url,\
osc_thirdparty_mirror_url =\
'http://maven.oschina.net/content/groups/public/',\
'http://maven.oschina.net/content/repositories/thirdparty/'

def main():
    # parse  settings xml
    settings = parse( settings_path )

    backup()
    processing_mirrors(settings)
    processing_profiles(settings)
    save(settings,settings_path)

# parse osc_main_mirror xml
def parse_osc_main_mirror():
    osc_main_mirror = parse(osc_main_mirror)
    return osc_main_mirror.documentElement

# parse osc_thirdparty_mirror xml
def parse_osc_thirdparty_mirror():
    osc_thirdparty_mirror = parse(osc_thirdparty_mirror)
    return osc_thirdparty_mirror.documentElement

def processing_mirrors(settings):
    osc_main_mirror_exist,osc_thirdparty_mirror_exist = False,False
    mirrors = settings.getElementsByTagName('mirrors')
    if mirrors:
        mirrors =mirrors[0]
        for mirror in mirrors.getElementsByTagName('mirror'):
            url_element = mirror.getElementsByTagName('url')[0]
            url = url_element.childNodes[0].nodeValue
            if url ==osc_main_mirror_url:
                osc_main_mirror_exist = True
            elif url == osc_thirdparty_mirror_url:
                osc_thirdparty_mirror_exist = True
        if not osc_main_mirror_exist:
            mirrors.appendChild(parse_osc_main_mirror())
        if not osc_thirdparty_mirror_exist:
            mirrors.appendChild(parse_osc_thirdparty_mirror())

    else:
        # doc_childs = settings_doc.childNodes
        # for c in doc_childs:
        #     if c.nodeType = Comment.nodeType
        frag = settings.createDocumentFragment()
        tem_mirrors = settings.createElement('mirrors')
        tem_mirrors.appendChild(parse_osc_main_mirror())
        tem_mirrors.appendChild(parse_osc_thirdparty_mirror())
        frag.appendChild(tem_mirrors)
        settings.appendChild(frag)
def processing_profiles(settings):
    profiles = settings.getElementsByTagName('profiles')[0]
    if profiles:
        profile_elements = profiles.getElementsByTagName('profile')
        if profile_elements:
            raise NotImplementedError
        else:
            tem_profile = parse( osc_profile )
            profiles.appendChild(tem_profile.documentElement)
    else:
        frag = settings.createDocumentFragment()
        tem_profiles = settings.createElement('profiles')
        tem_profile = parse( osc_profile )
        tem_profiles.appendChild(tem_profile.documentElement)
        frag.appendChild(tem_profiles)
        settings.appendChild(frag)
def backup():
    if os.path.isfile(settings_path):
        shutil.copy2 (settings_path, settings_path+'.bak')

def save(settings,path):
    settings.writexml(file(path,'w'))

main()