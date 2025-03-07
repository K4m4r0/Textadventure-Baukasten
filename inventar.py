# inventar.py

class Item:
    def __init__(self, name, description, visible=True): #Gegenstände sichtbar für Spieler = visible=True, unsichtbar für Spieler = visible=False (für Gegenstände die ein Event triggern sollen zB)
        self.name = name
        self.description = description
        self.visible = visible

    def __str__(self):
        return f"{self.name}: {self.description}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item, suppress_output=False):
        self.items.append(item)
        if item.visible and not suppress_output:
            print(f"{item.name} wurde dem Inventar hinzugefügt.\n")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} wurde aus dem Inventar entfernt.\n")
                return item
        print(f"{item_name} nicht im Inventar gefunden.\n")
        return None

    def has_item(self, item_name):
        return any(item.name == item_name for item in self.items)

    def list_items(self):
        visible_items = [item for item in self.items if item.visible]
        if not visible_items:
            print("Das Inventar ist leer.\n")
        else:
            print("Inventarinhalt:")
            for item in visible_items:
                print(f"- {item}")

    def __str__(self):
        visible_items = [item for item in self.items if item.visible]
        if not visible_items:
            return "Das Inventar ist leer."
        return ', '.join(str(item) for item in visible_items)

    def to_dict(self):
        return [item.__dict__ for item in self.items]

    @classmethod
    def from_dict(cls, items_list, suppress_output=False):
        inventory = cls()
        for item_data in items_list:
            item = Item(item_data['name'], item_data['description'], item_data.get('visible', True))
            inventory.add_item(item, suppress_output=suppress_output)
        return inventory
