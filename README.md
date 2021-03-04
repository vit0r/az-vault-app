# Configurations

1. Official doc [MS](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=cmd)
2. Create the app register [APP](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps)

2. Create .env file on this project and reload shell after

    ```shell
    cat > .env << EOF
    KEY_VAULT_NAME=https://youvault.vault.azure.net
    tenant_id=
    client_id=
    client_secret=
    EOF
    ```

# Run with docker compose

```shell
docker-compose up --build
```

# Install

```shell
python setup.py install
```

# Run

```shell
python -m vault_app -n secretname
```
