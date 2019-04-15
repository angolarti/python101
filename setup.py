from setuptools import setup, find_packages


from os import path

PATH = path.abspath(path.dirname(__file__))

# Get the long description form the relevant file
try:
    with open(path.join(PATH, 'DESCRIPTION.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    log_description = ''

setup(
    # Ver PEP 426 (names)
    name='python101',

    # Ver PEP 440
    # O formato pode ser assim:

    # 1.2.0.devel1  # Development release
    # 1.2.0a1       Alpha Release
    # 1.2.0b1       Beta Release
    # 1.2.0rc1      Release Candidate
    # 1.2.0         Release Final
    # 1.2.0.post1   Post Release
    # 21.04         date based release
    # 23            Serial release

    version='1.0.2',

    description='Exemplo para o Python 101',
    long_description=long_description,

    # Detalhes do Autor
    url='https://angolarti.github.io',
    author_email='angolarti@gmail.com',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Prodution/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Education :: Testing',

        # pPick your license as you wish (should match "License" above)
        'License :: OSI Approved :: GPLv3',

        # Specify the Python version you support here. in paeticular, ensure
        # that you indicate whether you support Python 2, Python 3 or both
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='exemplo tutorial desenvolvimento',

    # You cam just specify the packages manually here if your project is
    # simple. Or you can use find_packages()
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependecies here. these will be installed by pip when
    # your project is installed. for an analysis of "install_requires" us pip`s
    # requirements files see:
    # https://packaging.python.org/en/requirements.html
    install_requires=['sh>=1.12.14'],

    # List additional groups of dependencies here (e.g. development
    # dependecies). You can install these using the following syntax,
    #  for exemple:
    #  $ pip install -e .[dev.test]
    #  extras_require=[
    #       'dev': ['check-manifest'],
    #       'test': ['coverage'],
    #  ],

    # if there are data files included in your packages that need to be
    # installed, specify them here. If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data=(
    #      'data': ['data.json'],
    # ),

    # Although 'package_data' is the preferred appoach, in some case you may
    # need to place data files outside of your packages. See:
    # https://docs.python.org/3.7/disutils/setupscript.html#installing-additional-file
    # In this case,  'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('python101', ['data/dados.json'])],

    # To provide executable scruipts, use entry poinys in preferences to the
    # "scripts" keyword. Entry points provide cross-plataform support and allow
    # pip to create the appropriate form of executable for the tarfet plataform
    # entry_points={
    #   'console_scripts': [
    #       'sample=sample:main'
    #   ],
    # }
)
