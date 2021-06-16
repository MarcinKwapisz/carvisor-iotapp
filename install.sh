sudo apt update -y
sudo apt upgrade -y
sudo apt install git python3 python3-pip bluetooth libbluetooth-dev bluez -y
git clone https://github.com/MarcinKwapisz/carvisor-iotapp.git
sudo pip3 install pyserial pint tinydb pybluez pynmea2