# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_configuration", response_model=schemas.CountryConfiguration)
def create_configuration(country_config: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_country_configuration(db, country_config)

@app.get("/get_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_country_config = crud.get_country_configuration(db, country_code)
    if db_country_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return db_country_config

@app.post("/update_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def update_configuration(country_code: str, country_config: schemas.CountryConfigurationUpdate, db: Session = Depends(get_db)):
    updated_config = crud.update_country_configuration(db, country_code, country_config)
    if updated_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return updated_config

@app.delete("/delete_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    deleted_config = crud.delete_country_configuration(db, country_code)
    if deleted_config is None:
        raise HTTPException(status_code=404, detail="Country configuration not found")
    return deleted_config

# Create the database tables on startup
models.Base.metadata.create_all(bind=engine)
