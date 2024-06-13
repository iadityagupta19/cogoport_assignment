# app/schemas.py
from pydantic import BaseModel

class CountryConfigurationBase(BaseModel):
    country_code: str
    business_name: str = None
    registration_number: str = None
    additional_details: str = None

class CountryConfigurationCreate(CountryConfigurationBase):
    pass

class CountryConfigurationUpdate(CountryConfigurationBase):
    pass

class CountryConfiguration(CountryConfigurationBase):
    class Config:
        orm_mode = True
