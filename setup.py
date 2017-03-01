from setuptools import setup

setup(
    name='lektor-cp',
    description='Lektor plugin to support publishing simply by copying the files',
    version='0.1',
    author='Laurent Peuch',
    author_email='cortex@worlddomination.be',
    url='https://github.com/psycojoker/lektor-cp',
    license='MIT',
    platforms='any',
    py_modules=['lektor_cp'],
    entry_points={
        'lektor.plugins': [
            'cp = lektor_cp:CpPlugin',
        ]
    },
    install_requires=[
        'Lektor',
    ],
)
