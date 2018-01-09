from flask import Flask, jsonify

app = Flask(__name__)

# api copy patch
import api.copy.views

# api run tcm
import api.tcm.views

# api return error
# import api.error.views

