from setuptools import setup, find_packages
import os

# Read requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Find all packages, including submodules
packages = ['src']
for package in find_packages(where="src"):
    packages.append(f"src.{package}")

# Include configuration files that come with the package
package_data = {
    'src': ['contexts/*.yml', 'contexts/*.yaml', 'contexts/*.json']
}

setup(
    name="e2e-agent",
    version="0.1.0",
    description="E2E test failure analysis agent using LLM",
    author="Agent Team",
    packages=packages,
    include_package_data=True,
    package_data=package_data,
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "e2e-agent=src.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 
