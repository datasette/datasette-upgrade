from datasette import hookimpl
from datasette.utils import parse_metadata
import click
import pathlib
import yaml


@hookimpl
def register_commands(cli):
    @cli.group()
    def upgrade():
        """
        Apply configuration upgrades to an existing Datasette instance
        """
        pass

    @upgrade.command()
    @click.argument("metadata", type=click.Path(exists=True))
    @click.option(
        "new_metadata",
        "-m",
        "--new-metadata",
        help="Path to new metadata.yaml file",
        type=click.Path(exists=False),
    )
    @click.option(
        "new_datasette",
        "-c",
        "--new-datasette",
        help="Path to new datasette.yaml file",
        type=click.Path(exists=False),
    )
    @click.option(
        "output_dir",
        "-e",
        "--output-dir",
        help="Directory to write new files to",
        type=click.Path(),
        default=".",
    )
    def metadata_to_config(metadata, new_metadata, new_datasette, output_dir):
        """
        Upgrade an existing metadata.json/yaml file to the new metadata.yaml and
        datasette.yaml split introduced prior to Datasette 1.0.
        """
        print("Upgrading {} to new metadata.yaml format".format(metadata))
        output_dir = pathlib.Path(output_dir)
        if not new_metadata:
            # Pick a filename for the new metadata.yaml file that does not yet exist
            new_metadata = pick_filename("metadata", output_dir)
        if not new_datasette:
            new_datasette = pick_filename("datasette", output_dir)
        old_metadata = parse_metadata(open(metadata).read()) or {}
        # Move "plugins" to config
        plugins = old_metadata.pop("plugins", {})
        permissions = old_metadata.pop("permissions", {})
        config = {}
        if plugins:
            config["plugins"] = plugins
        if permissions:
            config["permissions"] = permissions
        print("New metadata.yaml file will be written to {}".format(new_metadata))
        open(new_metadata, "w").write(yaml.dump(old_metadata))
        print("New datasette.yaml file will be written to {}".format(new_datasette))
        open(new_datasette, "w").write(yaml.dump(config))


def pick_filename(base, output_dir):
    options = ["{}.yaml".format(base), "{}-new.yaml".format(base)]
    i = 0
    while True:
        option = options.pop(0)
        option_path = output_dir / option
        if not option_path.exists():
            return option_path
        # If we ran out
        if not options:
            i += 1
            options = ["{}-new-{}.yaml".format(base, i)]
