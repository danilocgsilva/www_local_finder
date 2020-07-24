from setuptools import setup

VERSION = '0.0.1'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="www-local-finder",
    version=VERSION,
    description="Searchs for local www root in current environment",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="dev www environment",
    url="https://github.com/danilocgsilva/www_local_finder",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["wwwlocalfinder"],
    include_packages_data=True
)