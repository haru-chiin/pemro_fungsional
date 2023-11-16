#percobaan 1
# Curry function
def perkalian(a):
    def dengan(b):
        nonlocal a
        return a * b
    return dengan

# HOF
def curry_perkalian(a):
    def inner(b):
        return a * b
    return inner

# Panggil HOF
hof_result = curry_perkalian(5)(3)
print("Hasil HOF:", hof_result)

# Panggil Currying
curry_result = perkalian(5)(3)
print("Hasil Currying:", curry_result)



