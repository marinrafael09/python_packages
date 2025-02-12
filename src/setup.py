from setuptools import setup, find_packages
import os

# Função para incluir apenas arquivos .pyc
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
