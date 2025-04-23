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
   - When testing in air, ensure that the modems are aligned to ideally face each other for optimal communication.

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
To exit the terminal session, disconnect the modem. You can also kill the screen session by pressing `Ctrl + A` followed by `K` and confirming the action.

## Timed Transmissions
For timed transmissions, the modem will only accept transmissions scheduled up to 2 seconds in the future. Use the following command format:
```sh
$B05HelloT01234567890123
```
To schedule a transmission, get the current system time and immediately schedule the transmission programmatically. The modem will then broadcast the message when the internal 1 MHz clock reaches the specified time.

### Timestamped Delays
- For scheduled transmissions, this is the time at which the modem begins the process of preparing the packet, powering up the transmit power supply, and then starting to emit the acoustic waveforms. So this equates to **about 7ms prior** to the acoustic emission. 
- For timestamped message arrivals, this occurs when the framesynch has been detected, so **at the end of the 30ms chirp arriving**.
- Future firmware versions might revisit this and perhaps set it such  that the scheduled transmission time is when the actual acoustic emission begins.

## Acknowledgments
Special thanks to the Succorfish team for their support and documentation.