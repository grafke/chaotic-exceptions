# Chaotic Exceptions

A Python library for generating random exceptions to test system resilience and fault tolerance. Perfect for chaos engineering, testing error handling, and ensuring your applications can gracefully handle unexpected failures.

## Installation

```bash
pip install chaotic-exceptions
```

## Quick Start

### Basic Usage

```python
from chaotic_exceptions import random_exception, chaos_monkey

# Raise a random exception with 50% probability
random_exception(probability=0.5)

# Use as a decorator to add chaos to any function
@chaos_monkey(probability=0.1)
def my_function():
    return "This might fail!"

# Call the function - it has a 10% chance of raising an exception
result = my_function()
```

### Advanced Usage

```python
from chaotic_exceptions import ChaoticExceptionGenerator, NetworkChaosException, DatabaseChaosException

# Create a custom generator
chaos = ChaoticExceptionGenerator(
    exception_types=[NetworkChaosException, DatabaseChaosException],
    probability=0.2,
    seed=42  # For reproducible chaos
)

# Use in your code
def risky_operation():
    chaos.maybe_raise()  # 20% chance of network or database exception
    return "Success!"

# Force an exception for testing
try:
    chaos.force_raise()  # Always raises an exception
except Exception as e:
    print(f"Caught: {e}")

# Use as context manager
with chaos.chaos_context():
    # Code here might fail on entry or exit
    do_something()
```

## Exception Types

The library includes realistic exception types for different failure scenarios:

- **NetworkChaosException**: Simulates network failures (timeouts, connection refused, DNS issues)
- **DatabaseChaosException**: Simulates database issues (connection pool exhausted, deadlocks, constraint violations)
- **FilesystemChaosException**: Simulates file system problems (permissions, disk full, I/O errors)
- **MemoryChaosException**: Simulates memory issues (out of memory, allocation failures)
- **ConfigurationChaosException**: Simulates configuration problems (missing files, invalid format)
- **AuthenticationChaosException**: Simulates auth failures (invalid credentials, expired tokens)
- **RateLimitChaosException**: Simulates rate limiting (quota exhausted, too many requests)
- **DataCorruptionChaosException**: Simulates data integrity issues (checksum mismatches, corruption)
- **TimeoutChaosException**: Simulates various timeout scenarios
- **ResourceExhaustionChaosException**: Simulates resource limits (thread pools, connections)

## Use Cases

### Testing Error Handling

```python
from chaotic_exceptions import chaos_monkey, NetworkChaosException

@chaos_monkey(probability=0.3, exception_types=[NetworkChaosException])
def api_call():
    # Your API call logic here
    return make_http_request()

# Test that your retry logic works
for i in range(10):
    try:
        result = api_call()
        print(f"Success: {result}")
    except NetworkChaosException as e:
        print(f"Network error: {e}")
        # Your retry/fallback logic here
```

### Chaos Engineering

```python
from chaotic_exceptions import ChaoticExceptionGenerator
import threading
import time

# Create chaos in a background thread
def chaos_thread():
    chaos = ChaoticExceptionGenerator(probability=0.05)  # 5% failure rate
    while True:
        time.sleep(1)
        chaos.maybe_raise()

# Start chaos engineering
threading.Thread(target=chaos_thread, daemon=True).start()
```

### Custom Exception Messages

```python
from chaotic_exceptions import ChaoticExceptionGenerator, NetworkChaosException

custom_messages = {
    NetworkChaosException: [
        "The server is having a bad day",
        "Network gremlins are at it again",
        "Have you tried turning it off and on again?"
    ]
}

chaos = ChaoticExceptionGenerator(
    exception_types=[NetworkChaosException],
    custom_messages=custom_messages,
    probability=1.0
)

try:
    chaos.force_raise()
except NetworkChaosException as e:
    print(e)  # Will print one of your custom messages
```

## API Reference

### ChaoticExceptionGenerator

The main class for generating chaotic exceptions.

**Parameters:**
- `exception_types`: List of exception types to choose from (default: all built-in types)
- `probability`: Probability of raising an exception, 0.0 to 1.0 (default: 0.1)
- `custom_messages`: Dictionary mapping exception types to custom error messages
- `seed`: Random seed for reproducible behavior

**Methods:**
- `maybe_raise()`: Raise an exception based on probability
- `force_raise()`: Always raise a random exception
- `chaos_context()`: Return a context manager that may raise exceptions
- `chaos_decorator(func)`: Return a decorator that adds chaos to a function

### Convenience Functions

- `random_exception(**kwargs)`: Immediately raise a random exception
- `chaos_monkey(probability=0.1, **kwargs)`: Decorator to add chaos to functions

## Best Practices

1. **Start with low probabilities** (0.01-0.05) in production-like environments
2. **Use seeds for reproducible testing** when debugging specific failure scenarios
3. **Combine with proper logging** to track when chaos is injected
4. **Test your error handling** before deploying to production
5. **Use specific exception types** relevant to your system's failure modes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Changelog

### 1.0.0
- Initial release
- 10 built-in exception types with realistic error messages
- Configurable probability and custom messages
- Decorator and context manager support
- Reproducible chaos with seed support