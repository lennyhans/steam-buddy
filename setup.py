"Setup chimera app"
from glob import glob
from setuptools import setup, find_packages

setup(
    name="Chimera",
    version="0.12.2",
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['chimera = chimera_app.__main__:main']
                  },
    scripts=['migrate-to-chimera',
             'steam-tweaks',
             'steam-patch',
             ],

    data_files=[
        ('share/chimera/images', glob('images/*.png')),
        ('share/chimera/images/flathub', glob('images/flathub/*.png')),
        ('share/chimera/views', glob('views/*.tpl')),
        ('share/chimera/public', glob('public/*.js')),
        ('share/chimera/public', glob('public/*.css')),
        ('share/chimera/config', glob('config/*.cfg')),
        ('share/chimera/config', glob('config/*.conf')),
        ('share/chimera/bin',    glob('bin/*')),
        ('bin', glob('launchers/*')),
        ('share/doc/chimera', ['README.md']),
        ('share/doc/chimera', ['LICENSE']),
    ],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'bottle',
        'pyyaml',
        'requests',
        'beaker',
        'pygame',
        'psutil',
        'bcrypt',
        'vdf',
        'inotify_simple',
    ],

    # metadata to display on PyPI
    author="Alesh Slovak",
    author_email="aleshslovak@gmail.com",
    description=("Chimera is a web based tool for installing non-Steam "
                 "software to your Linux based couch gaming system. It "
                 "was primarily developed for ChimeraOS."),
    keywords=("steam steamos couch emulation flatpak flathub chimera app "
              "chimeraos gamer gaming"),
    url="https://github.com/chimeraos/chimera",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/chimeraos/chimera/issues",
        "Documentation": ("https://github.com/chimeraos/chimera/"
                          "blob/master/README.md"),
        "Source Code": "https://github.com/chimeraos/chimera",
    },
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)
