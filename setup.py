from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="validator-luhn",
    version="0.1.0",
    author="teanus",
    author_email="teanus.ti@gmail.com",
    description="Simple credit card validator using Luna algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teanus/Validator-Luhn",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
