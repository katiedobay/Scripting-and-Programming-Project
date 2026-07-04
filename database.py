from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

def save_weather_data(engine, weather):
    """
    save weather data to the database.
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    weather_record = WeatherRecord(
        latitude=weather.latitude,
        longitude=weather.longitude,
        month=weather.month,
        day=weather.day,
        year=weather.year,

        avg_temperature=weather.avg_temperature,
        min_temperature=weather.min_temperature,
        max_temperature=weather.max_temperature,

        avg_wind_speed=weather.avg_wind_speed,
        min_wind_speed=weather.min_wind_speed,
        max_wind_speed=weather.max_wind_speed,

        sum_precipitation=weather.sum_precipitation,
        min_precipitation=weather.min_precipitation,
        max_precipitation=weather.max_precipitation
    )

    session.add(weather_record)
    session.commit()
    session.close()