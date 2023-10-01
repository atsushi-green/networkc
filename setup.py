from setuptools import Extension, setup

module = Extension("networkc", sources=["networkc.c"])

setup(
    name="networkc",
    version="0.0",
    description="Python package with C extension for networkx",
    ext_modules=[module],
)
