from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ckm_image_processing",
    version="0.0.8",
    author="Celso",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckmihara/bootcamp_image_processing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.11",

)
