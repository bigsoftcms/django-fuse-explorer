django-fuse-explorer
====================

django-fuse-explorer is an extension command that provides a filesystem view of a Django project's data and metadata.

Installation
------------
For now: pip install git+https://github.com/mindsocket/django-fuse-explorer.git#egg=django-fuse-explorer
TODO pip install django-fuse-explorer

Usage
-----

python manage.py fuse_explorer [TODO alternative mount point]

This command will start a FUSE session and create a root mount point, by default ... TODO called fuse

Filesystem contents
-------------------
TODO * 1,000,000
navigate models - meta and actual data
- manipulate data (json/csv/yaml/xml?)
management commands?
navigate tests?
reverse urls?
"execute" template tags?
browse media, templates and static files
symlinks to other libraries etc?
... others - see what management commands can be mapped to fs
