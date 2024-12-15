from typing import Tuple, List, Dict
import numpy as np
import random

class Custom:
    """
    This is a class so you can design your own custom Q environment
    """

    # TODO: Make this an input or something but for now that space is of size n
    n: int = 5

    def __init__(self, *args, **kwargs):
        """
        Initialize the custom object.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        self.args = args
        self.kwargs = kwargs
        self.name = kwargs.get("name", "UnnamedComponent")
        self.metadata = kwargs.get("metadata", {})
        self.action_space = self.ActionSpace(self.n)
        self.observation_space = self.ObservationSpace(self.n)

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
        # print(f"Rendering {self.name} in {mode} mode.")
        if mode == "rgb_array":
            # Example rendering array
            return np.array([[0, 0, 0], [255, 255, 255], [0, 0, 0]])
        else:
            return np.array([[0, 0, 0], [255, 255, 255], [0, 0, 0]])
        
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

    # def close(self):
    #     """
    #     Perform cleanup tasks when the component is no longer needed.
    #     Override this method in subclasses if needed.
    #     """
    #     print(f"Closing {self.name} and releasing resources.")

    # def __str__(self):
    #     """
    #     String representation of the object.
    #     """
    #     return f"<CustomGymBase(name={self.name})>"

    # def __repr__(self):
    #     """
    #     Detailed string representation of the object.
    #     """
    #     return f"CustomGymBase(name={self.name}, metadata={self.metadata})"
