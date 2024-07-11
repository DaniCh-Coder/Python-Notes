    
import math
from scipy.stats import norm, uniform, rv_continuous, rv_discrete
    
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
    print(f"Valores de sigma  : {(mean-iqa)/sigm:.2f} y {(iqb-mean)/sigm:.2f}")
    print(f"Probs. acums.     : {pqa:.3f} y {pqb:.3f}.")
    print(f"Prob. a + b       : {pab*100:.2f}%.")
    distr_prob(norm(loc=mean, scale=sigm), a=iqa, b=iqb)
