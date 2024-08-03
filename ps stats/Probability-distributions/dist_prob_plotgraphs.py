# Función de Distribución de Probabilidad Normal - Visualización del área del calculo y resultados
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import binom

def distr_prob(dist, a=None, b=None, between=True, pdx=False):
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
     pdx: True indica que se pone en el grafico la probabilidad correspondiente a x/z crítico.
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

    if dist.dist.name == 'norm':
            is_standard = (dist.mean() == 0 and dist.std() == 1)
    elif dist.dist.name == 'uniform':
            is_standard = (dist.mean() == 0.5 and dist.std() == (1/12)**0.5)
    
    x = 'x' if is_standard else 'z'
    print(f"dist: {dist.dist.name}, is_standard: {is_standard}, dist.mean: {dist.mean()}, dist.std:{dist.std()}")
     
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
        if pdx:
            ax.text(a, dist.pdf(a), f'p={dist.pdf(a):.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de p(b)
    
    # Añadir texto de valor de variable "b" y su probabilidad "p(b)"
    if b < x_max:
        ax.text(b, 0.0, f'{x}={b:.3f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de x=b
        if pdx:
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

    # plt.show()
    return fig, ax

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
    print(f"Valores de Z o S  : {(iqa-mean)/sigm:.2f} y {(iqb-mean)/sigm:.2f}")
    print(f"Probs. acums.     : {pqa:.3f} y {pqb:.3f}.")
    print(f"Prob. a + b       : {pab*100:.2f}%.")
    distr_prob(dist, iqa, iqb)
    

def reg_critica(dist, rg=0.05, side='both'):
    """
    Esta función imprime los parametros y estadísticos de una función 
    y grafica la región crítica
    
    Args:
        dist: La distribución con sus parametros
        rg: probabilidad alfa de la región crítica
        side: both: indica si es bilateral, 'left': cola izquierda o 'der': derecha

    Raises:
        ValueError: 
        "Not a left, right or both sides"
    """
    
    # Vemos los estadísticos de la función de distirbución
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    sigm = math.sqrt(var)
    
    print(f"media: {mean}, desv.std.: {sigm} , sesgo: {skew}, kurtosis: {kurt})")
    print(f"α: {rg*100}%.")    
    
    match side:
        case 'both':
            a= rg/2                 # percentil izquierdo
            b= 1-a                  # percentil derecho
            iqa = dist.ppf(a)       
            iqb = dist.ppf(b)
            pqa = dist.cdf(iqa)     # probabilidad acumulada izquierda
            pqb = dist.sf(iqb)      # probabilidad acumulada derecha
            pab = pqb + pqa         # suma de probabilidades acumuladas
            print(f"Probs. acums.     : {pqa:.3f} y {pqb:.3f}.")
            print(f"Prob. a + b       : {pab*100:.2f}%.")
        case 'left':
            a=0
            b=rg
            iqa = dist.ppf(a)       
            iqb = dist.ppf(b)
            pqb = dist.cdf(iqb)     # probabilidad acumulada izquierda desde -infinito a b
            print(f"Prob. acum.     : {pqb:.3f} = {pqb*100:.2f}%.")
        case 'right':
            a=1-rg
            b=1
            iqa = dist.ppf(a)       
            iqb = dist.ppf(b)
            pqa = dist.sf(iqa)     # probabilidad acumulada derecha desde a al infinito
            print(f"Prob. acum.     : {pqa:.3f} = {pqa*100:.2f}%.")        
        case _:
            raise ValueError("Not a left, right or both sides")
    
    print(f"Percentiles a y b : {a:.3f} y {b:.3f}")
    print(f"Valores de x      : {iqa:.3f} y {iqb:.3f}.")
    print(f"Valores de Z o S  : {(iqa-mean)/sigm:.2f} y {(iqb-mean)/sigm:.2f}")

    match side:
        case 'both':
            fig, ax = distr_prob(dist, iqa, iqb, between=False)
        case 'left':
            fig, ax = distr_prob(dist, b=iqb)
        case 'right':
            fig, ax = distr_prob(dist, a=iqa)
        case _:
            raise ValueError("Not a point")
    return fig, ax
            
# plot_binom: función que plotea la distribución binomial
def plot_binom(n=100, p=0.4, alfa=0.05, tipo=None, ax=None):
    """
    Esta función plotea la distribución binomial.
    Opcional: grafica también el nivel de signigicancia alfa o el intervalo de confianza

    Args:
        n (int, optional): tamaño de la muestra. Defaults to 100.
        p (float, optional): proporción. Defaults to 0.4.
        alfa (float, optional): nivel de significancia. Defaults to 0.05.
        tipo (str, optional): indica si se marca: cola izquierda, derecha, IC o nada. Defaults to 'none'.
    
    Returns:
        fig: Objeto Figure de matplotlib.
        ax: Objeto Axes de matplotlib.
    """
    # construcción de eje x para toda la distribución binomial de percentiles 0 a 100
    x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
    
    # plotea la función de distribución binomial de percentiles 0 a 100
    # Si se proporciona un eje, usar ese eje en lugar de crear uno nuevo
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    else:
        fig = ax.get_figure()

    # averigua el valor de x correspondiente a cada percentil de 0 a 100
    ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    # plotea la linea vertical correspondiente al valor de x de cada percentil
    ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

    rv = binom(n,p)
    match tipo:
        case None:
            # si no hay intervalo ni alfa específico dibuja dibuja de nuevo toda la función de distribución
            ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
        case 'left':
            # alfa cola izquierda: plotea en rojo el alfa en la cola izquierda de la distirbución.
            x_alfa_l = np.arange(binom.ppf(0.01, n, p), binom.ppf(alfa, n, p))
            ax.vlines(x_alfa_l, 0, rv.pmf(x_alfa_l), colors='r', linestyles='-', lw=2, label=f'alfa {alfa}')
            ax.text(binom.ppf(alfa, n, p), -0.003, f'k={binom.ppf(alfa, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
        case 'right':
            # alfa cola derecha: plotea en rojo el alfa en la cola derecha de la ditribución.
            x_alfa_r = np.arange(binom.ppf(1-alfa, n, p), binom.ppf(0.99, n, p))
            ax.vlines(x_alfa_r, 0, rv.pmf(x_alfa_r), colors='r', linestyles='-', lw=2, label=f'alfa {alfa}')
            ax.text(binom.ppf(1-alfa, n, p), -0.003, f'k={binom.ppf(1-alfa, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
        case 'both':
            # alfa bilateral: divide el alfa en dos y los dibuja en las dos colas.
            x_alfa_l = np.arange(binom.ppf(0.01, n, p), binom.ppf(alfa/2, n, p))
            ax.vlines(x_alfa_l, 0, rv.pmf(x_alfa_l), colors='r', linestyles='-', lw=2, label=f'alfa {alfa/2}')
            x_alfa_r = np.arange(binom.ppf(1-alfa/2, n, p), binom.ppf(0.99, n, p))
            ax.vlines(x_alfa_r, 0, rv.pmf(x_alfa_r), colors='r', linestyles='-', lw=2, label=f'alfa {alfa/2}')
            ax.text(binom.ppf(alfa/2, n, p), -0.003, f'k={binom.ppf(alfa/2, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
            ax.text(binom.ppf(1-alfa/2, n, p), -0.003, f'k={binom.ppf(1-alfa/2, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
        case 'IC':
            # intervalo de confianza: calcula el IC = 1- alfa y lo dibuja
            x_ic = np.arange(binom.ppf(alfa/2, n, p), binom.ppf(1-alfa/2, n, p))
            ax.vlines(x_ic, 0, rv.pmf(x_ic), colors='k', linestyles='-', lw=2, label=f'IC {1-alfa}')
            ax.text(binom.ppf(alfa/2, n, p), -0.003, f'k={binom.ppf(alfa/2, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
            ax.text(binom.ppf(1-alfa/2, n, p), -0.003, f'k={binom.ppf(1-alfa/2, n, p):.0f}', ha='center', va='bottom', color='red', fontsize=8)   # Añade valor de k=a
        case _ :
            print("*** Por favor indique tipo de plot: none, left, right, both, IC y alfa. ***")
                    
    ax.legend(loc='best', frameon=False)
    return fig, ax
