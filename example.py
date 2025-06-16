"""
Example usage of the chaotic-exceptions library.
"""

from chaotic_exceptions import (
    ChaoticExceptionGenerator, 
    chaos_monkey, 
    random_exception,
    NetworkChaosException,
    DatabaseChaosException
)
import time


def example_basic_usage():
    """Basic usage examples."""
    print("=== Basic Usage Examples ===")
    
    # Simple random exception with 100% probability
    print("1. Force a random exception:")
    try:
        random_exception(probability=1.0)
    except Exception as e:
        print(f"   Caught: {type(e).__name__}: {e}")
    
    # Random exception with 50% probability
    print("\n2. Maybe raise an exception (50% chance):")
    for i in range(5):
        try:
            random_exception(probability=0.5)
            print(f"   Attempt {i+1}: No exception raised")
        except Exception as e:
            print(f"   Attempt {i+1}: Caught {type(e).__name__}: {e}")


def example_decorator():
    """Example using the chaos_monkey decorator."""
    print("\n=== Decorator Examples ===")
    
    @chaos_monkey(probability=0.3)
    def unreliable_function():
        return "Function executed successfully!"
    
    @chaos_monkey(probability=0.5, exception_types=[NetworkChaosException])
    def network_operation():
        return "Network operation completed!"
    
    print("1. Testing unreliable function (30% failure rate):")
    for i in range(5):
        try:
            result = unreliable_function()
            print(f"   Attempt {i+1}: {result}")
        except Exception as e:
            print(f"   Attempt {i+1}: Failed with {type(e).__name__}: {e}")
    
    print("\n2. Testing network operation (50% failure rate, network errors only):")
    for i in range(5):
        try:
            result = network_operation()
            print(f"   Attempt {i+1}: {result}")
        except NetworkChaosException as e:
            print(f"   Attempt {i+1}: Network failed: {e}")


def example_generator():
    """Example using ChaoticExceptionGenerator."""
    print("\n=== Generator Examples ===")
    
    # Create a generator with specific exception types
    chaos = ChaoticExceptionGenerator(
        exception_types=[NetworkChaosException, DatabaseChaosException],
        probability=0.4,
        seed=42  # For reproducible results
    )
    
    print("1. Using generator with specific exception types:")
    for i in range(5):
        try:
            chaos.maybe_raise()
            print(f"   Operation {i+1}: Success")
        except Exception as e:
            print(f"   Operation {i+1}: Failed with {type(e).__name__}: {e}")


def example_context_manager():
    """Example using context manager."""
    print("\n=== Context Manager Examples ===")
    
    chaos = ChaoticExceptionGenerator(probability=0.3)
    
    for i in range(3):
        try:
            with chaos.chaos_context():
                print(f"   Inside context {i+1}: Doing some work...")
                time.sleep(0.1)  # Simulate work
                print(f"   Context {i+1}: Work completed")
        except Exception as e:
            print(f"   Context {i+1}: Failed with {type(e).__name__}: {e}")


def example_custom_messages():
    """Example with custom error messages."""
    print("\n=== Custom Messages Examples ===")
    
    custom_messages = {
        NetworkChaosException: [
            "The internet is broken again!",
            "Network hamsters stopped running",
            "WiFi is having an existential crisis"
        ],
        DatabaseChaosException: [
            "Database went on vacation",
            "SQL queries are feeling antisocial",
            "The database is having trust issues"
        ]
    }
    
    chaos = ChaoticExceptionGenerator(
        exception_types=[NetworkChaosException, DatabaseChaosException],
        custom_messages=custom_messages,
        probability=1.0  # Always fail for demonstration
    )
    
    print("1. Custom error messages:")
    for i in range(3):
        try:
            chaos.force_raise()
        except Exception as e:
            print(f"   Error {i+1}: {type(e).__name__}: {e}")


def example_testing_resilience():
    """Example of testing system resilience."""
    print("\n=== Testing System Resilience ===")
    
    @chaos_monkey(probability=0.2, exception_types=[NetworkChaosException])
    def api_call(data):
        """Simulate an API call that might fail."""
        return f"API response for: {data}"
    
    def resilient_api_call(data, max_retries=3):
        """A resilient version with retry logic."""
        for attempt in range(max_retries):
            try:
                return api_call(data)
            except NetworkChaosException as e:
                print(f"   Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(0.1 * (attempt + 1))  # Exponential backoff
        
    print("1. Testing resilient API calls:")
    test_data = ["user1", "user2", "user3", "user4", "user5"]
    
    for data in test_data:
        try:
            result = resilient_api_call(data)
            print(f"   Success: {result}")
        except Exception as e:
            print(f"   Final failure for {data}: {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("Chaotic Exceptions Library - Example Usage\n" + "="*50)
    
    example_basic_usage()
    example_decorator()
    example_generator()
    example_context_manager()
    example_custom_messages()
    example_testing_resilience()
    
    print("\n" + "="*50)
    print("Examples completed! Check out the different exception types and messages.")
    print("Remember: In production, use much lower probabilities (0.01-0.05)!")