"""
Setup script for chaotic-exceptions package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chaotic-exceptions",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A library for generating random exceptions to test system resilience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chaotic-exceptions",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    keywords="testing chaos exception resilience fault-injection",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/chaotic-exceptions/issues",
        "Source": "https://github.com/yourusername/chaotic-exceptions",
    },
)