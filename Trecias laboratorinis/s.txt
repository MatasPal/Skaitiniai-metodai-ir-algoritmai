import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint


def Euler():

    t = t0 # pradinis laikas
    TA = TA1 # Pradinė aplinkos temperatūra
    T = T1 # Pradinė kūno temperatūra

    print("Pradine kuno temperatura:", T)
    print("Pradine aplinkos temperatura:", TA)

    temperatura = []
    laikas = []
    aplinkosTemperatura = []


    while t != tmax: # Kol nepasiekė viso laiko momento
        if t == ts and TA != TA2: # kaip praeina ts sekundžių ir tol kol nepasiekė max temp TA2
            print("Pradeda kisti aplinkos temperatura")
            while TA != TA2: # tol kol nepasiekė max temperatūros TA2
                TA = TA1 + ((TA2-TA1)/2)*(1-np.cos(((math.pi)/20)*(t-ts))) # TA(t) dėsnis
                if TA == TA2:# kai pasieke aplinkos temperatūra
                    print("pasiekta aplinkos temperatura!", T, TA, t)
                    TA = TA2
                k = -0.01 - 0.16*((T-273)/100) - 0.04*((T-273)/100)**2 # k(T) dėsnis
                dt = k * (T - TA) # niutono temperatūros kitimo dėsnis
                T = T + z * dt # eulerio, kuno temperatūra + žingsnis * išvestinė
                print("esamos temperaturos:",T, TA)
                t += z

                temperatura.append(T)
                laikas.append(t)
                aplinkosTemperatura.append(TA)
        else:
            k = -0.01 - 0.16*((T-273)/100) - 0.04*((T-273)/100)**2 # k(T) dėsnis
            dt = k * (T - TA) # niutono temperatūros kitimo dėsnis
            T = T + z * dt # eulerio, kuno temperatūra + žingsnis * išvestinė
            print("esamos temperaturos:",T, TA)
            t += z

            temperatura.append(T)
            laikas.append(t)
            aplinkosTemperatura.append(TA)

    def model(T, t):

        global reachedModel
        TA = TA1 if not reachedModel else TA2
        if t > ts:
            if not reachedModel:
                TA = TA1 + ((TA2 - TA1) / 2) * (1 - np.cos(((math.pi) / 20) * (t - ts)))
                if TA>TA2:
                    TA=TA2
                    reachedModel = True
        k = -0.01 - 0.16 * ((T - 273) / 100) - 0.04 * ((T - 273) / 100) ** 2
        dt = k * (T - TA)
        return dt


    x = np.arange(0, tmax, 1)
    plt.plot(laikas, temperatura, label = "kūno temperatūra")
    plt.plot(laikas, aplinkosTemperatura, label = "aplinkos temperatūra")
    plt.plot(x, odeint(model, T, x),'g',label="odeint")
    plt.title("Eulerio")
    plt.xlabel('Laikas')
    plt.ylabel('Temperatura')
    plt.grid()
    plt.legend()
    plt.show()

  
            
            

        




if __name__ == '__main__':
    reachedModel = False
    t0 = 0 #pradinis laikas
    z = 0.5  # zingsnis
    #z = 1  # zingsnis
    #z = 2  # zingsnis
    #z = 5  # zingsnis
    T1 = 400 #pradine kuno temp
    #T1 = 270 #pradine kuno temp antras variantas
    TA1 = 320 #aplinkos temp kinta nuo
    TA2 = 460 #aplinkos temp kinta iki
    tmax = 80 #galutinis laikas
    ts = 30 #kada pradeda kisti aplinkos temp



    Euler()

