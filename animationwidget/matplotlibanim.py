from __future__ import absolute_import

from IPython.display import display, clear_output
from ipywidgets import ToggleButton
from traitlets import link

from . import widget_image
from .example import AnimationWidget


class AnimationViewer(object):
    """
    Animation widget
    """
    def __init__(self, anim):
        self._anim = anim
        self._fig = anim._fig
        self._iter = anim.new_frame_seq()
        self._image = widget_image.Image()
        figsize = widget_image.get_fig_size(self._fig)
        self._image.width = "{0}px".format(figsize[0])
        self._image.height = "{0}px".format(figsize[1])
        widget_image.plot_into_img_widget(self._image, self._fig)

    @property
    def image(self):
        return self._image

    def update(self, new_value):
        args = self._iter.next()
        self._anim._draw_frame(args)
        widget_image.plot_into_img_widget(self._image, self._fig)


def gen_widget(anim):
    viewer = AnimationViewer(anim)
    clear_output(True)
    anim_widget = AnimationWidget()
    anim_widget.loop = True
    button = ToggleButton(description="run", default=False)
    link((button, 'value'), (anim_widget, 'run'))
    display(anim_widget)
    display(viewer.image)
    display(button)
    anim_widget.observe(lambda value: viewer.update(value["new"]), names="value")
