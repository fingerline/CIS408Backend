import os

from .base import *
if os.getenv('MYPROJECT') == 'dev':
    from .dev import *
else:
    from .prod import *