#==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Este arquivo python diz respeito a busca por imagens
# Sentinel 2 da coleção ee.ImageCollection("COPERNICUS/S2_SR"), presente no GEE.
# Essa busca ocorre dentro do QGIS,através do terminal python e utilizando o plugin Google Earth Engine.

# O que acontece?

# Os códigos deste arquivo irão consultar o Earth Engine em busca das imagens de acordo com o que esta sendo filtrado
# da coleção. Se encontrar alguma imagem ela será adicionada como uma camada no QGIS e poderá ser visualizada.
# Algumas condições foram impostas, uma delas é que se não houver imagem para a data solicitada e com percentual de
# cobertura de nuvem menor que 10% logo aparecerá no terminal a seguinte mensagem:
# NÃO TEM IMAGEM.
# Deste modo, basta voce alterar as datas ou o percentual de nuvem.
# E necessário centralizar bem, em um basemap, a sua área de interesse antes de rodar o arquivo no terminal.

#==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Para a maioria dos scripts EE, as importações abaixo devem ser feitas no terminal Python do QGIS.
Import ee
from ee_plugin import Map
# Deposi disso as funções .Map podem ser usadas do mesmo modo que são implementadas no editor de código do GEE.

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
 
#==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Recomendações:
# Analise o código com calma.
# Altere as datas, o percentual de cobertura de nuvem, perceba o que cada linha de código esta fazendo.
# Pratique.
#==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
