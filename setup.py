from setuptools import setup, find_packages
setup(
    name='Hello_World',
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'exp10it'==2.6.70,
        'gradio'==4.16.0,
    ],
)
