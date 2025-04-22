from setuptools import setup, find_packages

setup(
    name="reconapp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0", "tabulate>=0.8", "python-whois>=0.7"
    ],
    entry_points={
        "console_scripts": [
            "reconapp = reconapp.cli:cli",
        ],
    },
)
