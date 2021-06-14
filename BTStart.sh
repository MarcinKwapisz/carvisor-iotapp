#!/bin/bash
serial=$(cat /proc/cpuinfo |grep Serial|cut -d' ' -f2)
number=${serial: -3}
hciconfig hci0 name "CarVisor$number"
hciconfig hci0 piscan