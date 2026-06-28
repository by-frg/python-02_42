def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int >= 0 and temp_int <= 40:
        return temp_int
    elif temp_int < 0:
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0ºC)")
    else:
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40ºC)")


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "-50", "100"]
    for x in tests:
        print(f"\nInput data is '{x}'")
        try:
            temp: int = input_temperature(x)
            print(f"Temperature is now {temp}ºC")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
