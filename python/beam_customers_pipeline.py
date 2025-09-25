import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv

# Define BigQuery schema
BQ_SCHEMA = {
    "fields": [
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "name", "type": "STRING"},
        {"name": "email", "type": "STRING"},
        {"name": "age", "type": "INTEGER"},
    ]
}

def parse_customer(row):
    """Parse and cleanse a CSV row into a dict"""
    try:
        values = list(csv.reader([row]))[0]
        customer_id = int(values[0]) if values[0] else None
        name = values[1].strip() if values[1] else None
        email = values[2].lower().strip() if values[2] else None
        age = int(values[3]) if values[3] and values[3].isdigit() else None

        # Basic validation
        if not all([customer_id, name, email, age]):
            return None

        return {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "age": age
        }
    except Exception:
        return None

def run():
    options = PipelineOptions(
        runner='DataflowRunner',
        project='data-engineer-task-python',
        region='europe-west2',
        temp_location='gs://customer-transactions-01/temp',
        staging_location='gs://customer-transactions-01/staging',
        job_name='customers-pipeline'
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Read CSV' >> beam.io.ReadFromText('gs://customer-transactions-01/customers.csv', skip_header_lines=1)
            | 'Parse & Cleanse' >> beam.Map(parse_customer)
            | 'Filter Valid Rows' >> beam.Filter(lambda x: x is not None)
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table='data-engineer-task-python:customer_analytics.customers',
                schema=BQ_SCHEMA,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run()