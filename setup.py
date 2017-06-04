from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
setup(
  options = {
    'py2exe' : {
        'compressed': 1,
        'optimize': 2,
        'bundle_files': 1, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist\\v003',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        }
        },
  zipfile=None,
  console = ['getStatus.py'],
)
