import os

from .base import *
if os.environ['myproject'] == 'dev':
    from .dev import *
else:
    from .prod import *