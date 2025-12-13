from setuptools import find_packages, setup
from typing import List

Connector ='-e .'
def get_requirements(file_path:str)->List[str]:
    "This funtion returns list of get_requirements"
    requirements = []
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        
        if Connector in requirements:
            requirements.remove(Connector)
            
    return requirements
    


setup (
    name = 'MLP',
    version = '0.0.1',
    author = 'Akshat',
    author_email= 'akshatchaurasia212005@gmail.com',
    packages = find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')
)