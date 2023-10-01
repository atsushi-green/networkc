from distutils.core import Extension, setup

module = Extension("floyd_warshall_module", sources=["floyd_warshall.c"])

setup(
    name="FloydWarshallPackage",
    version="0.0",
    description="Python interface for the Floyd-Warshall algorithm",
    ext_modules=[module],
)
