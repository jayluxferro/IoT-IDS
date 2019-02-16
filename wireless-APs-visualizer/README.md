## IoT-IDS Wireless AP monitoring System
### Instructions
1. Install sailsjs
```
sudo npm install -g sails --allow-root --unsafe-perm=true
```

2. Install npm dependencies
```
npm install --save
```

3. Install mongodb
```
sudo apt install mongodb
```

4. Start mongodb service
```
sudo service mongodb start
```

5. Run the sails web service
```
sails lift
```

6. Open a new terminal and navigate to the same working directory. Enable monitoring interface on your wireless interface card using the command
```
cd ../tools
./mm wlan0
```
where `wlan0` is the name of the wireles interface.
In the same `tools` directory run the command below to enable wireless AP capturing
```
./cap
```
Finally run the command below to parse the captured data to the Visualizer software
```
./run
```


