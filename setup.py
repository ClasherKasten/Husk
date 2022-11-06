from setuptools import find_packages, setup


setup(
    name='Husk',
    version = '1.0.0',
    description= 'A simple shell written in Python',
    entry_points={
        'console_scripts':[
            'husk=Husk.husk:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'readchar'
    ],
    python_requires='>=3.8'
)

