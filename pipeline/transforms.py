#transforms.py 

from datetime import datetime

def parse_transaction(row):
    """Convert CSV row to dict with correct types."""
    return {
        'transaction_id': row[0],
        'customer_id': row[1],
        'amount': float(row[2]) if row[2] else 0.0,
        'transaction_date': parse_date(row[3]),
	      'transaction_type': row[4]

    }

def parse_date(date_str):
    """Convert date string to ISO format."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None
