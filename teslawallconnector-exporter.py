#!/usr/bin/python3 -u

import json
import time

import requests
import sys
from prometheus_client import start_http_server, Gauge, Enum

contactor_closed = Gauge('contactor_closed', 'Indicates if contactor is closed')
vehicle_connected = Gauge('vehicle_connected', 'Indicates if vehicle is connected')
session_s = Gauge('session_s', 'Number of second the vehicle is currently being charged')
grid_v = Gauge('grid_v', 'Current voltage of grid')
grid_hz = Gauge('grid_hz', 'Current grid frequency')
vehicle_current_a = Gauge('vehicle_current_a', 'Current amps to vehicle')
currentA_a = Gauge('currentA_a', 'Current amps phase 1')
currentB_a = Gauge('currentB_a', 'Current amps phase 2')
currentC_a = Gauge('currentC_a', 'Current amps phase 3')
currentN_a = Gauge('currentN_a', 'Current amps neutral')
voltageA_v = Gauge('voltageA_v', 'Current voltage phase 1')
voltageB_v = Gauge('voltageB_v', 'Current voltage phase 2')
voltageC_v = Gauge('voltageC_v', 'Current voltage phase 3')
relay_coil_v = Gauge('relay_coil_v', 'Current voltage relay coil')
pcba_temp_c = Gauge('pcba_temp_c', 'Current temperature PCBA')
handle_temp_c = Gauge('handle_temp_c', 'Current temperature handle')
mcu_temp_c = Gauge('mcu_temp_c', 'Current temperature MCU')
uptime_s = Gauge('uptime_s', 'Uptime in seconds')
input_thermopile_uv = Gauge('input_thermopile_uv', 'Thermopile element uv')
prox_v = Gauge('prox_v', 'Prox voltage')
pilot_high_v = Gauge('pilot_high_v', 'Pilot high voltage')
pilot_low_v = Gauge('pilot_low_v', 'Pilot high voltage')
session_energy_wh = Gauge('session_energy_wh', 'Used energy of this charging session')
config_status = Gauge('config_status', 'Config status')
evse_state = Gauge('evse_state', 'Evse state')


if __name__ == '__main__':
    print("Tesla wall connector exporter v0.1\n")
    ip_address = '192.168.178.64'
    server_port = 3225
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]

    print("IP: " + ip_address)
    print("Port: " + str(server_port) + "\n")

    start_http_server(server_port)
    while True:
        response = json.loads(requests.get('http://' + ip_address + '/api/1/vitals').content.decode('UTF-8'))

        contactor_closed.set(response['contactor_closed'])
        vehicle_connected.set(response['vehicle_connected'])
        session_s.set(response['session_s'])
        grid_v.set(response['grid_v'])
        grid_hz.set(response['grid_hz'])
        vehicle_current_a.set(response['vehicle_current_a'])
        currentA_a.set(response['currentA_a'])
        currentB_a.set(response['currentB_a'])
        currentC_a.set(response['currentC_a'])
        currentN_a.set(response['currentN_a'])
        voltageA_v.set(response['voltageA_v'])
        voltageB_v.set(response['voltageB_v'])
        voltageC_v.set(response['voltageC_v'])
        relay_coil_v.set(response['relay_coil_v'])
        pcba_temp_c.set(response['pcba_temp_c'])
        handle_temp_c.set(response['handle_temp_c'])
        mcu_temp_c.set(response['mcu_temp_c'])
        uptime_s.set(response['uptime_s'])
        input_thermopile_uv.set(response['input_thermopile_uv'])
        prox_v.set(response['prox_v'])
        pilot_high_v.set(response['pilot_high_v'])
        pilot_low_v.set(response['pilot_low_v'])
        session_energy_wh.set(response['session_energy_wh'])
        config_status.set(response['config_status'])
        evse_state.set(response['evse_state'])

        time.sleep(10)

