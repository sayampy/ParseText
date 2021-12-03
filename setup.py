from setuptools import setup
setup(
    name="ParseAnyText",
    version="0.1",
    author="Sayam Goswami",
    description="A small textparsing package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sayampy/ParseAnyText",
    project_urls={
        "Bug Tracker": "https://github.com/sayampy/ParseAnyText/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=['textparser'],
    python_requires=">=3.6",
)
