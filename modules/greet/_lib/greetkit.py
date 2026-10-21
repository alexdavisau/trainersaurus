import json


def expect(ok, message):
    """Print one fail line (AUTHORING §5.5) unless ok."""
    if not ok:
        print(json.dumps({"fail": message}))
