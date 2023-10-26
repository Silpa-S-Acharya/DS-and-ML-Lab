1. 
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()

2.
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('xaxis label')
plt.ylabel('yaxis label')
plt.title('Sine and Cosine')
plt.title(

3.
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('Sine')
plt.subplot(2,1,1)
plt.title('Cosine')
plt.show()

4.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
tstimg=img.imread('Cycle3/cat.jpeg)
plt.subplot(1,2,1)
plt.imshow(tstimg)
plt.subplot(1,2,2)
plt.imshow(tstimg)   
