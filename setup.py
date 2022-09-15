from setuptools import setup
import versioneer

setup(name='scusage',
    license='MIT',
    packages=['scusage'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False
)
