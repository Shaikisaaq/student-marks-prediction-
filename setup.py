from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(filepath:str) -> List[str]:
    """Reads the requirements.txt file and returns a list of requirements."""
    requirements=[]
    with open(filepath) as f:
        requirements = f.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup( name='ml-package',
        author='Isaaq',
        version='0.1',
        packages=find_packages(),
        author_email="isaaq.2889@gmail.com",
        requires=get_requirements("requirements.txt")
    )