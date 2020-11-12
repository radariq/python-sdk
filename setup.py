import setuptools
with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='radariq',
    version='1.0.0',
    author='RadarIQ Ltd',
    author_email='support@radariq.io',
    description='Python SDK for the RadarIQ sensor',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['radariq'],
    url='http://github.com/radariq/python-sdk',
    license='MIT',
    python_requires='>=2.7',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
)
