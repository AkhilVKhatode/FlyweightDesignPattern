import random

class ParticleType:
    def __init__(self, color, sprite):
        self.color = color
        self.sprite = sprite

    def render(self, x, y, velocity):
        print(f"Rendering {self.color} particle at ({x},{y}) with sprite {self.sprite}")

class ParticleTypeFactory:
    def __init__(self):
        self.particle_types = {}

    def get_particle_type(self, color, sprite):
        key = f"{color}_{sprite}"
        if key not in self.particle_types:
            self.particle_types[key] = ParticleType(color, sprite)
        return self.particle_types[key]

class Particle:
    def __init__(self, particle_type, x, y, velocity):
        self.type = particle_type  # reference to flyweight
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        self.y += self.velocity
        self.type.render(self.x, self.y, self.velocity)

def main():
    factory = ParticleTypeFactory()
    particles = []
    
    # Create thousands of particles using shared flyweights
    explosion_type = factory.get_particle_type("red", "explosion.png")
    
    for _ in range(1000):
        particles.append(Particle(explosion_type,
                                  random.random() * 100,
                                  random.random() * 100,
                                  1.0))
    
    # Update all particles
    for particle in particles:
        particle.update()

if __name__ == "__main__":
    main()
