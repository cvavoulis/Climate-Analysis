import numpy as np
import pandas as pd

import datetime as dt
import datetime
from datetime import date, timedelta

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


from flask import Flask, jsonify

app= Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation_data=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>="2016-08-23").filter(Measurement.date<="2017-08-23").all()
    precip_json=[]
    print(precipitation_data)
    for x in precipitation_data:
        prcp_dictionary={}
        prcp_dictionary["date"]=x[0]
        prcp_dictionary["prcp"]=x[1]
        precip_json.append(prcp_dictionary)
    return jsonify(precip_json)



@app.route("/api/v1.0/stations")
def stations():
    stations= session.query(Station.station).all()
    station_list = list(np.ravel(stations))
    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_data=session.query(Measurement.tobs).filter(Measurement.date>="2016-08-23").all()
    tobs_list=list(np.ravel(tobs_data))
    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start(start):  
    start_only=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    return jsonify(start_only)


@app.route("/api/v1.0/<start>/<end>")
def start_end():
    start_end=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(start_end)


if __name__ == "__main__":
    app.run(debug=True)


