from setuptools import setup

setup(name='guess_logo',
      version='0.0.2',
      description="Detect logo url for any website.",
      long_description="",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: Apache Software License",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: SQL",
                   "Topic :: Database"],
      keywords='guess logo website selenium',
      author='Kehao Wu',
      author_email='kehao.wu@gmail.com',
      license='MIT',
      packages=['guess_logo'],
      include_package_data=True,
      zip_safe=True,
      install_requires=["selenium>=3.0.0"],
      entry_points="")
