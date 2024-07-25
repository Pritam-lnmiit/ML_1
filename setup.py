from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list:
    with open(file_path, 'r') as file_obj:
        requirements = [line.strip() for line in file_obj.readlines() if line.strip()]
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Pritam',
    author_email='22ume028@lnmiit.ac.in',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)

