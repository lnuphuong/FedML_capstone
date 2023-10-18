import click

import fedml.api


@click.group("federate")
@click.help_option("--help", "-h")
def fedml_federate():
    """
    Manage federated resources on the MLOps platform.
    """
    pass


@fedml_federate.command("build", help="Build federate packages for the FedML® Launch platform (open.fedml.ai).")
@click.help_option("--help", "-h")
@click.option(
    "--server", "-s", default=None, is_flag=True, help="build the server package, default is building client package.",
)
@click.option(
    "--source_folder", "-sf", type=str, default="./", help="the source code folder path"
)
@click.option(
    "--entry_point",
    "-ep",
    type=str,
    default="./",
    help="the entry point of the source code",
)
@click.option(
    "--entry_args",
    "-ea",
    type=str,
    default="./",
    help="entry arguments of the entry point program",
)
@click.option(
    "--config_folder", "-cf", type=str, default="./", help="the config folder path"
)
@click.option(
    "--dest_folder",
    "-df",
    type=str,
    default="./",
    help="the destination package folder path",
)
@click.option(
    "--ignore",
    "-ig",
    type=str,
    default="",
    help="the ignore list for copying files, the format is as follows: *.model,__pycache__,*.data*, ",
)
@click.option(
    "--model_name",
    "-m",
    type=str,
    default="",
    help="model name for training.",
)
@click.option(
    "--model_cache_path",
    "-mc",
    type=str,
    default="",
    help="model cache path for training.",
)
@click.option(
    "--input_dim",
    "-mi",
    type=str,
    default="",
    help="input dimensions for training.",
)
@click.option(
    "--output_dim",
    "-mo",
    type=str,
    default="",
    help="output dimensions for training.",
)
@click.option(
    "--dataset_name",
    "-dn",
    type=str,
    default="",
    help="dataset name for training.",
)
@click.option(
    "--dataset_type",
    "-dt",
    type=str,
    default="",
    help="dataset type for training.",
)
@click.option(
    "--dataset_path",
    "-dp",
    type=str,
    default="",
    help="dataset path for training.",
)
def build(server, source_folder, entry_point, entry_args, config_folder, dest_folder, ignore,
          model_name, model_cache_path, input_dim, output_dim, dataset_name, dataset_type, dataset_path):
    is_client = True
    is_server = server
    if is_server is not None:
        is_client = False

    fedml.api.federate.build(
        is_client, source_folder, entry_point, entry_args, config_folder, dest_folder, ignore,
        model_name, model_cache_path, input_dim, output_dim, dataset_name, dataset_type, dataset_path)
