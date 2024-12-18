def parse_inventory(file_path):
    """
    Parses an inventory file in INI-like format and returns a dictionary of groups with server lists.
    
    :param file_path: Path to the inventory file.
    :return: Dictionary with group names as keys and lists of servers as values.
    """
    inventory = {}
    current_group = None

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line.startswith("[") and line.endswith("]"):
                    # New group header
                    current_group = line[1:-1]  # Extract group name without brackets
                    inventory[current_group] = []
                elif line and current_group:
                    # Add server to the current group
                    inventory[current_group].append(line)
        return inventory
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def get_group_details(inventory, group_name):
    """
    Retrieves the server details for a specified group and returns them as a comma-separated string.
    
    :param inventory: Dictionary with group names and server lists.
    :param group_name: Name of the group to retrieve details for.
    :return: Comma-separated string of server details, or a message if the group is not found.
    """
    servers = inventory.get(group_name)
    if servers:
        return ", ".join(servers)
    else:
        return f"Group '{group_name}' not found in the inventory."

# Path to the inventory file
inventory_file = "inventory.txt"

# Parse the inventory
inventory_data = parse_inventory(inventory_file)

# Specify the group name to fetch details for
group_name = "ABCD"  # Change this to test with different groups

# Get and display the group details
group_details = get_group_details(inventory_data, group_name)
print(group_details)
