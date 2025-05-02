# Particle System with Flyweight Pattern

This project implements a simple particle system using the Flyweight design pattern in Python. It simulates particles such as explosions using shared `ParticleType` objects to save memory and optimize rendering performance.

## Overview

In this project, we model particles like explosions using a shared `ParticleType` object for all particles of the same color and sprite. This approach reduces memory usage by ensuring that identical particle types are not recreated multiple times.

### Design Pattern: Flyweight

The **Flyweight** pattern is used to share common data (such as the color and sprite of the particle) between multiple particle objects, while allowing each individual particle to store its own specific properties (such as position and velocity). This reduces memory consumption when handling large numbers of particles.

## Classes

### 1. `ParticleType`
Represents a specific type of particle (e.g., color and sprite). This class is shared across multiple `Particle` instances.

#### Methods:
- `render(x, y, velocity)`: Renders the particle at the given position with the specified velocity.

### 2. `ParticleTypeFactory`
Responsible for creating and managing the shared `ParticleType` objects. It ensures that particles with the same color and sprite are reused.

#### Methods:
- `get_particle_type(color, sprite)`: Retrieves a `ParticleType` based on the color and sprite, creating a new one only if it doesn't already exist.

### 3. `Particle`
Represents an individual particle in the system. Each particle has its own position (`x`, `y`) and velocity, but shares a common `ParticleType` object for rendering.

#### Methods:
- `update()`: Updates the particle's position and renders it at the new position.

## Example Output
```csharp
Rendering red particle at (23.45, 45.67) with sprite explosion.png
Rendering red particle at (12.34, 56.78) with sprite explosion.png
...
```
