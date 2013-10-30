from setuptools import setup, find_packages
import os

import cmsplugin_dragoman

CLASSIFIERS = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
]

setup(
    name='cmsplugin_dragoman',
    version=cmsplugin_dragoman.get_version(),
    description='This is a Django CMS plugin for django-dragoman-blog',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/cmsplugin_dragoman/',
    packages=find_packages(),
    package_data={
        'cmsplugin_dragoman': [
            'static/cmsplugin_dragoman/*',
            'locale/*/LC_MESSAGES/*',
        ]
    },
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-dragoman-blog'],
)
