from setuptools import setup, find_packages

PROJECT = 'cool python'


DESCRIPTION = 'how to user python cool'


setup(
    name=PROJECT,
    version="0.0.1",
    description=DESCRIPTION,

    author='cool8sniper',
    author_email='cool8sniper@gmail.cn',

    platforms=['Any'],
    namespace_packages=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)
