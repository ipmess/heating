# How to control your home heating

I needed a solution to control my home heating. I wanted a browser-based solution, so that everyone with a browser-capable device on my home LAN could control the heating.

This means that I need a web server running somewhere, and the web server should take commands over http and turn on/off the required equipment.

The equipment that needs to be controlled is the following:

* The _boiler_. The boiler burns fuel to warm up water to a preset temperature.
* The _Underfloor pump_. The underfloor pump pumps hot water to the water circuit running under my house's floor. When the water is warm, this will also warm up my house's floor, and in turn my house.
* The _Towel rail pump_. The towel rail is on a separate water circuit than the underfloor, so it requires a separate pump.

Each of the above equipment is connected to a separate relay that provides electrical power each of them. These relays provide 240V AC. The control voltage for those relays is also 240 V.

To solve this problem, I connected a Raspberry Pi 4 to a seeed studios [Grove - 4-Channel SPDT Relay](https://wiki.seeedstudio.com/Grove-4-Channel_SPDT_Relay/).

![Raspberry Pi 4, model B](./doc/RaspberryPi_4B.svg)

The physical connections are shown below:

![Physical connections](./doc/physical.svg)

The 4-channel SPDT Relay communicates over I^2^C.

![The 4-Channel SPDT Relay](./doc/4-channel-relay.jpg)

![The 4-Channel SPDT Relay - top view](./doc/4-channel-relay_front.jpg)

![The 4-Channel SPDT Relay - bottom view](./doc/pin_map_back.jpg)

I used pins 3-6 of the 40-pin GPIO of the Raspberry Pi:

![Raspberry Pi 40-pin GPIO pin diagram](./doc/GPIO-Pinout-Diagram-2.png)

# Logical structure

Once the physical connections were up and running, I had to deploy a web werver on the Raspberry Pi to expose controls for the three relays.

The logical structure is shown below:

! [Logical structure of controlling the three relays](./doc/logical.svg)

The above diagram shows the interaction of the three processes that make up this solution.

1. At first, the web browser from the user's device requests the default page from the server.
2. This request gets handled by the NGINX web server running on the Raspberry Pi.
3. When requesting the root of the web server, NGINX simply delivers three static files:

* index.html
* script.js
* styles.css

4. The static web page that NGINX serves runs some JavaScript functions whenever the page loads and whenever the user clicks on the equipment controls. Most of the time, the JavaScript functions call some REST API endpoints on the web server.
5. Once the NGINX web server receives these requests on the REST API endpoints, it forwards them to the GUnicorn WSGI.
6. Upon receiving API requests, GUnicorn runs a Python Flask application. In particular, it calls particular functions associated with the particular API calls. These Python functions communicate with the 4-Channel SPDT Relay board and close/open the relays, as required. After acting on the relays, the Python function returns the state of the relays, in JSON format.
7. The NGINX seb server relays this JSON object back to the web browser, as a reply to the original REST API call.
8. When the JavaScript function running in the web browser receives the JSON reply from the API, it updates the page's DOM with the received information.

# More information

More information at [heating.md](./doc/heating.md)

