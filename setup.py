from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author_email='limpid86@icloud.com',
    description='A utility for backing up PostgreSQL database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/m-lisitski/pgbackup',
    packages=find_packages('src')
)
