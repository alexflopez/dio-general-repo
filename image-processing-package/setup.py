from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="package_name",
    version="0.0.1",
    author="Alex Lopez",
    author_email="alexflopez@...",
    description="My short description",
    long_description=page_description,
    url="",
    packages=find_packages(),
    install_requirements="requirements.txt",
    python_requires='>=3.8',
)
