# Función de Distribución de Probabilidad Normal - Visualización del área del calculo y resultados
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, rv_continuous, rv_discrete

def distr_prob(dist, a=None, b=None, between=True):
    """
     Función: Esta función grafica:
     1. La curva de distribución normal de probabilidad entre x_min y x_max
     2. El área de probabilidad acumulada bajo la curva entre a y b
     3. Coloca paremetros y resultados en el gráfico
     Argumentos:
     dist: Distribución de probabilidad a graficar.
     a: Límite inferior del rango de probabilidad buscado
     b: Límite superior del rango de probabilidad buscado
     between: True indica probabilidad entre a y b. False indica probabilidad fuera de a y b.
     Paremetros:
     x_rango: es el rango de x/z correspondiente a la curva de distribución.
     dist.loc=0 y dist.scale=1 se considera estandard
          Consideraciones sobre los parámetros a y b:
     + si se especifica a y b, la probabilidad acumulada entre a y b
     + si no se especifica ni a ni b, la función calcula la brobabilidad total entre minimo y maximo, es decir 100%
     + si no se especifica a, la función calcula desde el mínimo de la distribución hasta el limite b o el máximo.
     + si no se especifica b la función calcula desde a hasta el máximo
    """
# Verificar si 'dist' es una distribución estándar
    is_standard = False

    if isinstance(dist, rv_continuous):
        if dist.dist.name == 'norm':
            is_standard = (dist.mean() == 0 and dist.std() == 1)
        elif dist.dist.name == 'uniform':
            is_standard = (dist.mean() == 0.5 and dist.std() == (1/12)**0.5)
    
    x = 'x' if is_standard else 'z'
    
    # Rango de x de la funcion de distribución normal
    # Como la distribución es normal distribuye los valores desde negativos hasta positivos con media cero
    x_min = dist.ppf(0.00001) # devuelve el valor de probabilidad correspondiente al percentil especificado como argumento
    x_max = dist.ppf(0.99999) # devuelve el valor de probabilidad correspondiente al percentil especificado como argumento
    x_rango = np.linspace(x_min, x_max, 10000)  # rango de valores del eje x
    
    # Rango de x entre a y b
    a = x_min if a is None else a 
    b = x_max if b is None else b
    
    ### Líneas de debug
    # print(f"a:{a}, b:{b}")
    # cdfa = dist.cdf(a)
    # cdfb = dist.cdf(b)
    # cdfab = cdfb-cdfa
    # print(f"dist.cdf(b):{cdfa}")
    # print(f"dist.cdf(b):{cdfb}")
    # print(f"cdf a-b : {cdfab}")
    
    # Calculo del rango de x entre a y b que estoy buscando
    if between:
        ab_rango = np.linspace(a, b, 1000) # rango de valores de probabilidad acumulada buscado
    else:
        a_rango = np.linspace(x_min, a, 1000)
        b_rango = np.linspace(b, x_max, 1000)

    # Genero la plantilla del grafico
    fig, ax = plt.subplots(1, 1, figsize = (7,4))

    # Dibujo la distribución normal
    ax.plot(x_rango, dist.pdf(x_rango), 'k-', lw=2, alpha=0.6, label='norm pdf')

    # Sombreado del área bajo la curva de interés
    if between :
        ax.fill_between(ab_rango, 0, dist.pdf(ab_rango), color='blue', alpha=0.2, label='Área bajo la curva')
    else :
        ax.fill_between(a_rango, 0, dist.pdf(a_rango), color='blue', alpha=0.2, label='Área bajo la curva')
        ax.fill_between(b_rango, 0, dist.pdf(b_rango), color='blue', alpha=0.2, label='Área bajo la curva')

    # Dibujar las líneas punteadas en pdf(a), pdf(b)
    ax.plot([a, a], [0, dist.pdf(a)], linestyle="dashed")
    ax.plot([b, b], [0, dist.pdf(b)], linestyle="dashed")

    # Añadir texto de valor de variable "a" y su probabilidad "p(a)"
    if a > x_min:
        ax.text(a, 0.0, f'{x}={a:.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de x=a
        ax.text(a, dist.pdf(a), f'p={dist.pdf(a):.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de p(b)
    
    # Añadir texto de valor de variable "b" y su probabilidad "p(b)"
    if b < x_max:
        ax.text(b, 0.0, f'{x}={b:.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de x=b
        ax.text(b, dist.pdf(b), f'p={dist.pdf(b):.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de p(b)

    # Añadir texto probabilidad acumulada en el centro del gráfico
    x_centro = (x_rango.max() + x_rango.min()) / 2 # Punto medio del eje X
    y_centro = (dist.pdf(dist.mean())/2)  # Valor arbitrario en el eje Y (cerca del centro de la distribución)
    if between:
        ax.text(x_centro, y_centro, f"{(dist.cdf(b)-dist.cdf(a))*100:.1f}%", ha='center', va='center', fontsize=10, color='red')
    else:
        ax.text(x_centro, y_centro, f"{(dist.sf(b)+dist.cdf(a))*100:.1f}%", ha='center', va='center', fontsize=10, color='red')

    # Personalización del gráfico
    # ax.set_title('Distribución Normal Estandard')
    ax.set_xlabel(x)
    # ax.set_ylabel('Densidad de probabilidad')
    # ax.legend()
    # plt.grid(True)

    ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('gray')

    plt.show()

def inter_confi(dist, nc=0.95):
    # Vemos los estadísticos de la función de distirbución
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    sigm = math.sqrt(var)
  
    a= (1-nc)/2
    b= 1-a
    iqa = dist.ppf(a)
    iqb = dist.ppf(b)
    pqa = dist.cdf(iqa)
    pqb = dist.sf(iqb)
    pab = pqb + pqa

    print(f"media: {mean}, desv.std.: {sigm} , sesgo: {skew}, kurtosis: {kurt})")
    print(f"Nivel de confianza: {nc*100}%.")
    print(f"Percentiles a y b : {a:.3f} y {b:.3f}")
    print(f"Valores de x      : {iqa:.3f} y {iqb:.3f}.")
    print(f"Valores de sigma  : {(iqa-mean)/sigm:.2f} y {(iqb-mean)/sigm:.2f}")
    print(f"Probs. acums.     : {pqa:.3f} y {pqb:.3f}.")
    print(f"Prob. a + b       : {pab*100:.2f}%.")
    distr_prob(dist, iqa, iqb)
    
