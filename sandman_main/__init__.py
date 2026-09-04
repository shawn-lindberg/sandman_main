"""The main application for Sandman."""

import typing

from . import sandman


def create_app(
    test_config: dict[typing.Any, typing.Any] | None = None,
) -> sandman.Sandman:
    """Create and configure the app.

    test_config - Which testing configuration to use, if any.
    """
    sandman_app = sandman.create_app()

    if sandman_app is None:
        raise ValueError("Failed to create Sandman application.")

    return sandman_app
