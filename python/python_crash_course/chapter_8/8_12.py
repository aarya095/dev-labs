def collect_items_in_sandwich(*items):
    for item in items:
        print(f"I am adding {item} to your sandwich.")

collect_items_in_sandwich('cheese','tomato','potato')
collect_items_in_sandwich('tomato','potato')
collect_items_in_sandwich('cheese')