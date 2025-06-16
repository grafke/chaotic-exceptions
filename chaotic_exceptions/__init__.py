"""
Chaotic Exceptions - A library for generating random exceptions to test system resilience.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .chaos import ChaoticExceptionGenerator, chaos_monkey, random_exception
from .exceptions import *

__all__ = [
    'ChaoticExceptionGenerator',
    'chaos_monkey',
    'random_exception',
    'NetworkChaosException',
    'DatabaseChaosException',
    'FilesystemChaosException',
    'MemoryChaosException',
    'ConfigurationChaosException',
    'AuthenticationChaosException',
    'RateLimitChaosException',
    'DataCorruptionChaosException',
    'TimeoutChaosException',
    'ResourceExhaustionChaosException'
]