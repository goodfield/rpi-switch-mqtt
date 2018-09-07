# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rpi-switch-mqtt',
    version='0.0.4',
    description='Use mqtt to control relays connected to raspberry',
    long_description=readme,
    author='David Uebelacker',
    author_email='david@uebelacker.ch',
    url='https://github.com/goodfield/rpi-switch-mqtt.git',
    license=license,
    packages=['rpi_switch_mqtt'],
    install_requires=['paho-mqtt'],
    scripts=['bin/rpi-switch-mqtt']
)
