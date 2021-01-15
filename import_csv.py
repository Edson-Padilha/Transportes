import pandas as pd

cont=0

def imprimir():
    print('='*60)


cidades = ['AGRONOMICA','APIUNA','ARAQUARI','ASCURRA','AURORA','BALNEARIO BARRA DO SUL','BALNEARIO CAMBORIU','BALNEARIO PICARRAS','BARRA VELHA','BENEDITO NOVO','BIGUACU','BLUMENAU','BRACO DO TROMBUDO','BRUSQUE','CAMBORIU','CAMPO ALEGRE','CANELINHA','CORUPA','DOUTOR PEDRINHO','FLORIANOPOLIS','GARUVA','GASPAR','GUABIRUBA','GUARAMIRIM','IBIRAMA','ILHOTA','INDAIAL','ITAJAI','ITAPEMA','ITAPOA','ITUPORANGA','JOINVILLE','JARAGUA DO SUL','LAURENTINO','LONTRAS','MAFRA','MASSARANDUBA','NAVEGANTES','NOVA TRENTO','PALHOCA','PENHA','POMERODE','PORTO BELO','POUSO REDONDO','PRESIDENTE GETULIO','RIO DO SUL','RIO DOS CEDROS','RIO NEGRINHO','RIO NEGRO','RODEIO','SANTO AMARO DA IMPERATRIZ','SAO BENTO DO SUL','SAO FRANCISCO DO SUL','SAO JOAO BATISTA','SAO JOAO DO ITAPERIU','SAO JOSE','SCHROEDER','TAIO','TIJUCAS','TIMBO','TROMBUDO CENTRAL'] # Lista de cidades atendidas

imprimir()
print('Quantidade de cidades atendidas por Disk Tenha: ', len(cidades))
imprimir()

ped = pd.read_csv('C:\Edson\Pedidos.csv', sep = ';')# Lista de pedidos 
clientes = pd.read_csv('C:\Edson\sc.csv', sep = ';')# Lista de cliente em SC

#leitura.insert(2,"Transportadora",' ')
print(ped.head())
print(ped.shape)

imprimir()
print(clientes.head())
print(clientes.shape)
imprimir()
print('Lista de Pedidos Janeiro')
imprimir()

colunas = ped.loc[:,['Pedido', 'Cliente', 'Nome']]# Recebe a lista de pedidos com filtro de colunas
print(colunas.head())
print(colunas.shape)

imprimir()
print('Clientes de Santa Catarina')
imprimir()

print(clientes.info())
cid = clientes.iloc[:,[0, 1, 4]]# Recebe lista de clientes com filtro de colunas
print(cid.head())
print(cid.shape)


imprimir()






















