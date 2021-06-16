#!/bin/bash
sudo hciconfig hci0 up
serial=$(cat /proc/cpuinfo |grep Serial|cut -d' ' -f2)
number=${serial: -3}
sudo hciconfig hci0 name "CarVisor"
sudo hciconfig hci0 piscan