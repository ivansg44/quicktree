import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quicktree",
    # TODO: Uncomment when ready for first release
    # version="0.1.0",
    author="Ivan Sohrab Gill",
    author_email="ivansg44@gmail.com",
    # TODO: Uncomment and fill
    # description="...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivansg44/quicktree",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="~=3.5",
    entry_points={
        "console_scripts": [
            "quicktree=quicktree.core:main"
        ]
    }
)