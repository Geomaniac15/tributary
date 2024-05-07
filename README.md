# tributary
Backend for Ford's Sensor Streaming System.
It uses a Flask server, which records data in a Redis database.
It has two Endpoints:
  /record - records a new engine temp. reading to the database
  /collect - collects the most current engine temp. and calculates an average
