class World:
    def __init__(self):
        self.chunks = {}
        self.load_world()

    def load_world(self):
        # Load or generate chunks here
        pass

    def get_chunk(self, x, z):
        # Retrieve a chunk based on its coordinates
        return self.chunks.get((x, z))

    def generate_chunk(self, x, z):
        # Generate a new chunk and add it to the world
        chunk = Chunk(x, z)
        self.chunks[(x, z)] = chunk
        return chunk

    def update(self):
        # Update the world state
        for chunk in self.chunks.values():
            chunk.update()

    def render(self, surface):
        # Render all chunks in the world
        for chunk in self.chunks.values():
            chunk.render(surface)