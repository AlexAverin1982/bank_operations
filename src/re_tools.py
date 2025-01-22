import re


def find_matches_in_description(
    operations: list[dict], pattern: str, case_sensitive: bool = False
) -> list[dict]:
    result = []
    flags = 0
    if not case_sensitive:
        flags = re.IGNORECASE
    for operation in operations:
        description = operation.get("description", "")
        if description and re.search(pattern, description, flags=flags):
            result.append(operation)
    return result
