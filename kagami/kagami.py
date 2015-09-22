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
            subprocess.check_output(kagami_resources.read(os.path.join('js','npm','registry.sh')),\
                stderr=subprocess.STDOUT,
                shell=True
             )
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