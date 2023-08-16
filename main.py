from src.command_parser import CommandParser
from src.SpacesCraft import SpacesCraft

def main():
    start_position = (0, 0, 0)
    start_direction = "N"
    commands = input("Enter commands: ")
    
    parsed_commands = CommandParser.parse_commands(commands) 

    SpacesCraft = SpacesCraft()
    for command in parsed_commands:
        SpacesCraft.execute_command(command)
    
    final_position = SpacesCraft.get_position()
    final_direction = SpacesCraft.get_direction()
    
    print("Starting Position:", start_position)
    print("Initial Direction:", start_direction)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    main()
