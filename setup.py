from setuptools import setup, find_packages
setup(
    name="eas",
    version="0.1",
    packages=find_packages(),

    install_requires=['pyxray>=1.3','numpy>=1.14.1'],

    author="Thiago Gomes Veríssimo",
    author_email="verissimotgv@gmail.com",
    description="EAS",
    license="PSF",
    keywords="x-rays"
)
