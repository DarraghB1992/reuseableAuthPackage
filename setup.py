import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='reusable-auth-app',
    version='1.0.0',
    packages=['reusable_auth'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to add email authorization',
    long_description=README,
    url='http://example.com',
    author='Darragh Browne',
    author_email='darragh1992@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved : BSD License',
        'Operating System :: OS Independent',
        'Programming License :: Python :: 2.6',
        'Programming License :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django_forms_bootstrap',
    ],

)
