from sqlalchemy import Table, Column, String, Date, Time, Integer

from src.database import metadata

event = Table(
    'event',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('description', String),
    Column('start_time', Time),
    Column('end_time', Time),
    Column('date', Date),
    Column('author', String)
)
