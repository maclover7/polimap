from setuptools import setup

setup(
    name="polimap",
    version="0.0.1",
    author="Jon Moss",
    author_email="me@jonathanmoss.me",
    url="https://github.com/maclover7/polimap",
    description="Political mapping, made easy.",
    packages=("polimap"),
    entry_points={"console_scripts": ("polimap",)},
    install_requires=[],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="election"
)
