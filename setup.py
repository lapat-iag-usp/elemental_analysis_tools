import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elemental-analysis-scripts",
    version="1.0.0",
    url = 'https://github.com/elemental-analysis-group/elemental-analysis-scripts.git',
    author="Thiago Gomes Veríssimo",
    author_email="verissimotgv@gmail.com",
    description="elemental-analysis-scripts",
    packages=setuptools.find_packages(),
    install_requires=['pyxray>=1.3','numpy>=1.14.1'],
)
