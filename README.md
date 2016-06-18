animation-widget
===============================

Jupyter Animation Widget

Installation
------------

To install use pip:

    $ pip install animationwidget
    $ jupyter nbextension enable --py --sys-prefix animationwidget


For a development installation (requires npm),

    $ git clone https://github.com/jdlesage/animation-widget.git
    $ cd animationwidget
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --user animationwidget
    $ jupyter nbextension enable --py --user animationwidget
