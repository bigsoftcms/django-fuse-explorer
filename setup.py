from setuptools import setup, find_packages

setup(
    name='django-fuse-explorer',
    version='0.1.0',
    description="A FUSE (Filesystem in Userspace) module for exposing a Django project's data and metadata in a directory structure.",
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Roger Barnes',
    author_email='roger@mindsocket.com.au',
    url='https://github.com/mindsocket/django-fuse-explorer',
    download_url='https://github.com/mindsocket/django-fuse-explorer/downloads',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
    tests_require=[
        'django>=1.3',
        'fuse-python',
    ],
#    test_suite='runtests.runtests',
#    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
