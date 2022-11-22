import click

@click.group()
def cli():
  pass

@cli.command(name='gen')
def generic():
    click.secho('Hello there',fg="red", bold=True)

@cli.command(name='morning')
def morning():
    click.secho('Ndi na mi',fg="green", bold=True)

@cli.command(name='afternoon')
def afternoon():
    click.secho('Nd) na mi',fg="blue", bold=True)

@cli.command(name='evening')
def evening():
    click.secho('Fi3yi na mi')

if __name__ == '__main__':
    cli()