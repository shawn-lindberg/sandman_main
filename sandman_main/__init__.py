"""The main application for Sandman."""

import threading
import time
import typing

import fastapi
import uvicorn

from . import sandman


def _api_thread_run(app: fastapi.FastAPI) -> None:
    """Run the API thread."""
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


def create_app(
    test_config: dict[typing.Any, typing.Any] | None = None,
) -> None:
    """Create and configure the app.

    test_config - Which testing configuration to use, if any.
    """
    # I think this should become a part of the Sandman app.
    app = fastapi.FastAPI()

    @app.get("/health")
    def get_health() -> dict[str, str]:
        return {"health": "Healthy"}

    api_thread = threading.Thread(
        target=_api_thread_run, args=[app], daemon=True
    )
    api_thread.start()

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
