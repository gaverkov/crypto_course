class Coset:
    """
    Represents a coset [a]_n in Z/nZ.

    Designed for teaching:
    - No implicit conversion between int and Coset
    - Explicit algebraic operations only
    """

    def __init__(self, rep, mod):
        if not isinstance(rep, int):
            raise TypeError("Representative must be an integer")
        if not isinstance(mod, int) or mod <= 0:
            raise ValueError("mod must be a positive integer")

        self.mod = mod
        self.rep = rep % mod

    # -------------------------
    # Membership: x ∈ [a]_n
    # -------------------------
    def __contains__(self, x):
        if not isinstance(x, int):
            return False
        return (x - self.rep) % self.mod == 0

    # -------------------------
    # Addition: [a]_n + [b]_n
    # -------------------------
    def __add__(self, other):
        if not isinstance(other, Coset):
            return NotImplemented
        if self.mod != other.mod:
            raise ValueError("Cannot add cosets with different moduli")

        return Coset(self.rep + other.rep, self.mod)

    # -------------------------
    # Multiplication:
    # Coset * Coset or scalar multiplication
    # -------------------------
    def __mul__(self, other):
        # Coset multiplication
        if isinstance(other, Coset):
            if self.mod != other.mod:
                raise ValueError("Cannot multiply cosets with different moduli")
            return Coset(self.rep * other.rep, self.mod)

        # Scalar multiplication (right)
        if isinstance(other, int):
            return Coset(self.rep * other, self.mod)

        return NotImplemented

    # Scalar multiplication (left)
    def __rmul__(self, other):
        if isinstance(other, int):
            return Coset(self.rep * other, self.mod)
        return NotImplemented

    # -------------------------
    # Equality (strict)
    # -------------------------
    def __eq__(self, other):
        return (
            isinstance(other, Coset)
            and self.rep == other.rep
            and self.mod == other.mod
        )

    # -------------------------
    # Pretty printing: [a]_n
    # -------------------------
    def __repr__(self):
        return f"[{self.rep}]_{self.mod}"


# =========================================================
# Factory function
# =========================================================

def coset(z, mod):
    return Coset(z, mod)


# =========================================================
# Z_mod(n): full residue system { [0], ..., [n-1] }
# =========================================================

def Z_mod(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    return [coset(z, n) for z in range(n)]