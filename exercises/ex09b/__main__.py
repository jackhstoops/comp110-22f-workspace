"""This specially named module makes the package runnable."""

from exercises.ex09b import constants
from exercises.ex09b.model import Model
from exercises.ex09b.view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED)
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()