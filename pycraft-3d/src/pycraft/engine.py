class GameEngine:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 0

    def start(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.delta_time = self.clock.tick(60) / 1000.0  # Frame time in seconds

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Update game state logic here

    def render(self):
        pass  # Render the game world and objects here

    def stop(self):
        self.running = False