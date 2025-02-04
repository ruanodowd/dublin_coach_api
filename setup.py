from setuptools import setup, find_packages

setup(
    name="dublin_coach_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    author="Ruan O'Dowd",
    author_email="ruanodowd@gmail.com",
    description="A Python package for interacting with the Dublin Coach API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruanodowd/310_bus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
