from flask import Flask
import logging

logger = logging.getLogger(__name__)
logging.basicConfig( level=logging.INFO)
logger.info('Spin up Server')

app = Flask(__name__)

def getV1Route(name:str)->str:
    res = "/apiV1/"+name
    logger.info(f"Create route for: {res}")
    return res 

@app.route(getV1Route("example"),methods=["GET"])
def example():
    return "Hello World"