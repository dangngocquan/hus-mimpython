def solve_quadratic_equation_2(a, b, c):
    answer_tuple = ()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
        else:
            answer_tuple = (-c / b, )
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            answer_tuple = (-b / (2*a), )
        elif delta > 0:
            answer_tuple = ((-b - delta**(1/2)) / (2*a), (-b + delta**(1/2)) / (2*a))
    return answer_tuple

if __name__ == '__main__':
    print(solve_quadratic_equation_2(1, 1, -2)) # (-2.0, 1.0)
    print(solve_quadratic_equation_2(1, 2, 1))  # (-1.0,)
    print(solve_quadratic_equation_2(1, 0, 1))  # ()
    print(solve_quadratic_equation_2(0, 0, 0))  # ()