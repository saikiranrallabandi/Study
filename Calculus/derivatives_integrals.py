"""
CALCULUS PRACTICE PROBLEMS
Derivatives, Integrals, Chain Rule, and Partial Derivatives
Beginner Level - Focus on Mechanics
"""

from sympy import symbols, diff, integrate, simplify, sqrt, sin, cos, exp, ln
from sympy import oo  # infinity


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)


def print_problem(num, problem_text):
    """Print a formatted problem"""
    print(f"\n{num}. {problem_text}")


def print_solution(solution_text):
    """Print a formatted solution"""
    print(f"   Solution: {solution_text}")


# ================== 1. DERIVATIVES (Basic) ==================
print_section("1. DERIVATIVES - BASIC MECHANICS")
print("\nPower Rule: d/dx(x^n) = n·x^(n-1)")
print("Product Rule: d/dx(u·v) = u'·v + u·v'")
print("Quotient Rule: d/dx(u/v) = (u'·v - u·v') / v²")
print("Constant Rule: d/dx(c) = 0")

x = symbols('x')

# Problem 1.1
print_problem("1.1", "Find the derivative of f(x) = x³")
f1 = x**3
f1_prime = diff(f1, x)
print(f"   f(x) = {f1}")
print_solution(f"d/dx(x³) = {f1_prime}")

# Problem 1.2
print_problem("1.2", "Find the derivative of f(x) = 5x² - 3x + 7")
f2 = 5*x**2 - 3*x + 7
f2_prime = diff(f2, x)
print(f"   f(x) = {f2}")
print_solution(f"d/dx(5x² - 3x + 7) = {f2_prime}")

# Problem 1.3
print_problem("1.3", "Find the derivative of f(x) = 1/x (or x⁻¹)")
f3 = 1/x
f3_prime = diff(f3, x)
print(f"   f(x) = {f3}")
print_solution(f"d/dx(1/x) = {f3_prime}")

# Problem 1.4
print_problem("1.4", "Find the derivative of f(x) = √x (or x^(1/2))")
f4 = sqrt(x)
f4_prime = diff(f4, x)
print(f"   f(x) = {f4}")
print_solution(f"d/dx(√x) = {f4_prime}")

# Problem 1.5
print_problem("1.5", "Find the derivative of f(x) = sin(x)")
f5 = sin(x)
f5_prime = diff(f5, x)
print(f"   f(x) = {f5}")
print_solution(f"d/dx(sin(x)) = {f5_prime}")

# ================== 2. CHAIN RULE ==================
print_section("2. CHAIN RULE - dy/dx = (dy/du) · (du/dx)")
print("\nUsed when you have a composite function: f(g(x))")

# Problem 2.1
print_problem("2.1", "Find the derivative of f(x) = (x² + 1)³")
print("   Let u = x² + 1, then f(x) = u³")
print("   du/dx = 2x")
print("   df/du = 3u²")
print("   df/dx = (df/du) · (du/dx) = 3u² · 2x = 3(x²+1)² · 2x = 6x(x²+1)²")
f2_1 = (x**2 + 1)**3
f2_1_prime = diff(f2_1, x)
print_solution(f"d/dx((x² + 1)³) = {f2_1_prime}")

# Problem 2.2
print_problem("2.2", "Find the derivative of f(x) = sin(3x)")
print("   Let u = 3x, then f(x) = sin(u)")
print("   du/dx = 3")
print("   df/du = cos(u)")
print("   df/dx = cos(3x) · 3 = 3cos(3x)")
f2_2 = sin(3*x)
f2_2_prime = diff(f2_2, x)
print_solution(f"d/dx(sin(3x)) = {f2_2_prime}")

