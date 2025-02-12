To include all the dependencies (packages used) by the lib1 and lib2 libraries in your package, you can list these dependencies in the setup.py file. When your package is installed, pip will automatically install all the listed dependencies. I'll show you how to do this step by step:

Identify the Dependencies: First, identify all the external libraries that your lib1 and lib2 libraries use. Let's assume that lib1 uses requests and lib2 uses numpy.

Project Structure:

meu_projeto/
├── lib1/
│   ├── lib1.py
│   └── __init__.py
├── lib2/
│   ├── lib2.py
│   └── __init__.py
├── __pycache__/ (generated automatically after compilation)
├── setup.py
└── MANIFEST.in
Create the Libraries (lib1/lib1.py and lib2/lib2.py):

python
# lib1/lib1.py

import requests

def funcao_lib1(nome):
    resposta = requests.get(f'https://api.agify.io?name={nome}')
    idade = resposta.json().get('age')
    return f'Hello from lib1, {nome}! Your estimated age is {idade}.'

python

# lib2/lib2.py
import numpy as np

def funcao_lib2(numeros):
    media = np.mean(numeros)
    return f'Hello from lib2! The average of the provided numbers is {media}.'
Compile the Python Files to Bytecode:

´´´ sh
python -m py_compile lib1/lib1.py lib2/lib2.py

´´´

Copy pyc files to pack folder

Write the setup.py File: In the setup.py, include the dependencies in the install_requires list:


''' python 
from setuptools import setup, find_packages
import os

# Function to include just .pyc files
def find_pyc_files(package_dir):
    pyc_files = []
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if file.endswith('.pyc'):
                pyc_files.append(os.path.relpath(os.path.join(root, file), package_dir))
    return pyc_files

setup(
    name='meu_projeto',
    version='0.1',
    packages=find_packages(include=['pack', 'pack.*']),
    package_data={
        'pack': find_pyc_files('pack'),
    },
    install_requires=[
        'requests',
        'numpy',
    ],
    zip_safe=False,
)

python setup.py bdist_wheel

The Wheel package will be generated in the dist/ folder, containing the compiled bytecodes and the listed dependencies.

Install and Use the Package: In your other project, install the Wheel package:

sh

pip install /path/to/meu_projeto/dist/meu_projeto-0.1-py3-none-any.whl

Use the library functions:

python

# main.py
from pack.lib1 import funcao_lib1
from pack.lib2 import funcao_lib2

print(funcao_lib1('World'))
print(funcao_lib2([1, 2, 3, 4, 5]))

By following these steps, you'll have a Wheel package that includes all the necessary dependencies for the lib1 and lib2 libraries, making it easier to install and use in other projects.