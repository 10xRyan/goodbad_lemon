from setuptools import find_packages,setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_name = "goodbad_lemon"
Author= "10xRyan"
SRC_repo = "goodbad_lemon"

setup(
    name=SRC_repo,
    version=__version__,
    author=Author,
    packages=find_packages(),
)