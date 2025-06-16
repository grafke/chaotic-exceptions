"""
Main chaos generation functionality.
"""

import random
from typing import List, Type, Optional, Dict
from functools import wraps

from .exceptions import (
    NetworkChaosException,
    DatabaseChaosException,
    FilesystemChaosException,
    MemoryChaosException,
    ConfigurationChaosException,
    AuthenticationChaosException,
    RateLimitChaosException,
    DataCorruptionChaosException,
    TimeoutChaosException,
    ResourceExhaustionChaosException
)


class ChaoticExceptionGenerator:
    """
    A configurable generator for random exceptions to test system resilience.
    """
    
    # Default exception types with realistic error messages
    DEFAULT_EXCEPTIONS = {
        NetworkChaosException: [
            "Connection timeout after 30 seconds",
            "DNS resolution failed for host",
            "Connection refused by remote server",
            "Network unreachable",
            "SSL handshake failed",
            "HTTP 503 Service Unavailable",
            "Connection reset by peer"
        ],
        DatabaseChaosException: [
            "Connection pool exhausted",
            "Database lock timeout",
            "Deadlock detected and resolved",
            "Table does not exist",
            "Foreign key constraint violation",
            "Transaction rollback due to serialization failure",
            "Database connection lost"
        ],
        FilesystemChaosException: [
            "Permission denied accessing file",
            "Disk space full",
            "File not found",
            "Directory is not empty",
            "File is locked by another process",
            "I/O error reading from disk",
            "Filesystem is read-only"
        ],
        MemoryChaosException: [
            "Out of memory",
            "Memory allocation failed",
            "Stack overflow detected",
            "Heap corruption detected",
            "Memory leak threshold exceeded",
            "Virtual memory exhausted"
        ],
        ConfigurationChaosException: [
            "Configuration file not found",
            "Invalid configuration format",
            "Missing required configuration key",
            "Configuration validation failed",
            "Environment variable not set",
            "Configuration file corrupted"
        ],
        AuthenticationChaosException: [
            "Invalid credentials",
            "Authentication token expired",
            "Account locked due to failed attempts",
            "Permission denied for requested resource",
            "Multi-factor authentication required",
            "Session expired"
        ],
        RateLimitChaosException: [
            "Rate limit exceeded, try again later",
            "Too many requests in time window",
            "API quota exhausted",
            "Concurrent request limit reached",
            "Throttling applied due to high load"
        ],
        DataCorruptionChaosException: [
            "Data checksum mismatch",
            "Corrupted data detected",
            "Invalid data format",
            "Data integrity violation",
            "Incomplete data transmission",
            "Schema validation failed"
        ],
        TimeoutChaosException: [
            "Operation timed out",
            "Request timeout after 60 seconds",
            "Lock acquisition timeout",
            "Response timeout from upstream service",
            "Connection idle timeout"
        ],
        ResourceExhaustionChaosException: [
            "Thread pool exhausted",
            "Connection limit reached",
            "CPU usage threshold exceeded",
            "File descriptor limit reached",
            "Queue capacity exceeded",
            "Worker process limit reached"
        ]
    }
    
    def __init__(self, 
                 exception_types: Optional[List[Type[Exception]]] = None,
                 probability: float = 0.1,
                 custom_messages: Optional[Dict[Type[Exception], List[str]]] = None,
                 seed: Optional[int] = None):
        """
        Initialize the chaotic exception generator.
        
        Args:
            exception_types: List of exception types to randomly choose from
            probability: Probability of raising an exception (0.0 to 1.0)
            custom_messages: Custom error messages for each exception type
            seed: Random seed for reproducible chaos
        """
        if seed is not None:
            random.seed(seed)
        
        self.probability = max(0.0, min(1.0, probability))
        
        if exception_types is None:
            self.exception_types = list(self.DEFAULT_EXCEPTIONS.keys())
        else:
            self.exception_types = exception_types
        
        self.messages = custom_messages or self.DEFAULT_EXCEPTIONS
        
    def maybe_raise(self) -> None:
        """
        Maybe raise a random exception based on configured probability.
        """
        if random.random() < self.probability:
            self.force_raise()
    
    def force_raise(self) -> None:
        """
        Always raise a random exception.
        """
        exception_type = random.choice(self.exception_types)
        messages = self.messages.get(exception_type, ["Chaos exception occurred"])
        message = random.choice(messages)
        raise exception_type(message)
    
    def chaos_context(self):
        """
        Context manager that may raise exceptions on entry or exit.
        """
        return ChaosContext(self)
    
    def chaos_decorator(self, func):
        """
        Decorator that may raise exceptions before function execution.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.maybe_raise()
            return func(*args, **kwargs)
        return wrapper


class ChaosContext:
    """Context manager for chaotic exceptions."""
    
    def __init__(self, generator: ChaoticExceptionGenerator):
        self.generator = generator
    
    def __enter__(self):
        self.generator.maybe_raise()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.generator.maybe_raise()


# Convenience functions
def random_exception(exception_types: Optional[List[Type[Exception]]] = None,
                    probability: float = 1.0,
                    custom_messages: Optional[Dict[Type[Exception], List[str]]] = None,
                    seed: Optional[int] = None) -> None:
    """
    Convenience function to raise a random exception.
    
    Args:
        exception_types: List of exception types to choose from
        probability: Probability of raising an exception (0.0 to 1.0)
        custom_messages: Custom error messages for each exception type
        seed: Random seed for reproducible chaos
    """
    generator = ChaoticExceptionGenerator(
        exception_types=exception_types,
        probability=probability,
        custom_messages=custom_messages,
        seed=seed
    )
    generator.maybe_raise()


def chaos_monkey(probability: float = 0.1,
                exception_types: Optional[List[Type[Exception]]] = None,
                seed: Optional[int] = None):
    """
    Decorator to add chaos to any function.
    
    Args:
        probability: Probability of raising an exception (0.0 to 1.0)
        exception_types: List of exception types to choose from
        seed: Random seed for reproducible chaos
    
    Usage:
        @chaos_monkey(probability=0.2)
        def my_function():
            return "Hello, World!"
    """
    def decorator(func):
        generator = ChaoticExceptionGenerator(
            exception_types=exception_types,
            probability=probability,
            seed=seed
        )
        return generator.chaos_decorator(func)
    return decorator