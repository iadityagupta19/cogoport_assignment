# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_country_configuration(db: Session, country_config: schemas.CountryConfigurationCreate):
    db_country_config = models.CountryConfiguration(
        country_code=country_config.country_code,
        business_name=country_config.business_name,
        registration_number=country_config.registration_number,
        additional_details=country_config.additional_details
    )
    db.add(db_country_config)
    db.commit()
    db.refresh(db_country_config)
    return db_country_config

def get_country_configuration(db: Session, country_code: str):
    return db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()

def update_country_configuration(db: Session, country_code: str, country_config: schemas.CountryConfigurationUpdate):
    db_country_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if db_country_config:
        for key, value in country_config.dict(exclude_unset=True).items():
            setattr(db_country_config, key, value)
        db.commit()
        db.refresh(db_country_config)
    return db_country_config

def delete_country_configuration(db: Session, country_code: str):
    db_country_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if db_country_config:
        db.delete(db_country_config)
        db.commit()
    return db_country_config
