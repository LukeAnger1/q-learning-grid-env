from typing import Tuple, List, Dict

class Custom:
    """
    This is a class so you can design your own custom Q environment
    """

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
        self.action_space = self.ActionSpace("""put n here""")
        self.observation_space = self.ObservationSpace("""put n here""")

    def step(self, action) -> Tuple[int, float, bool, bool, dict]:
        """

        Args:
            action (_type_): _description_

        Returns new_state, reward, terminated, truncated, info
        """

    def reset(self, seed = None) -> Tuple[int, dict]:
        """
        Reset the state of the object to its initial state.
        Override this method in subclasses if needed.

        returns state, info
        """
        print(f"Resetting {self.name} to its initial state.")

    def render(self, mode="human"):
        """
        Render the component, if applicable.

        Args:
            mode (str): The rendering mode (e.g., "human" or "rgb_array").

        Returns:
            None or an array, depending on the rendering mode.
        """
        print(f"Rendering {self.name} in {mode} mode.")
        if mode == "rgb_array":
            # Example rendering array
            return [[0, 0, 0], [255, 255, 255], [0, 0, 0]]
        
    class ObservationSpace:
        """
        Custom observation space for the environment.
        """
        def __init__(self, n):
            self.n = n

    class ActionSpace:
        """
        Custom action space for the environment.
        """
        def __init__(self, n):
            self.n = n

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
