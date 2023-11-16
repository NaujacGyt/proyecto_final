
query_insert = """
INSERT INTO {table_name}
    (cc_customer, name_customer, lastname_customer, email_customer, password_customer, register_date) 
VALUES
    ({cc_customer}, '{name_customer}', '{lastname_customer}', '{email_customer}', '{password_customer}', '{register_date}')
"""

query_val_user = """
SELECT * 
FROM {table_name} 
WHERE cc_customer = {cc_customer}
"""