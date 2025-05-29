import click


@click.command()
@click.option(
    "--service",
    envvar="SERVICE",
    required=True,
    help="Pokemon service to run (can also be set via SERVICE env var)",
)
def run_service(service):
    click.echo(f"Running Pokemon service: {service}!")


if __name__ == "__main__":
    run_service()
