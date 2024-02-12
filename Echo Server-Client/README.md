
# Echo Server-Client Model

This Python project implements a basic echo server and client using sockets. The code provides a simple demonstration of communication between a server and a client application.

## Overview

The project consists of two main files:

1. **echo-server.py**: This file represents the echo server. It establishes a socket connection, listens for incoming data, and echoes it back to the client.

2. **echo-client.py**: This file represents the echo client. It connects to the server, sends a predefined message, and prints the received data.

## How to Use

### Prerequisites

Make sure you have Python installed on your machine. If not, you can download it from [python.org](https://www.python.org/downloads/).

### Running the Echo Server

1. Open a terminal and navigate to the project directory.

2. Run the following command to start the echo server:

    ```bash
    python echo-server.py
    ```

   The server will start listening for incoming connections on `127.0.0.1:65432`.

### Running the Echo Client

1. Open another terminal and navigate to the project directory.

2. Run the following command to start the echo client:

    ```bash
    python echo-client.py
    ```

   The client will connect to the server, send the message "Hello, world," and display the received data.

### Understanding the Code

- The `echo-server.py` script creates a socket, binds it to the address `127.0.0.1:65432`, and listens for incoming connections. Upon connection, it receives data and echoes it back to the client.

- The `echo-client.py` script creates a socket, connects to the server at `127.0.0.1:65432`, sends the message "Hello, world," and prints the received data.

- The server script is designed to run continuously, handling multiple connections sequentially.

## Customization

- You can modify the IP address and port in both scripts to fit your networking requirements.

- Feel free to experiment with the code for educational purposes. If you have specific use cases or modifications, adapt the code accordingly.

## Known Issues

- No error handling is implemented in this basic example for simplicity. In a production environment, consider adding robust error handling mechanisms.

## Author

[Harishraj Selvakumar]

## For more info on Echo Client - Server model
[Notes](./Client-Server%20model%20notes.zip)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
