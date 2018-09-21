from setuptools import setup, find_packages

setup(
    name='ocdskit',
    version='0.0.0',
    author='Open Contracting Partnership & Open Ownership',
    author_email='data@opendataservices.coop',
    url='https://github.com/openownership/bodskit',
    description='A suite of command-line tools for working with BODS data',
    license='BSD',
    packages=find_packages(),
    long_description='A suite of command-line tools for working with BODS data',
    install_requires=[
        'jsonref',
        'jsonschema',
    ],
    extras_require={
        'test': [
            'pytest',
            'flake8',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points='''[console_scripts]
bodskit = bodskit.cli.__main__:main''',
)
