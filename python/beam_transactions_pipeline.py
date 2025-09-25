import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import datetime

# Define BigQuery schema
BQ_SCHEMA = {
    "fields": [
        {"name": "transaction_id", "type": "INTEGER"},
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "transaction_date", "type": "TIMESTAMP"},
        {"name": "amount", "type": "FLOAT"},
        {"name": "transaction_type", "type": "STRING"},
    ]
}

def parse_transaction(row):
    """Parse and cleanse a CSV row into a dict"""
    try:
        values = list(csv.reader([row]))[0]
        transaction_id = int(values[0]) if values[0] else None
        customer_id = int(values[1]) if values[1] else None
        transaction_date = values[2]
        amount = float(values[3]) if values[3] else None
        transaction_type = values[4].strip().lower() if values[4] else None

        # Basic validation
        if not all([transaction_id, customer_id, transaction_date, amount, transaction_type]):
            return None

        # Convert date
        try:
            transaction_date = datetime.datetime.strptime(transaction_date, "%Y-%m-%d %H:%M:%S").isoformat()
        except ValueError:
            return None

        return {
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "transaction_date": transaction_date,
            "amount": amount,
            "transaction_type": transaction_type
        }
    except Exception:
        return None

def run():
    options = PipelineOptions(
        runner='DataflowRunner',
        project='data-engineer-task-python',
        region='europe-west1',
        temp_location='gs://customer-transactions-01/temp',
        staging_location='gs://customer-transactions-01/staging',
        job_name='transactions-pipeline'
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Read CSV' >> beam.io.ReadFromText('gs://customer-transactions-01/transactions.csv', skip_header_lines=1)
            | 'Parse & Cleanse' >> beam.Map(parse_transaction)
            | 'Filter Valid Rows' >> beam.Filter(lambda x: x is not None)
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table='data-engineer-task-python:customer_analytics.transactions',
                schema=BQ_SCHEMA,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run()