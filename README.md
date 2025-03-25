# Succorfish Modems

This repository contains scripts and documentation for working with Succorfish Delphis modems. These modems are used for underwater communication and data transfer in marine research and underwater robotics.

## Setup

1. **Install Dependencies**:
   - Python 3.x

   You can install the required Python packages using pip:
   ```sh
   pip install -r requirements.txt
   ```

2. **Connect Modems**:
   - Connect the modems to your computer via USB.
   - Ensure the modems are aligned to ideally face each other for optimal communication.

## Usage
We use the screen command to communicate with the modems. To open a terminal session with the modem, run the following command:
```sh
sudo screen /dev/ttyUSB0 9600
```
Replace `/dev/ttyUSB0` with the path to the modem on your system. You can find the path by running the following command:
```sh
ls /dev/ttyUSB*
```
Once you're in the terminal session, you can send commands to the modem. For example, to broadcast "Hello, World!" to all modems in the network, run the following command:
```sh
$B13Hello, World!
```
To exit the terminal session, disconnect the modem. You can also press `Ctrl + A` followed by `Ctrl + \` to exit the session. (#TODO: correct this)

## Acknowledgments
Special thanks to the Succorfish team for their support and documentation.