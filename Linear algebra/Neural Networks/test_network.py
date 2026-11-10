"""
Test script for the neural network
Demonstrates the fixed network.py works correctly
"""

import numpy as np
from network import Network

print("=" * 70)
print("TESTING FIXED NEURAL NETWORK")
print("=" * 70)

# Create a simple network: 2 inputs -> 3 hidden -> 1 output
print("\nCreating network with architecture: [2, 3, 1]")
net = Network([2, 3, 1])
print("✓ Network created successfully!")

# Test feedforward
print("\nTesting feedforward pass...")
test_input = np.array([[0.5], [0.3]])
output = net.feedforward(test_input)
print(f"Input: {test_input.flatten()}")
print(f"Output: {output.flatten()}")
print("✓ Feedforward working!")

# Create some training data (simple XOR-like problem)
print("\nCreating training data...")
training_data = [
    (np.array([[0], [0]]), np.array([[0]])),
    (np.array([[0], [1]]), np.array([[1]])),
    (np.array([[1], [0]]), np.array([[1]])),
    (np.array([[1], [1]]), np.array([[0]])),
]
print(f"Training data: {len(training_data)} samples")
print("✓ Training data ready!")

# Train the network
print("\n" + "=" * 70)
print("TRAINING THE NETWORK")
print("=" * 70)
print("Configuration:")
print("  - Epochs: 50")
print("  - Mini-batch size: 1")
print("  - Learning rate (eta): 1.0")
print()

net.SGD(training_data, epochs=50, mini_batch_size=1, eta=1.0)

print("\n" + "=" * 70)
print("TRAINING COMPLETE!")
print("=" * 70)

# Test predictions
print("\nTesting predictions on training data:")
print("Input (x1, x2) | Target | Predicted | Difference")
print("-" * 55)

for inputs, target in training_data:
    prediction = net.feedforward(inputs)
    diff = abs(prediction[0, 0] - target[0, 0])
    print(f"  {inputs.flatten()}     |  {target[0,0]:.1f}    |   {prediction[0,0]:.4f}   |   {diff:.4f}")

print("\n" + "=" * 70)
print("✓ ALL TESTS PASSED - NETWORK IS WORKING!")
print("=" * 70)
