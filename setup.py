from distutils.core import setup
setup(
  name = 'pycubescrambler',         # How you named your package folder (MyLib)
  packages = ['pycubescrambler'],   # Chose the same as "name"
  version = '0.2.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'a python module to generate scrambles for most wca puzzles',   # Give a short description about your library
  author = 'midnightcuberx',                   # Type in your name
  author_email = 'midnightcuberx@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/midnightcuberx/pycubescrambler',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/midnightcuberx/pycubescrambler/archive/v_0.2.4.tar.gz',    # I explain this later on
  keywords = ['CUBING', 'SCRAMBLES', 'RUBIKS'],   # Keywords that define your package best
  install_requires=[
        'appdirs',
        'packaging',
        'PyExecJS',
        'pyparsing',
        'six',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
