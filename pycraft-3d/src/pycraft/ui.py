class UI:
    def __init__(self):
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible

    def draw(self, screen):
        if self.menu_visible:
            # Draw the menu overlay
            pass  # Implement menu drawing logic here

    def update(self):
        # Update UI elements if necessary
        pass  # Implement UI update logic here