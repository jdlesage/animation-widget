"""Modified jupyter Image class.

Represents an image in the frontend using a widget.

Add: the service that modify the image content (in the goal to animate)
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import base64
import cStringIO

import ipywidgets as widgets
from traitlets import Unicode, CUnicode, Bytes

__dpi__ = 100


@widgets.register('animation.Image')
class Image(widgets.DOMWidget):
    """Displays an image as a widget.

    The `value` of this widget accepts a byte string.  The byte string is the
    raw image data that you want the browser to display.  You can explicitly
    define the format of the byte string using the `format` trait (which
    defaults to "png").
    """
    _view_name = Unicode('ImageView').tag(sync=True)
    _model_name = Unicode('ImageModel').tag(sync=True)
    _model_module = Unicode('animation-widget').tag(sync=True)
    _view_module = Unicode('animation-widget').tag(sync=True)

    # Define the custom state properties to sync with the front-end
    format = Unicode('png').tag(sync=True)
    width = CUnicode().tag(sync=True)
    height = CUnicode().tag(sync=True)
    _b64value = Unicode().tag(sync=True)

    value = Bytes()

    def _value_changed(self, name, old, new):
        """
        Service that change the base64 value of image
        """
        self._b64value = base64.b64encode(new)


def plot_into_img_widget(img_widget, figure):
    """
    Render into memory then display into an image widget
    """
    buf = cStringIO.StringIO()
    figure.savefig(buf, format='png', dpi=__dpi__)
    img_widget.value = buf.getvalue()
    buf.close()


def get_fig_size(fig):
    """
    Return matplotlib size in pixels
    """
    return fig.get_figwidth() * __dpi__, fig.get_figheight() * __dpi__
