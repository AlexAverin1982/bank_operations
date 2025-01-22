from collections import Counter


def count_categories(operations: list[dict], categories: list) -> dict:
    op_categories = []

    # categories = [cat.lower() for cat in categories]
    for operation in operations:
        category = str(operation.get("description"))           # .lower()
        if category in categories:
            op_categories.append(category)
    return dict(Counter(op_categories))
