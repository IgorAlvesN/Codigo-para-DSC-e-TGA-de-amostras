import numpy as np

def derivada(data_x_axis,data_y_axis):                          # calcula a derivada numérica
    r=len(data_x_axis)
    data_derivada=[]
    for i in range(1,r):
        a=data_x_axis[i]
        b=data_x_axis[i+1]
        fa=data_y_axis[i]
        fb=data_y_axis[i+1]
        try:
            derivate=(fb-fa)/(b-a)
        except ZeroDivisionError:
            derivate=0
        if np.isposinf(derivate) or np.isneginf(derivate):
            derivate=0
        data_derivada.append(derivate)
    data_derivada.append(data_derivada[-1])
    return data_derivada

def integral(data_x_axis,data_y_axis):                          # calcula a integral numérica
    r=len(data_x_axis)
    data_integral=[]
    for i in range(1,r):
        a=data_x_axis[i]
        b=data_x_axis[i+1]
        fa=data_y_axis[i]
        fb=data_y_axis[i+1]
        integral=(b-a)*(fa+fb)/2
        data_integral.append(integral)
    data_integral.append(data_integral[-1])
    return data_integral



def reta_dado_pontos(x1,y1,x2,y2):          #calcula os coeficientes da reta dado dois pontos
    m=(y2-y1)/(x2-x1)
    c=y1-m*x1
    coeficientes=[m,c]
    return coeficientes

def linhabaseonset(intervalo_ref,intervalo_alvo,indice,valor=0):   #encontra a linha base do onset
    while intervalo_ref[indice].values[0]<valor:
        indice-=1
    
    valor=[intervalo_alvo[indice],indice]
    return valor

def linhabaseendset(intervalo_ref,intervalo_alvo,indice,valor=0):   #encontra a linha base do endset
    while intervalo_ref[indice].values[0]<valor:
        indice+=1
    
    valor=[intervalo_alvo[indice],indice]
    return valor


def picolocal(data,type,start,end):                             #encontra o pico local do intervalo
    intervalo=data.loc[start:end]
    if type=="min":
        result=intervalo.min()
    elif type=="max":
        result=intervalo.max()
    
    return result

def reta_perpend(y_start,y_end,x_value):                    # coordenadas de uma reta perpendicular ao eixo x
    coord=[]
    y_tt=np.arange(y_start,y_end,0.01)
    x_tt=[]
    for i in y_tt:
        x_tt.append(x_value)
    coord.append(x_tt)
    coord.append(y_tt)

    return coord 