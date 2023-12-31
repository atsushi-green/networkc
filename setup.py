from setuptools import Extension, find_packages, setup

module = Extension(
    "networkc_core",
    sources=[
        "src/c_module/networkc.c",
        "src/c_module/util.c",
        "src/c_module/heapq.c",
    ],
)

setup(
    name="networkc",
    version="0.0.0",
    description="Python package with C extension for networkx",
    ext_modules=[module],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
