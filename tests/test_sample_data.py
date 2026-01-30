import csv
import pathlib


def test_sample_has_expected_columns():
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    sample = repo_root / "data" / "sample_small.csv"
    assert sample.exists(), "sample_small.csv must exist for quick tests"

    with sample.open(newline='') as f:
        reader = csv.reader(f)
        header = next(reader)

    expected = {"Month", "AA"}
    assert expected.issubset(set(header)), (
        f"Header must include {expected}, got {header}"
    )
