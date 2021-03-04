"""
vault_app module
"""

import logging
import sys
import traceback
from os import environ

try:
    import click
except ModuleNotFoundError:
    print("###  pip install click  ###")
    raise
try:
    from azure.identity import ClientSecretCredential, DefaultAzureCredential
except ModuleNotFoundError:
    print("###  pip install azure-identity  ###")
    raise

try:
    from azure.keyvault.secrets import SecretClient
except ModuleNotFoundError:
    print("###  pip install azure-keyvault-secrets  ###")
    raise
