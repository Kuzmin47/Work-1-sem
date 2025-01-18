def main():
    import matplotlib.pyplot as plt
    import numpy as np
    from findiff import FinDiff                                        
    from scipy.integrate import quad                                    

    def f(sx):
        return 2**(sx**4)*np.cos(20*sx**2+5)

    def deriv(fx, sx):
        h = 0.00000000001
        return (fx(sx+h) - fx(sx)) / h

    def curve_length_formula(sx):
        return np.sqrt(1 + deriv(f, sx) ** 2)

    x = np.linspace(0, 1, 10000)

    y_max = max(f(x))
    x_pos = list(f(x)).index(max(f(x)))
    x_max = x[x_pos]

    x0 = float(input('Введите точку x0 касательной и нормали: '))
    k = f(x0) + deriv(f, x0) * (x - x0)
    n = f(x0) - (x - x0) / deriv(f, x0)

    ax = plt.subplot(2, 3, 1)
    plt.plot(x, f(x))
    plt.grid()
    plt.ylim(-2.5, 2.5)
    plt.title("f(x)")
    plt.plot([x_max], [y_max], 'o', color='b')
    plt.plot(x, k)
    plt.plot(x, n)

    dx = x[1] - x[0]

    df_dx = FinDiff(0, dx)                                         
    plt.subplot(2, 3, 2)
    plt.plot(x, df_dx(f(x)))                                       
    plt.grid()
    plt.title("f'(x)")

    # Создание второй производной
    d2f_dx2 = FinDiff(0, dx, 2)                                 
    plt.subplot(2, 3, 3)
    plt.plot(x, d2f_dx2(f(x)))                                
    plt.grid()
    plt.title("f''(x)")

    plt.subplot(2, 1, 2)
    plt.plot(x, f(x))
    plt.grid()
    plt.ylim(-2.5, 2.5)
    plt.title('Касательное расслоение f(x)')
    short_x = np.linspace(0, 1, 10)                     
    for pos in short_x:
        k_pos = f(pos) + deriv(f, pos) * (short_x - pos)
        plt.plot(short_x, k_pos, 'r')

    curve_l = quad(curve_length_formula, 0, 1)                     
    print(curve_l[0])                                                   

    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()


if __name__ == '__main__':
    main()
