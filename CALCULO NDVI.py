#!/usr/bin/env python
# coding: utf-8

# In[3]:


from spectral import imshow, save_rgb
import tifffile as tiff
import matplotlib.pyplot as plt
import os 
import shutil


# In[4]:


dirs = os.listdir("C:/Users/breno/Desktop/SCRIPT_NDVI/")                           # Arquivo Raiz, com subpastas  

for dir in dirs:
    caminho_4 = ("C:/Users/breno/Desktop/SCRIPT_NDVI/" + dir + "/" + "B04.tif")    # Leitura de cada subpastas 
    caminho_8 = ("C:/Users/breno/Desktop/SCRIPT_NDVI/" + dir + "/" + "B08.tif")
       
    RED = tiff.imread(caminho_4)                                                   # Leitura de cada banda 
    NIR = tiff.imread(caminho_8)
    
    ndvi = ((NIR-RED)/(NIR+RED))                                                   # Calculo do NDVI
    
    save_rgb('ndvi.tif',ndvi)                                                      # Salvar arquivo ndvi.tif
    shutil.move('ndvi.tif','C:/Users/breno/Desktop/SCRIPT_NDVI/' + dir) 
    
    imshow((ndvi), cmap="RdYlGn")                                                  # Visualização do índice de vegetação
    plt.colorbar()
    


# In[ ]:


Resultado: Ndvi salvo nas devidas pastas


# ![scrpit.JPG](attachment:scrpit.JPG)
