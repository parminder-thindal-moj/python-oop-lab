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


@click.command()
@click.argument("filename")
@click.option("-t", "--times", type=int)
def multi_echo(filename, times):
    """Print value filename multiple times."""
    for x in range(times):
        click.echo(filename)


if __name__ == "__main__":
    multi_echo()
