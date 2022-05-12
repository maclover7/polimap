import click
import json

from .results_downloader import ResultsDownloader


def set_config(ctx, param, filename):
    with open(filename) as f:
        config = json.loads(f.read())
        ctx.default_map = config
        return config


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command()
@click.option("--config", callback=set_config, type=click.Path())
def download_results(config):
    click.echo(config)
    downloader = ResultsDownloader(
        config['election_owner'],
        config['election_id'],
        config['contest_name'],
        config['contest_shortname'],
        config['formatted_candidate_names'],
        config['downloaded'])
    downloader.run()
