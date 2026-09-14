import os

from src.logic import check_recent_files, check_hashes


def test_check_recent_files():
    folder = "data/sample_evidence"

    result = check_recent_files(folder)

    assert isinstance(result, list)


def test_check_hashes():
    folder = "data/sample_evidence"

    result = check_hashes(folder)

    assert isinstance(result, dict)
    assert len(result) == 3

    for filename, digest in result.items():
        assert os.path.exists(os.path.join(folder, filename))
        assert len(digest) == 64