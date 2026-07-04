from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class WeatherRecord(Base):
    """
    SQLAlchemy table for data.
    """

    def create_database():
        """
        creates the SQLite database and table.
        """

        engine = create_engine("sqlite:///identifier.sqlite")

        Base.metadata.create_all(engine)

        return engine

    __tablename__ = "weather_records"

    # primary key
    id = Column(Integer, primary_key=True)

    # location info
    latitude = Column(Float)
    longitude = Column(Float)

    # date
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    # temp data
    avg_temperature = Column(Float)
    min_temperature = Column(Float)
    max_temperature = Column(Float)

    # wind data
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)

    # precipitation statistics
    sum_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

def create_database():
    engine = create_engine("sqlite:///identifier.sqlite")

    Base.metadata.create_all(engine)

    return engine