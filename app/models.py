# app/models.py
from sqlalchemy import Column, String
from .database import Base

class CountryConfiguration(Base):
    __tablename__ = "country_configurations"

    country_code = Column(String, primary_key=True, index=True)
    business_name = Column(String, index=True)
    registration_number = Column(String, index=True)
    additional_details = Column(String, index=True)
