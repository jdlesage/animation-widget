from ._version import version_info, __version__

from .widget_timer import *
from .widget_image import *


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'animation-widget',
        'require': 'animation-widget/extension'
    }]
