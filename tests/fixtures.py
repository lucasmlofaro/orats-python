import json
import os


def persist_fixture(endpoint, fixture, prefix="data"):
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, "fixtures", prefix, f"{endpoint}.json")
    with open(path, "w") as file:
        json.dump(fixture, file, indent=2)


def _resource(url):
    return "-".join(url.split("://")[1].split("/")[2:])


def load_fixture(url, *args, **kwargs):
    key = _resource(url)
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, "fixtures", "data", f"{key}.json")
    with open(path) as file:
        return json.load(file)["data"]
