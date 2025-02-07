from setuptools import find_packages,setup
from typing import List

HYPEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    
    reqired_lib=[]
    with open(file_path) as file_obj:
        reqired_lib=file_obj.readlines()
        reqired_lib=[req.replace("\n","") for req in reqired_lib]

        if HYPEN_DOT in reqired_lib:
            reqired_lib.remove(HYPEN_DOT)
    
    return reqired_lib

setup(
name='FASTAPI PRACTICE',
version='0.0.1',
author='Muhammad Ali',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)