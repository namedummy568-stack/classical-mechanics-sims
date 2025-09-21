import numpy as np

def simulate_harmonic_oscillator(mass, k, initial_position, initial_velocity, dt, num_steps):
    positions = [initial_position]
    velocities = [initial_velocity]
    
    for _ in range(num_steps):
        # Simple Euler integration (placeholder, not robust)
        acceleration = -k * positions[-1] / mass
        new_velocity = velocities[-1] + acceleration * dt
        new_position = positions[-1] + new_velocity * dt
        
        positions.append(new_position)
        velocities.append(new_velocity)
        
    return np.array(positions), np.array(velocities)

if __name__ == "__main__":
    # Example usage
    m = 1.0  # kg
    k = 1.0  # N/m
    x0 = 1.0 # m
    v0 = 0.0 # m/s
    delta_t = 0.01 # s
    steps = 1000
    
    pos, vel = simulate_harmonic_oscillator(m, k, x0, v0, delta_t, steps)
    
    print(f"Final position: {pos[-1]:.4f} m")
    print(f"Final velocity: {vel[-1]:.4f} m/s")
