"""Main entry point for the Sandman application."""

import time

import sandman_main
import sandman_main.sandman

if __name__ == "__main__":
    sandman = sandman_main.sandman.create_app()

    if sandman is None:
        raise ValueError("Failed to create Sandman application.")

    sandman.start()

    try:
        while True:
            # Sleep for 10 ms.
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

    sandman.stop()
