import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="kungufai-env",
    version="0.1.0",
    description="Environment handling to simplify development environments",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kungfuai/env",
    author="Endurance Idehen",
    author_email="endurance.idehen@kungfu.ai",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=(
        "examples",
        "kfai_env/tests",
    )),
    install_requires=["python-dotenv"],
    include_package_data=True,
)