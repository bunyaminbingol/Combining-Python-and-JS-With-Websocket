# Combining Python and JS With Websocket

Hi! 
The purpose here is to communicate **JavaScript (JS)** and **Python** programming languages using **Websocket**. The images taken from the camera opened in JS are sent to Python in base64 format via Websocket, and it converts base64 in Python, places it in the model and performs the detection process. It takes the coordinates of the detected face and adds it to a dictionary structure (JSON) and sends this structure to JS over websocket. Creates a canvas next to the camera area opened in JS and draws face coordinates on that canvas from Python. This way, you can run any real-time detection model on the web using Python and JS. And you can add Websocket to your own web processes.


# How to RUN
* First you need to start **python**
> You need to run `python server.py`
* Secondly, you open **client.html** and press the start button on the web, and after you give the camera permission, it will start working on the web.

#

**Note:** You can monitor the websocket information from the console on the web