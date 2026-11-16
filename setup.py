import os
from typing import List
from setuptools import find_packages, setup  # type: ignore

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines, comments, and editable install flag
                if requirement and not requirement.startswith('#') and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt not found')

    return requirement_list


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Anshu Pramanik",
    author_email="pramanikanshu456@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.13"
)
