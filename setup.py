from distutils.core import setup
setup(
  name = 'kartverket_tide_api',
  packages = ['kartverket_tide_api'],
  version = '0.1',
  license='MIT',
  description = 'This is a unofficial library for the kartverket tide api',
  author = 'Mats Johan Pedersen',
  author_email = 'matspedersen@protonmail.com',
  url = 'https://github.com/matsjp/kartverket_tide_api',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['kartverket'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'vcrpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)