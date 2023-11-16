def point(x,y):
    return x,y

def line_equation_of(p1, M):
    def calculate_C(p1, M):
        x, y = p1
        return y - M * x

    C = calculate_C(p1, M)
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
print(line_equation_of(point(6,-2),-2))
#nim saya 252
print("Persamaan garis yang melalui titik (2,5) dan bergradien 2:")
print(line_equation_of(point(2,5),2))