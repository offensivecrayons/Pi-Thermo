from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
#create a website directory called "index", this is used for the template

def index():
 with open ("/sys/bus/w1/devices/28-3c01d6075678/" + "w1_slave", 'r') as rawtemp:
    temp = rawtemp.read()
    value = temp[69:75]
    rawtemp.close()
    pass
#read the temp from the probe and return the temperature with some formatting for easy processing
         return "Temp:" + value
#show the value on the webpage        

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port = 80)

#host the webpage on the localhost on port 80
