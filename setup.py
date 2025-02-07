from setuptools import setup, find_packages

setup(
    name="procli",
    version="0.0.1",
    author="skrept",
    author_email="en.jargal.dev@gmail.com",
    description="A CLI for creating Python projects using Pipenv",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/skrept338/procli",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "procli=procli.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
