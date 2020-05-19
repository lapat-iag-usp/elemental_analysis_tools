import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elemental_analysis_tools",
    version="0.0.3",
    url = 'https://github.com/elemental-analysis-group/elemental_analysis_tools.git',
    description="elemental_analysis_tools package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Thiago Gomes Veríssimo",
    author_email="verissimotgv@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=['pyxray>=1.3','numpy>=1.14.1'],
)
