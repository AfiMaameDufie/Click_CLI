import click

@click.group()
def cli():
  pass

@cli.command(name='gen')
def generic():
    click.echo('Hello there')

@cli.command(name='morning')
def morning():
    click.echo('Ndi na mi')

@cli.command(name='afternoon')
def afternoon():
    click.echo('Nd) na mi')

@cli.command(name='evening')
def evening():
    click.echo('Fi3yi na mi')

if __name__ == '__main__':
    cli()