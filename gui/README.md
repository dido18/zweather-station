# Grafana bridge to ZDM for Power Consumption Demo

Dashboard template:
4ZeroBox Power Measurement-1589795341949.json




Start the docker containers:

- `docker-compose up`
- Open the Grafana web interface [http://127.0.0.1:3000](here)
- Configure the data source 
    - Select the simpleJson plugin 
    - Set th URL http://app:5000 (TODO: add source http automatically from grafana cli or plugin conf ??)

Follow the guide 
[here](https://www.zerynth.com/blog/docs/zdm/projects/learn-how-to-connect-zerynth-device-manager-with-grafana-for-iot-data-visualization/).

NOTE: the python script `ZDMgrafana.py` is automatically updated every time is modified.