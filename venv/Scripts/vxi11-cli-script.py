#!"C:\Users\Liam Droog\PycharmProjects\StanfordBox\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'python-vxi11==0.9','console_scripts','vxi11-cli'
__requires__ = 'python-vxi11==0.9'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-vxi11==0.9', 'console_scripts', 'vxi11-cli')()
    )
