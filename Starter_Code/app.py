# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")

def homepage():
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"api/v1.0/tobs"
        f"api/v1.0/<start>"
        f"api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date
    
    latest_date = most_recent_date [0]
    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')
    latest_date = latest_date.date()
    latest_date

    date_year_ago = latest_date - dt.timedelta(days = 365)
    date_year_ago

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_year_ago).all()

    precipitationData = []
    for result in results:
        precipitationDict = {result.date: result.prcp}
        precipitationData.append(precipitationDict)

    return jsonify(precipitationData)


@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Station.station, Station.name).all()

    return jsonify(results)


@app.route("/api/v1.0/tobs")


if __name__ == '__main__':
    app.run(debug = True)