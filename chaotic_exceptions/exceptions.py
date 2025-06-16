"""
Custom exception classes for chaotic testing.
"""


class ChaosException(Exception):
    """Base class for all chaos exceptions."""
    pass


class NetworkChaosException(ChaosException):
    """Simulates network-related failures."""
    pass


class DatabaseChaosException(ChaosException):
    """Simulates database-related failures."""
    pass


class FilesystemChaosException(ChaosException):
    """Simulates filesystem-related failures."""
    pass


class MemoryChaosException(ChaosException):
    """Simulates memory-related failures."""
    pass


class ConfigurationChaosException(ChaosException):
    """Simulates configuration-related failures."""
    pass


class AuthenticationChaosException(ChaosException):
    """Simulates authentication-related failures."""
    pass


class RateLimitChaosException(ChaosException):
    """Simulates rate limiting failures."""
    pass


class DataCorruptionChaosException(ChaosException):
    """Simulates data corruption failures."""
    pass


class TimeoutChaosException(ChaosException):
    """Simulates timeout failures."""
    pass


class ResourceExhaustionChaosException(ChaosException):
    """Simulates resource exhaustion failures."""
    pass