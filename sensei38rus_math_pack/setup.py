from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sensei38rus_math_pack",
    version="0.1.3",
    author="sensei38rus",
    author_email="shihowdima1337@gmail.com",
    description="Полезные математические утилиты для базовых вычислений",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sensei38rus/fossdev/tree/pypi-task",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords="math, utilities, calculator, geometry",
    project_urls={
        "Bug Reports": "https://github.com/sensei38rus/fossdev/tree/pypi-task/issues",
        "Source": "https://github.com/sensei38rus/fossdev/tree/pypi-task",
    },
)