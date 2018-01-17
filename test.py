# 1. Cloud Auth -
# gcloud auth application-default login
# 2. Python g clould bigquery lib
# pip install --upgrade google-cloud-bigquery

# Run following code
from google.cloud import bigquery

client = bigquery.Client(project="your-project-id")
query_results = client.run_sync_query(" SELECT * FROM `bigquery-public-data`.`hacker_news`.`comments` LIMIT 1000 ")

# Use standard SQL syntax for queries.
# See: https://cloud.google.com/bigquery/sql-reference/
query_results.use_legacy_sql = False

query_results.run()

# Drain the query results by requesting a page at a time.
page_token = None

while True:
	rows, total_rows, page_token = query_results.fetch_data(
		max_results=10,
		page_token=page_token)

	for row in rows:
		print(row)

	if not page_token:
		break
