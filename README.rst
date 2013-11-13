==================
cmsplugin-dragoman
==================

A cmsplugin for django-dragoman-blog

Installation
------------

For the current stable version:

::

    pip install cmsplugin-dragoman # no pypi yet

For the development version:

::

    pip install https://github.com/divio/django-cms/archive/develop.zip

    pip install https://github.com/fivethreeo/django-dragoman-blog/archive/develop.zip

    pip install https://github.com/fivethreeo/cmsplugin-dragoman/archive/develop.zip


Configuration
-------------

Settings
========

Add ::

    'cmsplugin_dragoman',
    'dragoman_blog',
    'taggit',


Set ``settings.DRAGOMAN_BLOG_ENTRY_MODEL`` to ``('cmsplugin_dragoman.dragoman_models.Entry', 'cmsplugin_dragoman')``.

Add the apphook for each language to a page in the cms and make sure you publish it, restart the devserver.

To join in development
----------------------

::

    git clone https://github.com/fivethreeo/cmsplugin-dragoman.git
    cd cmsplugin-dragoman
    
    virtualenv --system-site-packages env
    env/bin/activate
    pip install -r testing/requirements/django-1.5.txt
    
    python develop.py test
    
    python develop.py manage syncdb --all --noinput
    python develop.py manage migrate --fake
    python develop.py server
    
    http://127.0.0.1:8000/admin/
