from scipy.signal import residue

# Given numerator and denominator coefficients
numerator_coeffs = [0.00257643, 0.01030574, 0.01545861, 0.01030574, 0.00257643]
denominator_coeffs = [1, -2.63862774, 2.76930979, -1.33928076, 0.24982167]

# Compute partial fraction expansion
P, Q, R = residue(numerator_coeffs, denominator_coeffs)

# Output partial fraction expansion coefficients
print("P:", P)
print("Q:", Q)
print("R:", R)
