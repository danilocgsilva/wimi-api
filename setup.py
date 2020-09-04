from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="wimi-api",
    version=VERSION,
    description="Package to fetch the current external ip",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="ip what-is-my-ip",
    url="https://github.com/danilocgsilva/wimi-api",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["wimi-api"],
    include_package_data=True
)

