def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test1: str = "25"
    test2: str = "abc"
    print(f"\nInput data is '{test1}'")
    try:
        temp: int = input_temperature(test1)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print(f"\nInput data is '{test2}'")
    try:
        temp = input_temperature(test2)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
