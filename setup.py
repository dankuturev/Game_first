try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'the_first_game',
    'author': 'dankut',
    'url': 'Ссылка на проект',
    'download_url': 'Ссылка на скачивание',
    'author_email': 'dan.kutyrev@yandex.ru',
    'version': '0.1',
    'install_requires': ['none'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)