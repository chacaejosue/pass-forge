"""Compatibility imports for the original CLI and educational tests."""

from backend.passforge.generator import (
    MAX_LENGTH,
    MIN_LENGTH,
    estimate_entropy,
    generate_password,
)

__all__ = ["MAX_LENGTH", "MIN_LENGTH", "estimate_entropy", "generate_password"]
