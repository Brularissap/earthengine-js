import ee
from ee_plugin import Map 

col = ee.ImageCollection("COPERNICUS/S2_SR")\
.filterBounds(Map.getCenter())\
.filterDate('2022-01-01','2022-07-05')\
.filterMetadata('CLOUD_COVERAGE_ASSESSMENT','less_than',10)\


Qnt_imagens = col.size().getInfo()
print(f'Esta coleção de imagens filtradas tem {Qnt_imagens} imagem(s) com menos de 10% de cobertura de nuvem.')

if Qnt_imagens == 1:
    col =ee.ImageCollection("COPERNICUS/S2_SR")\
    .filterBounds(Map.getCenter())\
    .filterDate('2022-01-01','2022-07-05')\
    .filterMetadata('CLOUD_COVERAGE_ASSESSMENT','less_than',10)\
    .sort('CLOUD_COVERAGE_ASSESSMENT')\
    .first() 
    
    data_col = col.get('system:index').getInfo()
    nuvem_col = col.get('CLOUD_COVERAGE_ASSESSMENT').getInfo()
   
    print(f'Data da Imagem: { data_col}. Nuvem: {nuvem_col}%.')
    
    style = {'bands': ["B4","B3","B2"], 'gamma': 1.5,'max': 3000,'min': 900}
    Map.addLayer(col, style, data_col)

elif Qnt_imagens == 0:
    print('>>>\U0001F644NÃO TEM IMAGEM.')
    
else:
    col_0 = ee.ImageCollection("COPERNICUS/S2_SR")\
    .filterBounds(Map.getCenter())\
    .filterDate('2022-01-01','2022-07-05')\
    .filterMetadata('CLOUD_COVERAGE_ASSESSMENT','less_than',10)\
    .sort('CLOUD_COVERAGE_ASSESSMENT')\
    .first()
    
    data_col_0 = col_0.get('system:index').getInfo()
    nuvem_col_0 = col_0.get('CLOUD_COVERAGE_ASSESSMENT').getInfo()
    print(f'A Imagem: {data_col_0} apresenta {nuvem_col_0}% de cobertura de nuvem.')

    style = {'bands': ['B4','B3','B2'], 'gamma': 1.5,'max': 3000,'min': 900}

    Map.addLayer(col_0,style, data_col_0)
 

    
    
