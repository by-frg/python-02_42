class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error") -> None:
        self.msg: str = msg
        super().__init__(self.msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Water Error") -> None:
        super().__init__(msg)


def catching_plant_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught Plant Error: {e}")


def catching_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught Water Error: {e}")


def catching_garden_errors() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as f:
        print(f"Caught GardenError: {f}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting Plant Error...")
    catching_plant_error()
    print("\nTesting Water Error...")
    catching_water_error()
    print("\nTesting catching all garden errors...")
    catching_garden_errors()
    print("\nAll custom error types work correctly!")
