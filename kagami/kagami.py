#!/usr/bin/env python
import os
import argparse
import textwrap
import commands

from settings import kagami_resources

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

    for t in ns.apps:

        if t == 'maven':
            exec(kagami_resources.read(os.path.join('java','maven','settings.py')),config)
        elif t == 'android':
            exec(kagami_resources.read(os.path.join('java','android','sdk.py')),config)
        elif t == 'npm':
            code,r = commands.getstatusoutput("bash %s" % kagami_resources.read(os.path.join('js','npm','registry.sh')) )
            if code != 0:
                raise Exception(r)
        elif t == 'pypi':
            passvar = config.copy()
            passvar.update({'f':ns.f})
            exec(kagami_resources.read(os.path.join('python','pip','repository.py')),config)
        elif t == 'gem':
             code,r = commands.getstatusoutput("bash %s" % kagami_resources.read(os.path.join('ruby','gem','sources.sh') ))
             if code != 0:
                 raise Exception(r)
        elif t == 'bundle':
            passvar = config.copy()
            passvar.update({'f':ns.f})
            exec(kagami_resources.read(os.path.join('ruby','bundle','config.py')),passvar)
if __name__ =='__main__':
    main()