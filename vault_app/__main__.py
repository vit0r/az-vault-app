"""
Main program
"""

from vault_app import (
    ClientSecretCredential,
    DefaultAzureCredential,
    SecretClient,
    click,
    environ,
    logging,
    sys,
)


@click.command(name=__name__)
@click.help_option("--help", "-h", "?")
@click.option(
    "--secret-name", "-n", type=click.STRING, required=True, help="secret name"
)
def retrieved_secret(secret_name):
    """retrieved_secret"""
    log_level = environ.get("APP_LOG_LEVEL", logging.INFO)
    logging.basicConfig(format="%(levelname)s:%(message)s", level=log_level)
    if (
        "tenant_id" in environ.keys()
        and "client_id" in environ.keys()
        and "client_secret" in environ.keys()
    ):
        tenant_id = environ["tenant_id"]
        client_id = environ["client_id"]
        client_secret = environ["client_secret"]
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    else:
        credential = DefaultAzureCredential()
    kv_uri = environ["KEY_VAULT_NAME"]
    client = SecretClient(vault_url=kv_uri, credential=credential)
    secret = client.get_secret(secret_name)
    if hasattr(secret, "name") and hasattr(secret, "value"):
        logging.info("\t'SecretName:'\t'%s'", secret.name)
        logging.info("\t'SecretValue:'\t'%s'", secret.value)


def sys_errh(type_err, exception, traceback_err):
    """Loggin unHandler exceptions"""
    logging.exception("unhandler exception %s", exception)


sys.excepthook = sys_errh

if __name__ == "__main__":
    retrieved_secret()
