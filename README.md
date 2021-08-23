# AUTOMATIZA-O-CALCULO-NDVI-
O script percorre a pasta raiz e em cada subpasta encontra as devidas bandas para o cálculo do NDVI, calculando o índice e salvando o mesmo na sua devida pasta, esse processo visa acelerar a produção desse tipo de dado, que posteriormente vai ser analisado em softwares de SIG.


"""
from spectral import imshow, save_rgb
import tifffile as tiff
import matplotlib.pyplot as plt
import os 
import shutil

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
    
    """
