import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

def fnk(x):   # duota funkcija 
  rez=np.sin(2*np.pi*x)+0.3*np.cos(3*np.pi*x)+x**2;
  return rez

def HaarScaling(x,j,k,a,b):   # mastelio funkcija
# vaizdavimo taskai x, lygis j, postumis k, intervalas [a,b] 
   eps=1e-9;xtld=(x-a)/(b-a);xx=np.power(2,j)*xtld-k
   h=np.power(2,j/2)*(np.sign(xx-eps)-np.sign(xx-1+eps))/2/(b-a)
   return h

def HaarWavelet(x,j,k,a,b):   # bangeles funkcija
# vaizdavimo taskai x, lygis j, postumis k, intervalas [a,b] 
   eps=1e-9;xtld=(x-a)/(b-a);xx=np.power(2,j)*xtld-k
   h=np.power(2,j/2)*(np.sign(xx-eps)+np.sign(xx-1+eps)-2*np.sign(xx-0.5))/2/(b-a)
   return h   
   
def HaarVP(coef,x,a,b): # aproksimacija lygyje n1
# koeficientai coef, vaizdavimo taskai x, intervalas [a,b] 
  n=len(coef); n1=np.log2(n);
  h=np.zeros(x.size,dtype=float);
  for i in range (n): h+=coef[i]*HaarScaling(x,n1,i,a,b)
  return h  

def HaarWVP(coef,x,a,b): # detales lygyje n1
# koeficientai coef, vaizdavimo taskai x, intervalas [a,b]
  n=len(coef); n1=np.log2(n);
  h=np.zeros(x.size,dtype=float);
  for i in range (n): h+=coef[i]*HaarWavelet(x,n1,i,a,b)
  return h    

NL=8
a=0;b=2
xxx=np.linspace(a,b,2**NL); yyy=fnk(xxx)
axlim=[yyy.min()-1,yyy.max()+1]
fig=plt.figure(100);ax1=fig.add_subplot(1,1,1);ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.grid();ax1.set_ylim(axlim)
plt.title("duotas signalas");ax1.plot(xxx,yyy,'b.')

V=np.zeros((NL+1,2**NL),dtype=float);W=np.zeros((NL+1,2**NL),dtype=float);
V[NL,:]=yyy*np.power(2,-NL/2)*(b-a)   # pradinio signalo aproksimacijos koeficientai
xxx1=np.linspace(a,b,300) # vaizdavimo taskai intervale [a,b]  

fig=plt.figure(NL);
ax1=fig.add_subplot(1,2,1);ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.grid();ax1.set_ylim(axlim)
ax1.plot(xxx1,HaarVP(V[NL,:],xxx1,a,b),'r-');plt.title("pradinis signalas, lygis "+str(NL))

for i in range(NL,0,-1):
  fig=plt.figure(i-1);
  ax1=fig.add_subplot(1,2,1);ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.grid();ax1.set_ylim(axlim);plt.title("aproksimuotas signalas, lygis "+str(i-1))
  ax2=fig.add_subplot(1,2,2);ax2.set_xlabel('x');ax2.set_ylabel('y');ax2.grid();ax2.set_ylim(axlim);plt.title("detales, lygis "+str(i-1))
  
  for j in range (2**(i-1)):   # piramidinio algoritmo zingsnis
    V[i-1,j]=(V[i,2*j]+V[i,2*j+1])/np.sqrt(2)
    W[i-1,j]=(V[i,2*j]-V[i,2*j+1])/np.sqrt(2)
    
  ax1.plot(xxx1,HaarVP(V[i-1,0:2**(i-1)],xxx1,a,b),'b-');  # aproksimacija lygyje (i-1)
  ax2.plot(xxx1,HaarWVP(W[i-1,0:2**(i-1)],xxx1,a,b),'b-'); # detales lygyje (i-1)
  
print('mastelio funkciju koeficientai '); print(V)
print('bangeliu koeficientai  '); print(W)
  