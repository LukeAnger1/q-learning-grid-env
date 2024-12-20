from typing import Tuple, List, Dict
import numpy as np
import random

# This is the command to run the custom environment with the custom configuration
# python3 train.py --env Custom --config config/custom.yml

class Custom:
    """
    This is a class so you can design your own custom Q environment
    """

    def __init__(self, grid_size: int = 5, n: int = 9):
        """
        Initialize the custom object.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        self.n = n
        self.action_space = self.ActionSpace(n)
        self.observation_space = self.ObservationSpace(n)

        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)  # RGB grid
        self.position = (0, 0)  # Initial position of the red square

    def step(self, action) -> Tuple[int, float, bool, bool, dict]:
        """

        Args:
            action (_type_): _description_

        Returns new_state, reward, terminated, truncated, info
        """
        return (0, 0, False, False, None)

    def reset(self, seed = None) -> Tuple[int, dict]:
        """
        Reset the state of the object to its initial state.
        Override this method in subclasses if needed.

        returns state, info
        """
        # print(f"Resetting {self.name} to its initial state.")
        return (0, None)

    def render(self, mode="human") -> np.array:
        """
        Render the component, if applicable.

        Args:
            mode (str): The rendering mode (e.g., "human" or "rgb_array").

        Returns:
            None or an array, depending on the rendering mode.
        """

        # Create the innermost ndarray (shape: (3,), type: numpy.uint8)
        inner_most_array = np.array([255, 128, 64], dtype=np.uint8)

        # Create the middle ndarray (shape: (256, 3), type: numpy.uint8)
        middle_array = np.tile(inner_most_array, (256, 1))

        # Create the outermost ndarray (shape: (256, 256, 3), type: numpy.uint8)
        outer_array = np.tile(middle_array[:, np.newaxis, :], (1, 256, 1))


        self.grid = outer_array

        return self.grid
        
    class ObservationSpace:
        """
        Custom observation space for the environment.
        """
        def __init__(self, n: int):
            self.n: int= n

    class ActionSpace:
        """
        Custom action space for the environment.
        """
        def __init__(self, n: int):
            self.n: int = n

        def sample(self):
            """
            Sample a random action from the action space.
            """
            return random.randint(0, self.n - 1)

if __name__ == '__main__':
    # Create the innermost ndarray (shape: (3,), type: numpy.uint8)
    inner_most_array = np.array([255, 128, 64], dtype=np.uint8)

    # Create the middle ndarray (shape: (256, 3), type: numpy.ndarray)
    middle_array = np.array([inner_most_array for _ in range(256)], dtype=object)

    # Create the outermost ndarray (shape: (256, 256, 3), type: numpy.ndarray)
    outer_array = np.array([middle_array for _ in range(256)], dtype=object)

    # Print shapes and types
    print(f"Outer array shape: {outer_array.shape}, type: {type(outer_array)}")
    print(f"Middle array shape: {middle_array.shape}, type: {type(middle_array)}")
    print(f"Inner most array shape: {inner_most_array.shape}, type: {type(inner_most_array)}")
    print(f"Inner most array dtype: {type(inner_most_array[0])}")