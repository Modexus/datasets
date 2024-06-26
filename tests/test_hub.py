from urllib.parse import quote

import pytest

from datasets.utils.hub import hf_dataset_url


@pytest.mark.parametrize("repo_id", ["canonical_dataset_name", "org-name/dataset-name"])
@pytest.mark.parametrize("filename", ["filename.csv", "filename with blanks.csv"])
@pytest.mark.parametrize("revision", [None, "v2"])
def test_dataset_url(repo_id, filename, revision):
    url = hf_dataset_url(repo_id=repo_id, filename=filename, revision=revision)
    assert url == f"https://huggingface.co/datasets/{repo_id}/resolve/{revision or 'main'}/{quote(filename)}"
