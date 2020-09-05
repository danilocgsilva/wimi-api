from setuptools import setup

VERSION = "1.0.0"

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
    packages=["wimiapi"],
    include_package_data=True
)

