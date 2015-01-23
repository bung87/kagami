#!/usr/bin/env python
import os
import argparse
import textwrap
import commands
import settings

apps = ['android','maven','npm','pypi','gem','bundle']

parser = argparse.ArgumentParser(prog='./kagami.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('Programmer tools with Chinese features.\n')
    )
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

subparsers = parser.add_subparsers(title='Commands',

help=False
)

parser_forward = subparsers.add_parser('forward')
# parser_backward = subparsers.add_parser('backward')

parser_forward.add_argument('forward',action='store',type=str,choices=apps,nargs='+')
parser_forward.add_argument('-f',action='store',type=str)
# parser_backward.add_argument('backward',action='store',type=str,choices=apps)

config = dict([ (key, getattr(settings, key))for key in dir(settings) if key.isupper()])

ns = parser.parse_args()
for t in ns.forward:

    if t == 'maven':
        execfile(os.path.join(settings.BASE_DIR,'java','maven','settings.py'),config)
    elif t == 'android':
        execfile(os.path.join(settings.BASE_DIR,'java','android','sdk.py'),config)
    elif t == 'npm':
        code,r = commands.getstatusoutput("bash %s" % os.path.join(settings.BASE_DIR,'js','npm','registry.sh') )
        if code != 0:
            raise Exception(r)
    elif t == 'pypi':
        passvar = config.copy()
        passvar.update({'f':ns.f})
        execfile(os.path.join(settings.BASE_DIR,'python','pip','repository.py'),config)
    elif t == 'gem':
         code,r = commands.getstatusoutput("bash %s" % os.path.join(settings.BASE_DIR,'ruby','gem','sources.sh') )
         if code != 0:
             raise Exception(r)
    elif t == 'bundle':
        passvar = config.copy()
        passvar.update({'f':ns.f})
        execfile(os.path.join(settings.BASE_DIR,'ruby','bundle','config.py'),passvar)