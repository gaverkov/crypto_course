from Z_mod import coset, Z_mod


print("=== Z/5Z as a list of cosets ===")
Z5 = Z_mod(5)
print(Z5)


print("\n=== Membership test ===")
print("5 ∈ [2]_3:", 5 in coset(2, mod=3))
print("4 ∈ [2]_3:", 4 in coset(2, mod=3))
print("8 ∈ [2]_3:", 8 in coset(2, mod=3))


print("\n=== Coset addition ===")
a = coset(2, mod=5)
b = coset(3, mod=5)
print("[2]_5 + [3]_5 =", a + b)


print("\n=== Coset multiplication ===")
print("[2]_5 * [3]_5 =", a * b)


print("\n=== Scalar multiplication ===")
print("3 · [2]_5 =", 3 * a)
print("[2]_5 · 3 =", a * 3)


print("\n=== Structure check ===")
print("Z_mod(5) elements:")
for x in Z5:
    print(" ", x)