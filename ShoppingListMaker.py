items = []
while True:
    item = input("Add item (or type 'done'): ")
    if item.lower() == 'done': break
    items.append(item)
print(f"Your shopping list: {', '.join(items)}")