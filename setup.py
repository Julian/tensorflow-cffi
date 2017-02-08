import os

from setuptools import find_packages, setup


try:
    import __pypy__
except ImportError:
    cffi_requirement = ["cffi>=1.0.0"]
else:
    cffi_requirement = []


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name="tensorflow_cffi",
    url="https://github.com/Julian/tensorflow-cffi",

    description="CFFI bindings to the Tensorflow C API",
    long_description=long_description,

    author="Julian Berman",
    author_email="Julian@GrayVines.com",

    packages=find_packages(),

    cffi_modules=["tensorflow_cffi/build.py:ffi"],

    setup_requires=["vcversioner>=2.16.0.0"] + cffi_requirement,
    vcversioner={"version_module_paths": ["tensorflow_cffi/_version.py"]},

    install_requires=cffi_requirement,

    classifiers=classifiers,
)
