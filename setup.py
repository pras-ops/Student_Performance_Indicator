from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    def: It is a keyword in Python used to define a function.
    get_requirements: This is the name of the function. You can choose any valid name for your function that describes its purpose.
    (file_path: str): This part is called the function parameter or input parameter. It specifies that the function expects one parameter named file_path, and its type is str, which stands for string. The file_path parameter allows you to pass a file path as an argument when calling the function.
    -> List[str]: This part indicates the return type of the function. It specifies that the function will return a list of strings (List[str]). The arrow (->) is used to indicate the return type annotation.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    
'''
requirements=[]: Initializes an empty list called requirements to store the extracted requirements.

with open(file_path) as file_obj:: Opens the file specified by the file_path parameter in a context manager. This ensures that the file is properly closed after reading its contents.

requirements=file_obj.readlines(): Reads all lines of the file and assigns them to the requirements variable as a list of strings. Each line of the file becomes an element in the list.

requirements=[req.replace("\n","") for req in requirements]: Iterates over each requirement in the requirements list and removes the newline character ("\n") at the end of each requirement. This is done using a list comprehension to create a new list with modified requirements.

if HYPEN_E_DOT in requirements: requirements.remove(HYPEN_E_DOT): Checks if a specific requirement, represented by the variable HYPEN_E_DOT, is present in the requirements list. If it is found, it is removed from the list using the remove() method.

return requirements: Returns the modified list of requirements.
'''



setup(
name="SPI",
version='0.0.1',
author='Prashant',
author_email='prashantjacob.bilaspur@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


'''
Metadata: The file typically includes metadata about the project, such as the project name, version, author, description, license, and dependencies. This information helps users understand the purpose and requirements of the project.

Dependencies: setup.py specifies the dependencies required for the project to run correctly. These dependencies can be other Python packages that need to be installed for the project to work as intended.

Distribution: The file also defines the packaging and distribution options for the project. It specifies which files should be included in the package, such as source code, data files, and documentation. It also defines how the package should be built and distributed, such as creating a source distribution or a built distribution in the form of a wheel or an executable installer.

Installation: setup.py allows users to install the project using tools like pip. It provides instructions for installing the package and its dependencies, making it easier for users to set up and use the project on their own systems.

By running setup.py using appropriate commands, such as python setup.py install or pip install ., the necessary steps defined in the file are executed, including installing dependencies, building the package, and making it available for use.

Overall, setup.py serves as a central configuration file that provides the necessary information and instructions for packaging, distributing, and installing a Python project.
'''