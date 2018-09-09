# Python Local Bluetooth Scanner and URL Reporter
This simple python script executes a local bluetooth scan of devices from a local Bluetooth connected service. 

It's designed to pass found identification data to a URL. The URL should respond 1 (device already exists in database) or 2 (this is a new device). It will pass available data from the bluetooth device on the request. allowing the URL remote URL to capture basic information about the device. It also displays on each new device, allowing you to view locally the device information.

Update 'lookupURL' to the URL or domain you are querying.

'thissensor' is a variable you are passing on each request. This can allow you to have several sensors passing data to your listener URL.