from setuptools import setup, find_packages
import versioneer

setup(name="scusage",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=[
        "tabulate", "i3ipc"
    ],
    zip_safe=False
)
