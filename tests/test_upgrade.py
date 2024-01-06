from click.testing import CliRunner
from datasette.cli import cli
import pathlib


def test_metadata_to_config(tmpdir):
    dir = pathlib.Path(tmpdir / "dir")
    dir.mkdir()
    metadata = dir / "metadata.json"
    metadata.write_text(
        """
        {
            "title": "My database",
            "plugins": {
                "datasette-cluster-map": {
                    "latitude_column": "lat",
                    "longitude_column": "lon"
                }
            },
            "permissions": {
                "foo": ["bar"]
            }
        }
    """
    )
    out_metadata = dir / "metadata.yaml"
    out_datasette = dir / "datasette.yaml"
    assert not out_metadata.exists()
    assert not out_datasette.exists()
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "upgrade",
            "metadata-to-config",
            str(metadata),
            "-m",
            str(out_metadata),
            "-c",
            str(out_datasette),
        ],
    )
    assert result.exit_code == 0, result.output
    assert out_metadata.exists()
    assert out_datasette.exists()
    assert out_metadata.read_text() == "title: My database\n"
    assert out_datasette.read_text() == (
        "permissions:"
        "\n  foo:"
        "\n  - bar"
        "\nplugins:"
        "\n  datasette-cluster-map:"
        "\n    latitude_column: lat"
        "\n    longitude_column: lon"
        "\n"
    )
