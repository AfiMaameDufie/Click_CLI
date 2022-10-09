import click
import os

@click.argument('mydir', envvar='MYDIR', type=click.Path(exists=True))

@click.command()
def list_contents(mydir):

    click.echo(os.listdir(mydir))


if __name__ == '__main__':
    list_contents()