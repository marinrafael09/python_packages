python -m py_compile lib1/lib1.py lib2/lib2.py

mv ./lib1/__pycache__/lib1.cpython-312.pyc ./pack/lib1.pyc
mv ./lib2/__pycache__/lib2.cpython-312.pyc ./pack/lib2.pyc

python setup.py bdist_wheel