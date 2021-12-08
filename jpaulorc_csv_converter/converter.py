import logging
import threading
import typing
from os import path
from pathlib import Path

import click
from click.termui import prompt

thread_local = threading.local()

logging.basicConfig(level="DEBUG", format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'")
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--input", "-i", default="./", help="Path where to read the files for convertion.", type=str
)
@click.option(
    "--output", "-o", default="./", help="Path where the converted files will be saved.", type=str
)
@click.option(
    "--delimiter",
    "-d",
    default=",",
    help="Separator used to split the files. You can only use these symbols: comma and colon",
    type=str,
)
@click.option(
    "--prefix",
    "-prefix",
    prompt=True,
    prompt_required=False,
    default="file",
    help=(
        "Prefix used to prepend to the name of the converted file saved on disk."
        " The suffix will have a number starting from 0. eg: file_0.json."
    ),
)
def converter(input: str = "./", output: str = "./", delimiter: str = ",", prefix: str = None):
    pass
