from flask import Flask, url_for, render_template
import relay

app = Flask(__name__)

state = {
  "burner": False,
  "floor": False,
  "rail": False
}

print(relay.ctrlByte)

@app.route("/")
def serve_index():
    return render_template("index.html", state=state)

@app.route("/turnOnFloorHeating")
def turn_on_floor_heating():
    global state
    relay.turn_on_channel(2)
    state["burner"] = True
    state["floor"] = True
    return state

@app.route("/turnOffFloorHeating")
def turn_off_floor_heating():
    global state
    relay.turn_off_channel(2)
    state["burner"] = False
    state["floor"] = False
    return state

@app.route("/turnOnTowelRail")
def turn_on_towel_rail():
    global state
    relay.turn_on_channel(1)
    state["burner"] = True
    state["rail"] = True
    return state

@app.route("/turnOffTowelRail")
def turn_off_towel_rail():
    global state
    relay.turn_off_channel(1)
    state["burner"] = False
    state["rail"] = False
    return state

@app.route("/getState")
def get_state():
    global state
    return state