from setuptools import setup, find_packages

with open('requirements.txt') as file:
    requirements = file.read().splitlines()

setup(
    name="AI-Travel LLMOPS",
    version='0.0.1',
    author='Bayuzen Ahmad',
    packages=find_packages(),
    install_requires=requirements
)