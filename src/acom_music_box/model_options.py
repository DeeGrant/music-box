from .utils import convert_time, convert_pressure, convert_temperature, convert_concentration


class BoxModelOptions:
    """
    Represents options for a box model simulation.

    Attributes:
        grid (str): The type of grid. Default is "box".
        chemStepTime (float): Time step for chemical reactions in the simulation in seconds.
        outputStepTime (float): Time step for output data in the simulation in hours.
        simulationLength (float): Length of the simulation in hours.
    """

    def __init__(
            self,
            chem_step_time=None,
            output_step_time=None,
            simulation_length=None,
            grid="box"):
        """
        Initializes a new instance of the BoxModelOptions class.

        Args:
            chem_step_time (float): Time step for chemical reactions in the simulation in seconds.
            output_step_time (float): Time step for output data in the simulation in hours.
            simulation_length (float): Length of the simulation in hours.
            grid (str): The type of grid. Default is "box".
        """
        self.chem_step_time = chem_step_time
        self.output_step_time = output_step_time
        self.simulation_length = simulation_length
        self.grid = grid

    def __repr__(self):
        return f"BoxModelOptions(chem_step_time={self.chem_step_time}, output_step_time={self.output_step_time}, simulation_length={self.simulation_length}, grid={self.grid})"

    def __str__(self):
        return f"BoxModelOptions Time step: {self.chem_step_time}, Output time step: {self.output_step_time}, Simulation length: {self.simulation_length}, Grid: {self.grid}"

    @classmethod
    def from_config(cls, config_JSON):
        """
        Create a new instance of the BoxModelOptions class from a JSON object from a configuration JSON.

        Args:
            UI_JSON (dict): A JSON object representing box model options.

        Returns:
            BoxModelOptions: A new instance of the BoxModelOptions class.
        """

        chem_step_time = convert_time(
            config_JSON['box model options'],
            'chemistry time step')
        output_step_time = convert_time(
            config_JSON['box model options'],
            'output time step')
        simulation_length = convert_time(
            config_JSON['box model options'],
            'simulation length')

        grid = config_JSON['box model options']['grid']

        return cls(chem_step_time, output_step_time, simulation_length, grid)
