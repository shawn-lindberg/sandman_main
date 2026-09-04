"""The main application for Sandman."""

import time
import typing

from . import sandman


def create_app(
    test_config: dict[typing.Any, typing.Any] | None = None,
) -> None:
    """Create and configure the app.

    test_config - Which testing configuration to use, if any.
    """
    sandman_app = sandman.create_app()

    if sandman_app is None:
        raise ValueError("Failed to create Sandman application.")

    # I think we should be returning the app here, and starting it outside.
    sandman_app.start()

    try:
        while True:
            # Sleep for 10 ms.
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

    sandman_app.stop()

    return None
