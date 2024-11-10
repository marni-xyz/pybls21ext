import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybls21ext",
    version="4.0.3",
    author="Julius Vitkauskas (initial) and Martin Niese (additions)",
    author_email="zadintuvas@gmail.com",
    description="An api allowing control of AC state (temperature, on/off, speed) of an Blauberg S21 device locally over TCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marni-xyz/pybls21ext",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=["pymodbus>=3.6.3,<4.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
