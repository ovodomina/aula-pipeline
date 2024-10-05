from setuptools import setup, find_packages

setup(
    name='flask-web-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.3',
    ],
    tests_require=[
        'pytest==8.3.3',
    ],
)
