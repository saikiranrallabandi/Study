"""
MACHINE LEARNING WITH CALCULUS
Linear Regression using Gradient Descent from Scratch
Shows how derivatives power machine learning!
"""

import math


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"{title}")
    print("=" * 80)


# ================== SAMPLE DATA ==================
print_section("SAMPLE DATA: House Prices")

# Training data: (square feet, price in $1000s)
data = [
    (1, 2),      # 1000 sq ft → $2000
    (2, 4),      # 2000 sq ft → $4000
    (3, 6),      # 3000 sq ft → $6000
    (4, 8),      # 4000 sq ft → $8000
    (5, 10),     # 5000 sq ft → $10000
]

print("\nTraining Data:")
print("Square Feet (x) | Price in $1000s (y)")
for x, y in data:
    print(f"      {x}         |        {y}")

n = len(data)  # Number of data points
print(f"\nTotal data points: {n}")

# ================== LINEAR REGRESSION MODEL ==================
print_section("THE MODEL: y = mx + b")

print("""
We want to find the best values for:
  m = slope (weight) - how much does price increase per sq ft?
  b = intercept (bias) - base price

Goal: Find m and b that minimize prediction error
""")

# ================== LOSS FUNCTION ==================
print_section("STEP 1: LOSS FUNCTION (Mean Squared Error)")

print("""
Loss = (1/n) · Σ(predicted - actual)²
     = (1/n) · Σ(mx + b - y)²

This measures how wrong our predictions are.
Lower loss = better model
""")


def calculate_loss(data, m, b):
    """Calculate Mean Squared Error Loss"""
    total_error = 0
    for x, y in data:
        predicted = m * x + b
        error = (predicted - y) ** 2
        total_error += error

    loss = total_error / len(data)
    return loss


# Initial random guess
m = 0.5
b = 0.5

initial_loss = calculate_loss(data, m, b)
print(f"\nInitial guess: m = {m}, b = {b}")
print(f"Initial Loss: {initial_loss:.4f}")

# ================== DERIVATIVES (GRADIENTS) ==================
print_section("STEP 2: CALCULATE DERIVATIVES (Gradients)")

print("""
To find the direction to improve m and b, we calculate:

∂Loss/∂m = (2/n) · Σ(mx + b - y) · x
∂Loss/∂b = (2/n) · Σ(mx + b - y)

These tell us:
- How much loss changes if we change m
- How much loss changes if we change b
""")


def calculate_gradients(data, m, b):
    """Calculate partial derivatives (gradients)"""
    n = len(data)

    # Initialize gradients
    grad_m = 0
    grad_b = 0

    # Sum the errors for each data point
    for x, y in data:
        predicted = m * x + b
        error = predicted - y

        # ∂Loss/∂m = (2/n) · Σ(error) · x
        grad_m += error * x

        # ∂Loss/∂b = (2/n) · Σ(error)
        grad_b += error

    # Average the gradients
    grad_m = (2 / n) * grad_m
    grad_b = (2 / n) * grad_b

    return grad_m, grad_b


grad_m, grad_b = calculate_gradients(data, m, b)
print(f"\nInitial Gradients:")
print(f"∂Loss/∂m = {grad_m:.4f}")
print(f"∂Loss/∂b = {grad_b:.4f}")

print(f"\nInterpretation:")
print(f"- If we increase m, loss changes by {grad_m:.4f} per unit")
print(f"- If we increase b, loss changes by {grad_b:.4f} per unit")

# ================== GRADIENT DESCENT ==================
print_section("STEP 3: GRADIENT DESCENT (Learning)")

print("""
Update Rule:
  m_new = m_old - learning_rate · (∂Loss/∂m)
  b_new = b_old - learning_rate · (∂Loss/∂b)

We move in the OPPOSITE direction of the gradient (downhill)
learning_rate controls how big each step is
""")

# Training parameters
learning_rate = 0.01
iterations = 100

# Store history for visualization
history = {
    'iteration': [],
    'loss': [],
    'm': [],
    'b': []
}

# Initial values
m = 0.5
b = 0.5

print(f"\nStarting Gradient Descent:")
print(f"Learning Rate: {learning_rate}")
print(f"Iterations: {iterations}")
print(f"\nIteration | Loss      | m      | b")
print("-" * 40)

for iteration in range(iterations):
    # Calculate current loss
    loss = calculate_loss(data, m, b)

    # Store history
    history['iteration'].append(iteration)
    history['loss'].append(loss)
    history['m'].append(m)
    history['b'].append(b)

    # Print progress (every 10 iterations)
    if iteration % 10 == 0:
        print(f"{iteration:^9} | {loss:^9.4f} | {m:^6.3f} | {b:^6.3f}")

    # Calculate gradients
    grad_m, grad_b = calculate_gradients(data, m, b)

    # Update parameters (gradient descent step)
    m = m - learning_rate * grad_m
    b = b - learning_rate * grad_b

# Final iteration
loss = calculate_loss(data, m, b)
history['iteration'].append(iterations)
history['loss'].append(loss)
history['m'].append(m)
history['b'].append(b)
print(f"{iterations:^9} | {loss:^9.4f} | {m:^6.3f} | {b:^6.3f}")

# ================== RESULTS ==================
print_section("FINAL RESULTS")

print(f"\nLearned Model: y = {m:.4f}x + {b:.4f}")
print(f"Final Loss: {loss:.6f}")

print(f"\nImprovement:")
initial_loss = history['loss'][0]
final_loss = history['loss'][-1]
improvement = (initial_loss - final_loss) / initial_loss * 100
print(f"Loss reduced by {improvement:.1f}%")
print(f"From {initial_loss:.4f} → {final_loss:.4f}")

# ================== PREDICTIONS ==================
print_section("PREDICTIONS ON TEST DATA")

print("\nUsing learned model: y = {:.4f}x + {:.4f}".format(m, b))
print("\nSquare Feet | Actual Price | Predicted Price | Error")
print("-" * 55)

for x, actual_y in data:
    predicted_y = m * x + b
    error = abs(predicted_y - actual_y)
    print(f"    {x}      |      {actual_y}       |      {predicted_y:.2f}       | {error:.2f}")

# ================== KEY INSIGHTS ==================
print_section("KEY INSIGHTS: How Calculus Powers ML")

print("""
1. DERIVATIVES SHOW THE DIRECTION:
   - ∂Loss/∂m tells us how m affects the loss
   - ∂Loss/∂b tells us how b affects the loss
   - Negative gradient = move in that direction to reduce loss

2. CHAIN RULE IN ACTION:
   - Loss depends on m and b
   - m and b affect predictions
   - Predictions affect errors
   - Chain Rule: ∂Loss/∂m = ∂Loss/∂predicted · ∂predicted/∂m

3. GRADIENT DESCENT:
   - Iteratively follow the gradient (slope) downhill
   - Each step: update parameters = old - learning_rate · gradient
   - Eventually converge to optimal values

4. PARTIAL DERIVATIVES:
   - ∂Loss/∂m: derivative with respect to m (treat b as constant)
   - ∂Loss/∂b: derivative with respect to b (treat m as constant)
   - Used to update each parameter independently

5. LEARNING RATE:
   - Too small: learning is slow
   - Too large: might overshoot and diverge
   - Balance is key!
""")

print("=" * 80)
print("This is how neural networks learn! Just with millions of parameters instead of 2!")
print("=" * 80)
