from setuptools import setup

setup(
    name="applepay",
    version="0.3.1",
    author="Taras Halturin",
    author_email="halturin@gmail.com",
    description=("A Python library for decrypting Apple Pay payment tokens."),
    license="BSD",
    keywords="applepay payment tokens",
    url="https://github.com/halturin/applepay",
    packages=['applepay', 'tests'],
    install_requires=['asn1crypto>=0.21.0', 'cryptography>=1.7.2'],
    setup_requires=['pytest-runner>=2.0,<3dev'],
    tests_require=['pytest>=3.0.6', 'pytz==2016.10'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
