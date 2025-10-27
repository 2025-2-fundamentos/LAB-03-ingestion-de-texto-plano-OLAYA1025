"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re
import pandas as pd
"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


  """
def pregunta_01():
    
    
  def texto_a_lista_de_filas(text):
    texto_nuevo = "".join(text[4:])
    filas = texto_nuevo.split(".")

    filas = list(map(lambda x : re.sub(r"\s{3,}", " #", x).strip().split('#'), filas ))
    filas_bien = []
    for e in filas:
        
        if len(e)<2:
            filas.remove(e)
            continue
        
        e.pop(0)
        
        filas_bien.append([e[0].strip(), e[1].strip(), e[2].rstrip(" %").replace(",", "."), re.sub( r"\s{2,}"," ",''.join(e[3:]))])
    return filas_bien
        
  with open("./files/input/clusters_report.txt", "r") as file:
        text = file.readlines()
        titulo1 = re.sub(r"\s{2,}", "#", text[0]).strip().split('#')
        titulo2 = re.sub(r"\s{2,}", "#", text[1]).strip().split('#')

        encabezado = [titulo1[0], titulo1[1]+" "+titulo2[1], titulo1[2]+" "+titulo2[2], titulo1[3]]
        encabezado = list(map(lambda x: x.lower().replace(" ","_"), encabezado))

        filas = texto_a_lista_de_filas(text)
        
        df = pd.DataFrame(filas, columns=encabezado)
        df['cluster'] = df['cluster'].astype(int)
        df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
        df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)
        return df

pregunta_01()