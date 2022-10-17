from setuptools import find_packages, setup


setup(
    name='Husk',
    version = '0.0.2',
    description= ' A simple shell written in Python',
    entry_points={
        'console_scripts':[
            'husk=Husk.husk:main'
        ]
    },
    packages=find_packages()
)

