from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of requirement
    """
    path = r"requirements.txt"
    requirement_list: List[str] = []
    with open(path, "r") as f:
        requirement_list = [lib.strip() for lib in f if lib != "-e ."]

    return requirement_list


# print(get_requirements())

setup(
    name="sensor",
    version="0.0.1",
    author="Avinash",
    author_email="avinashsingh539@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
