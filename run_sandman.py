"""Main entry point for the Sandman application."""

import time

import sandman_main

if __name__ == "__main__":
    sandman_app = sandman_main.create_app()

    sandman_app.start()

    try:
        while True:
            # Sleep for 10 ms.
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

    sandman_app.stop()
