from setuptools import setup

setup(
    name="BruteNinja",
    version="0.1.0",
    description="A simple brute-force login cracker",
    author="Vishnu Thandel",
    author_email="branihat@gmail.com",
    url="BruteNinja.py",
    packages=["BruteNinja"],
    python_requires=">=3.6",
    install_requires=["requests", "colorama"],
)
