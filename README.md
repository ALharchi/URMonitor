
# URMonitor: Status Monitor and Data Recorder from Universal Robots

#### Configuration:
1. Install the latest version of External Control URCap on the UR Robot. You can download it [here](https://github.com/UniversalRobots/Universal_Robots_ExternalControl_URCap "here").

2. Install the `ur_rtde` library for Python (does **not** work on IronPython):
```bash
pip install ur_rtde
```

3. Edit the script to indicate the Robot IP, File Name (It will be saved as an CSV), and Saving Frequency.

#### How to use the recorded data:

The data is a dump of the Real-Time Data Exchange directly from the Universal Robot. The Robot controller outputs are explained in the PDF attached in the repository. An online version is also available [here](https://www.universal-robots.com/articles/ur/interface-communication/real-time-data-exchange-rtde-guide/).