# Problem 2.3
print_problem("2.3", "Find the derivative of f(x) = e^(2x)")
print("   Let u = 2x, then f(x) = e^u")
print("   du/dx = 2")
print("   df/du = e^u")
print("   df/dx = e^(2x) · 2 = 2e^(2x)")
f2_3 = exp(2*x)
f2_3_prime = diff(f2_3, x)
print_solution(f"d/dx(e^(2x)) = {f2_3_prime}")

# Problem 2.4
print_problem("2.4", "Find the derivative of f(x) = (5x³ + 2)⁴")
f2_4 = (5*x**3 + 2)**4
f2_4_prime = diff(f2_4, x)
print(f"   Using chain rule with u = 5x³ + 2")
print_solution(f"d/dx((5x³ + 2)⁴) = {f2_4_prime}")

# ================== 3. INTEGRALS ==================
print_section("3. INTEGRALS - BASIC MECHANICS")
print("\nPower Rule: ∫x^n dx = x^(n+1)/(n+1) + C  (n ≠ -1)")
print("Constant Rule: ∫c dx = c·x + C")
print("Sum Rule: ∫(f + g) dx = ∫f dx + ∫g dx")

# Problem 3.1
print_problem("3.1", "Find the integral of f(x) = x³")
f3_1 = x**3
integral3_1 = integrate(f3_1, x)
print(f"   f(x) = {f3_1}")
print_solution(f"∫x³ dx = {integral3_1} + C")

# Problem 3.2
print_problem("3.2", "Find the integral of f(x) = 3x² - 2x + 5")
f3_2 = 3*x**2 - 2*x + 5
integral3_2 = integrate(f3_2, x)
print(f"   f(x) = {f3_2}")
print_solution(f"∫(3x² - 2x + 5) dx = {integral3_2} + C")

# Problem 3.3
print_problem("3.3", "Find the integral of f(x) = 1/x")
f3_3 = 1/x
integral3_3 = integrate(f3_3, x)
print(f"   f(x) = {f3_3}")
print_solution(f"∫(1/x) dx = {integral3_3} + C")

# Problem 3.4
print_problem("3.4", "Find the integral of f(x) = cos(x)")
f3_4 = cos(x)
integral3_4 = integrate(f3_4, x)
print(f"   f(x) = {f3_4}")
print_solution(f"∫cos(x) dx = {integral3_4} + C")

# Problem 3.5
print_problem("3.5", "Find the integral of f(x) = e^x")
f3_5 = exp(x)
integral3_5 = integrate(f3_5, x)
print(f"   f(x) = {f3_5}")
print_solution(f"∫e^x dx = {integral3_5} + C")

# Problem 3.6
print_problem("3.6", "Find the definite integral ∫₀² (2x + 1) dx")
f3_6 = 2*x + 1
definite_integral = integrate(f3_6, (x, 0, 2))
print(f"   f(x) = {f3_6}")
print(f"   Upper limit = 2, Lower limit = 0")
print_solution(f"∫₀² (2x + 1) dx = {definite_integral}")

# ================== 4. PARTIAL DERIVATIVES ==================
print_section("4. PARTIAL DERIVATIVES")
print("\nFor functions with multiple variables: f(x, y, z, ...)")
print("Partial derivative ∂f/∂x means: take derivative with respect to x, treat others as constants")

x, y = symbols('x y')

# Problem 4.1
print_problem("4.1", "Find ∂f/∂x and ∂f/∂y for f(x, y) = x² + 3xy + y²")
f4_1 = x**2 + 3*x*y + y**2
df4_1_dx = diff(f4_1, x)
df4_1_dy = diff(f4_1, y)
print(f"   f(x, y) = {f4_1}")
print(f"   ∂f/∂x = {df4_1_dx}")
print_solution(f"∂f/∂y = {df4_1_dy}")

# Problem 4.2
print_problem("4.2", "Find ∂f/∂x and ∂f/∂y for f(x, y) = x²·y + x·y²")
f4_2 = x**2 * y + x * y**2
df4_2_dx = diff(f4_2, x)
df4_2_dy = diff(f4_2, y)
print(f"   f(x, y) = {f4_2}")
print(f"   ∂f/∂x = {df4_2_dx}")
print_solution(f"∂f/∂y = {df4_2_dy}")

