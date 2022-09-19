from core.handler import RoverHandler
from core.rover import Rover

import sys


def rover_handler(file_name):
    """
    Get instructions for each rover from input file. Create Rover object and send the instructions.
    Get the final position of Rover and print it.
    """
    data_handle = RoverHandler(input_file=file_name)

    for entry in data_handle.get_entries():
        rover = Rover(
            plateau=entry["plateau"],
            rover_name=entry["rover_name"],
            position=entry["position"],
        )
        for instruction in entry["instructions"]:
            rover.send_command(instruction)
        print(rover.get_final_position())


if __name__ == "__main__":
    file_name = sys.argv[-1]
    rover_handler(file_name)
