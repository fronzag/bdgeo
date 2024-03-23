import sqlalchemy
from sqlalchemy import create_engine, MetaData
import geopandas as gpd

## Connect to the Database 
conf ={
  'host':"xxx",
  'port':'xxx',
  'database':"xxxx",
  'user':"postgres",
  'password':"postgres"
}

engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{database}".format(**conf))


# Reflect the database tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Print the table names
print("Existing tables:")
for table in metadata.tables.values():
  print(table.name)

## Load shapefile as GeoDataFrame
mun_sc = gpd.read_file(r"G:\My Drive\Pessoal\agroflorsc\shps\aoi_mun.shp")

## Load shapefile to the database
mun_sc.to_postgis('municipios_agrofloresta',engine, index=True, index_label='Index')

