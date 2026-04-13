from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey, Text, DateTime
from datetime import datetime

metadata = MetaData()

customers = Table("customers", metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String, unique=True),
    Column("phone", String),
    Column("address", String),
    Column("password", String)
)

accounts = Table("accounts", metadata,
    Column("account_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.customer_id")),
    Column("account_type", String),
    Column("balance", Float, default=0),
    Column("status", String, default="Active")
)

transactions = Table("transactions", metadata,
    Column("transaction_id", Integer, primary_key=True),
    Column("from_account", Integer, ForeignKey("accounts.account_id")),
    Column("to_account", Integer, ForeignKey("accounts.account_id")),
    Column("amount", Float),
    Column("date", DateTime, default=datetime.utcnow),
    Column("status", String)
)

service_requests = Table("service_requests", metadata,
    Column("request_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.customer_id")),
    Column("type", String),
    Column("description", Text),
    Column("status", String)
)

bank_staff = Table("bank_staff", metadata,
    Column("staff_id", Integer, primary_key=True),
    Column("role", String),
    Column("credentials", String)
)
