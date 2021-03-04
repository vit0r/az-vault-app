"""Setup app from setup.cfg
"""

from setuptools import find_packages, setup

setup(
    packages=find_packages(exclude="tests"),
    version="1.0.0",
    py_modules="vault_app",
    zip_safe=True,
    name="vaultapp",
    description="how to get secret from azure keyvault",
    long_description="DEMOonly",
    url="https://github.com/vit0r/az-vault-app",
    author="vit0r",
    author_email="vitornascimentoaraujo@gmail.com",
    license="MIT",
    include_package_data=True,
    install_requires=["click", "azure-identity", "azure-keyvault-secrets"],
    entry_points={"console_scripts": [
        "vaultapp=vault_app.__main__:retrieved_secret"]},
)
