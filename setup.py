# setup.py

from setuptools import setup, find_packages

setup(
    name="classifier_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "langchain-core",
        "langchain-together",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "classifier = main:main",
        ],
    },
    author="imuki2004",
    author_email="imukhambe2-c@my.cityu.edu.hk",
    description="A topic classification tool using an LLM.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/imuki2004/DocPro-Demo.git", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
