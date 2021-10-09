from setuptools import setup, find_packages

with open("README.md", "r") as cd:
  long_description = cd.read()

with open('requirements.txt') as f:
  requirements = f.readlines()

setup(
      name='hugging_keras',
      version='0.0.1',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages = find_packages(),
      install_requires=[
       "pandas",
        "pydot",
        "scipy",
        "tf-nightly",
        "portpicker",
        "pyyaml",
        "Pillow",
        "numpy",
        ],
      )