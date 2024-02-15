from setuptools import setup

setup(
    name='Terminal_bot',
    version='0.0.0',
    url='https://github.com/Krom4rd/Terminal_bot',
    author='Team name',
    author_email='Krom4rd@gmail.com, ...',
    packages=['Terminal_bot'],    
    entry_points={'console_scripts': ['Terminal_bot = Terminal_bot.main:main']
                  })

