from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str) -> List[str]:
    """Function to return the list of requirements

    Args:
        file_path (str): path of requirements.txt

    Returns:
        List[str]: list of requirement packages
    """
    requirements = list()
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='end2end_mlproj',
    version='0.0.1',
    author='PhuTD',
    author_email='phutx2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)