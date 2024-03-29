from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='guess_logo',
      version='0.0.9',
      description="Detect logo url for any website.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: Apache Software License",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: SQL",
                   "Topic :: Database"],
      keywords='guess logo website selenium',
      author='Kehao Wu',
      author_email='kehao.wu@gmail.com',
      license='MIT',
      url='https://github.com/KehaoWu/guess_logo',
      packages=['guess_logo'],
      include_package_data=True,
      zip_safe=True,
      install_requires=["selenium>=3.0.0", "opencv-python>=4.0.0", "numpy>=1.0.0"],
      entry_points="")
