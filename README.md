# Wake Up

Wake Up is a simple Flask app that exposes an API endpoint to send a wake-on-LAN packet to a hardcoded host, and displays a webpage with a button that sends a fetch() GET request to the API endpoint.

## Installation

Clone the repository to your local machine, install the dependencies and start the server

```
  git clone https://github.com/stefnnn/wakeup
  cd wakeup
  pip install -r requirements.txt
  python server.py
```

## Configuration

You need to add the hardcoded MAC address for the server to be restarted to an .env file in the projects directory:

```
  MAC_ADDRESS=xx:xx:xx:xx:xx:xx
```

## Web Server

Open a web browser to http://localhost:5000 to see the index page with the "Wake up" button. Click the button to send a wake-on-LAN packet to the device.

## API Endpoint

The app exposes an API endpoint at /api/wake-on-lan. Sending a GET request to this endpoint will send a wake-on-LAN packet to the hardcoded host with the MAC address and IP address specified in the app.py file.

## License

This project is licensed under the MIT License. Ask ChatGPT for details.
