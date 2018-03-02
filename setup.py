from setuptools import setup, find_packages

setup(
    name="eas",
    version="0.1",
    url = 'git@github.com:thiagogomesverissimo/eas.git',
    author="Thiago Gomes Veríssimo",
    author_email="verissimotgv@gmail.com",
    description="EAS - elemental-analysis-scripts",
    packages = find_packages(),    
    install_requires=['pyxray>=1.3','numpy>=1.14.1'],
)
