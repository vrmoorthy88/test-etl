# 1. Cloud Auth -
# gcloud auth application-default login
# 2. Python g clould bigquery lib
# pip install --upgrade google-cloud-bigquery

# Run following code
from google.cloud import bigquery

client = bigquery.Client(project="conductive-fold-191517")
query = "SELECT 1"
dataset = client.dataset('test_dataset')

QUERY = ('SELECT 1 as name')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
