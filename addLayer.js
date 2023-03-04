// Determinar local de interesse.
var local = ee.Geometry.Point (-47.84367203124723,-15.783206335161422);

// Centralizar no mapa o local de interesse.
Map.centerObject(local,10);

// Importar ImageCollection.
var imageCollection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED");

// Visualizar Metadados da ImageCollection no console.
print(imageCollection);

// Filtrar a coleção de imagens.
var imageCollectionFiltrada = imageCollection.filterBounds(local)
                                             .filterDate('2022-07-21','2022-07-23') // data inicial e data final. 
                                             .filterMetadata('CLOUDY_PIXEL_PERCENTAGE','less_than',10) 
                                             .sort('CLOUDY_PIXEL_PERCENTAGE') 
                                             .first(); 

// Visualizar Metadados da imageCollectionFiltrada no console. 
// Perceba que agora não temos mais uma ImageCollection. Temos somente uma Image. 
// Aperte RUN e visualize no console ao lado.
print(imageCollectionFiltrada);  

// Criar parametros de visualização.
var imageVisParam = ({
  bands:['B4','B3','B2'], 
  min:0, 
  max:2000,
  gamma:1.7
});

// Adicionar camada no mapa.
Map.addLayer(imageCollectionFiltrada,imageVisParam,'Sentinel 2 / 2022-07-21');

//-=-=-=-==-=-=-=-=-=-==-=-=-==-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Comentários:
/*
Na linha 11 repare que após printar a ImageCollection aparece um erro no console, pois a coleção acumulou mais de 5.000 elementos
e sua execução foi abortada e é por isso que devemos filtrar a coleção de acordo com nossos interesses seja por data, local ou 
área específica. Coloque duas barras // na frente de print(imageCollection);, aperte RUN e verifique o que acontece no console.
Na linha 14 estamos filtrando a imageCollection para variável local (nossa área de interesse).
Na linha 15 determinamos a data inicial e data final. 
Na linha 16 estamos falando para o GEE que queros filtrar dentro da coleção somente as imagens que apresentam ('CLOUDY_PIXEL_PERCENTAGE','less_than',10), ou seja,
selecionando somente as que apresentam percentual de cobertura de nuvem menor que 10%.

OBS: Se em search places and datasets você buscar a ImageCollection que estamos utilizando >>> COPERNICUS/S2_SR_HARMONIZED, 
observará que 'CLOUDY_PIXEL_PERCENTAGE' faz parte dos metadados da coleção e pode ser encontrado em IMAGE PROPERTIES.

Na linha 17 a função .sort('CLOUDY_PIXEL_PERCENTAGE') colocará as imagens em ordem crescente de acordo com o percentual de nuvem.
Na linha 18 a função .first() pegará a primeira imagem com o menor percentual de nuvem.



//-=-=-=-==-=-=-=-=-=-==-=-=-==-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Recomendação:

/* Clicar na aba Inspector ao lado direito de editor de código e posteriormente clicar 
em qualquer lugar do mapa te dará as coordenadas de um determinado local.
Tente fazer isso para uma outra área de interesse. Troque as datas. Pratique.
*/