# Problem 4.3
print_problem("4.3", "Find ∂f/∂x and ∂f/∂y for f(x, y) = sin(x)·cos(y)")
f4_3 = sin(x) * cos(y)
df4_3_dx = diff(f4_3, x)
df4_3_dy = diff(f4_3, y)
print(f"   f(x, y) = {f4_3}")
print(f"   ∂f/∂x = {df4_3_dx}")
print_solution(f"∂f/∂y = {df4_3_dy}")

# Problem 4.4
print_problem("4.4", "Find ∂f/∂x and ∂f/∂y for f(x, y) = e^(x+y)")
f4_4 = exp(x + y)
df4_4_dx = diff(f4_4, x)
df4_4_dy = diff(f4_4, y)
print(f"   f(x, y) = {f4_4}")
print(f"   ∂f/∂x = {df4_4_dx}")
print_solution(f"∂f/∂y = {df4_4_dy}")

# ================== 5. PRACTICE PROBLEMS (Try These!) ==================
print_section("5. PRACTICE PROBLEMS - TRY THESE!")

print("\n--- Derivatives ---")
print("5.1) Find d/dx(x⁴ - 2x² + 3)")
print("5.2) Find d/dx(2sin(x) + 3cos(x))")
print("5.3) Find d/dx((3x + 1)⁵) using chain rule")
print("5.4) Find d/dx(x · sin(x)) using product rule")

print("\n--- Integrals ---")
print("5.5) Find ∫(4x³ - x) dx")
print("5.6) Find ∫(2x + e^x) dx")
print("5.7) Find ∫₁³ (x²) dx (definite integral)")
print("5.8) Find ∫sin(x) dx")

print("\n--- Partial Derivatives ---")
print("5.9) Find ∂f/∂x for f(x, y) = 3x²y + 2xy²")
print("5.10) Find ∂f/∂y for f(x, y) = x·e^y")

print("\n" + "=" * 70)
print("HINTS FOR PRACTICE PROBLEMS:")
print("=" * 70)
print("5.1: Use power rule on each term")
print("5.2: Derivatives of sin(x) and cos(x)")
print("5.3: Chain rule: d/dx(u^n) = n·u^(n-1)·(du/dx)")
print("5.4: Product rule: d/dx(u·v) = u'·v + u·v'")
print("5.5: Power rule in reverse for each term")
print("5.6: Integral of e^x is e^x")
print("5.7: Integrate, then evaluate at upper - lower limits")
print("5.8: ∫sin(x) dx = -cos(x) + C")
print("5.9: Treat y as constant when finding ∂f/∂x")
print("5.10: Treat x as constant when finding ∂f/∂y, remember (e^y)' = e^y")

print("\n" + "=" * 70)
print("KEY FORMULAS SUMMARY")
print("=" * 70)
print("""
DERIVATIVES:
• Power Rule: d/dx(x^n) = n·x^(n-1)
• Product Rule: d/dx(u·v) = u'·v + u·v'
• Chain Rule: d/dx(f(g(x))) = f'(g(x))·g'(x)
• sin(x)' = cos(x)
• cos(x)' = -sin(x)
• e^x' = e^x
• ln(x)' = 1/x

INTEGRALS:
• Power Rule: ∫x^n dx = x^(n+1)/(n+1) + C
• ∫sin(x) dx = -cos(x) + C
• ∫cos(x) dx = sin(x) + C
• ∫e^x dx = e^x + C
• ∫(1/x) dx = ln(x) + C

PARTIAL DERIVATIVES:
• ∂f/∂x: differentiate with respect to x, treat other variables as constants
• ∂f/∂y: differentiate with respect to y, treat other variables as constants
""")

print("=" * 70)
