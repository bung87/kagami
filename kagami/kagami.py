#!/usr/bin/env python
import os
import argparse
import textwrap
import commands
import zipfile
import subprocess

apps = ['android','maven','npm','pypi','gem','bundle']
actions = ['forward','backward']
def main():
    parser = argparse.ArgumentParser(prog='kagami',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('Programmer tools with Chinese features.\n')
        )
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    subparsers = parser.add_subparsers(title='Commands',

    help=False
    )

    parser_forward = subparsers.add_parser('forward')
    # parser_backward = subparsers.add_parser('backward')
    # parser_forward.add_argument('action',action='store',type=str,choices=apps,nargs='+')
    parser_forward.add_argument('apps',action='store',type=str,choices=apps,nargs='+')
    parser_forward.add_argument('-f',action='store',type=str)
    # parser_backward.add_argument('backward',action='store',type=str,choices=apps)

    config = vars(parser.parse_args())
    sh = os.environ.get('SHELL')
    sh_profile = '~/.bash_profile'
    if sh and -1 != sh.find('zsh'):
        sh_profile = '~/.zprofile'
    ns = parser.parse_args()
    kagami_resources = None
    if ns.apps:
        kagami_resources = zipfile.ZipFile(os.path.join(os.path.dirname(__file__),"resources.zip"), "r")
    for t in ns.apps:

        if t == 'maven':
            exec(kagami_resources.read(os.path.join('java','maven','settings.py')),config)
        elif t == 'android':
            exec(kagami_resources.read(os.path.join('java','android','sdk.py')),config)
        elif t == 'npm':
            with open(os.path.expanduser(sh_profile),'a') as f:
                f.write(kagami_resources.read(os.path.join('js','npm','registry.sh')))
                print('writing alias "cnpm" to your shell profile')
            print('You may execute commands below for the changes to take effect immediately.')
            print('alias cnpm="npm --registry=https://registry.npm.taobao.org --cache=$HOME/.npm/.cache/cnpm --disturl=https://npm.taobao.org/dist --userconfig=$HOME/.cnpmrc"')
        elif t == 'pypi':
            passvar = config.copy()
            passvar.update({'f':ns.f})
            exec(kagami_resources.read(os.path.join('python','pip','repository.py')),config)
        elif t == 'gem':
             subprocess.check_output(kagami_resources.read(os.path.join('ruby','gem','sources.sh') ),
                stderr=subprocess.STDOUT,
                shell=True
                )
             
        elif t == 'bundle':
            passvar = config.copy()
            passvar.update({'f':ns.f})
            exec(kagami_resources.read(os.path.join('ruby','bundle','config.py')),passvar)
    if kagami_resources:
        kagami_resources.close()
if __name__ =='__main__':
    main()