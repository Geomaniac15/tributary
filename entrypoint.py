import json
import redis
from flask import Flask, request
from loguru import logger
import statistics

HISTORY_LENGTH = 10
DATA_KEY = "engine_temperature"

# Create a Flask server
app = Flask(__name__)

def calc_temperature():
    database = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
    engine_temperature_values = database.lrange(DATA_KEY, 0, -1)
    logger.info(f"engine temperature list now contains these values: {engine_temperature_values}")

    temperatures = list(map(float, engine_temperature_values))
    average_temp = statistics.mean(temperatures)
    current_temp = engine_temperature_values[0]

    return average_temp, current_temp

# Define an endpoint which accepts POST requests, and is reachable from the /record endpoint
@app.route('/record', methods=['POST'])
def record_engine_temperature():
    payload = request.get_json(force=True)
    logger.info(f"(*) record request --- {json.dumps(payload)} (*)")

    engine_temperature = payload.get("engine_temperature")
    logger.info(f"engine temperature to record is: {engine_temperature}")

    database = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
    database.lpush(DATA_KEY, engine_temperature)
    logger.info(f"stashed engine temperature in redis: {engine_temperature}")

    while database.llen(DATA_KEY) > HISTORY_LENGTH:
        database.rpop(DATA_KEY)

    logger.info(f"record request successful :)")

    average_temp, current_temp = calc_temperature()

    logger.info(f"Current engine temperature: {current_temp}")
    logger.info(f"Average engine temperature: {average_temp}")

    return json.dumps({"average_temp": average_temp, "current_temp": current_temp})


@app.route('/collect', methods=['POST'])
def collect_engine_temperature():
    average_temp, current_temp = calc_temperature()

    return json.dumps({"average_temp": average_temp, "current_temp": current_temp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
