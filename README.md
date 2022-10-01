# Pi-Thermo
How it works?

## Stage 1 - The Pi
This is require a 4.7k ohm pull up resister between data (Yellow) and VSS (Red)
Red: 3.3V from Pi
Yellow: GPIO 4 (default pin for 1 wire, but can be changed)
Black: GND from PI

The pi uses 1-wire interface to communicate with a ds18b20 thermal sensor, the PI reads the temp from a file over the interface

## stage 2 - The webpage
The PI then hosts a very simple webpage using flask with the current temperature as reported by the ds18b20

## stage 3 - web scraper

a server will scrape the page as required using powershell and return the value to be processed by logicmonitor but you can use anything you'd like 
