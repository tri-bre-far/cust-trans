# test_transforms.py

from transforms import parse_transaction

def test_parse_transaction_valid():
    row = ['001', '123', '353.15', '2025-07-10','withdrawal']
    result = parse_transaction(row)
    assert result['amount'] == 353.15
    assert result['transaction_date'].isoformat() == '2025-07-10'
    assert result['transaction_type'] == 'withdrawal'

def test_parse_transaction_null_amount():
    row = ['002', '456', '', '2025-07-15','purchase']
    result = parse_transaction(row)
    assert result['amount'] == 0.0
    assert result['transaction_type'] == 'purchase'

def test_parse_transaction_bad_date():
    row = ['003', '789', '50.00', 'bad-date','purchase']
    result = parse_transaction(row)
    assert result['transaction_date'] is None
