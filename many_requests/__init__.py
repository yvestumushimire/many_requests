__version__ = "0.1.0"


import requests
from concurrent.futures import ThreadPoolExecutor
import click
import time


@click.command()
@click.option("--worker", default=4, help="Maximum workers")
@click.option("--url", prompt="Enter web address 🔗", help="url path to send request to")
@click.option(
    "--q",
    prompt="number of time to send request 💣",
    help="number of time to send request 💣",
)
def app(url: str, q: int, worker: int) -> None:
    list_of_urls = [f"{url}"] * int(q)

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=worker) as pool:
        response_list = list(pool.map(lambda x: requests.get(x), list_of_urls))

    click.echo("🎉hurray I'm done")
    click.echo(f"🚀sent {len(response_list)} requests")
    click.echo(f"⌛Time used {round(time.time() - start_time, 2)} seconds")


if __name__ == "__main__":
    app()
