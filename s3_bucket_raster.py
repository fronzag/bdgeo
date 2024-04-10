import boto3
import rasterio
from rasterio.io import MemoryFile
import matplotlib.pyplot as plt


#Connect to S3 
s3 = boto3.resource(
    service_name='s3',
    region_name='sa-east-1',
    aws_access_key_id='xxxxxxx',
    aws_secret_access_key='xxxxxx'
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


def download_raster_from_s3(bucket_name, key, local_filename):
    # Initialize boto3 client
    # Download raster file from S3 and save locally
    s3.download_file(bucket_name, key, local_filename)

def visualize_raster_from_s3(bucket_name, key):
    # Download raster data from S3
    raster_data = download_raster_from_s3(bucket_name, key)
    
    # Open raster data using rasterio
    with MemoryFile(raster_data) as memfile:
        with memfile.open() as dataset:
            # Read raster data
            raster_data = dataset.read()
            # Visualize raster
            plt.imshow(raster_data[0], cmap='gray')
            plt.colorbar()
            plt.title("Raster Visualization")
            plt.show()

BUCKET_NAME = 'xx'
RASTER_KEY = 'mapbiomas_sc_2022.tif'  # Inserir a chave do raster aqui

# Initialize boto3 client with credentials
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Download raster file from S3 bucket
download_raster_from_s3(BUCKET_NAME, RASTER_KEY, LOCAL_FILENAME)

# Visualize raster
visualize_raster(LOCAL_FILENAME)