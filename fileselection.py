import configparser

def parse_config_and_export(file_path, section_name):
    """
    Parse the configuration file and generate shell export commands for a selected section.

    :param file_path: Path to the configuration file.
    :param section_name: The section to process.
    :return: List of shell export commands for the selected section.
    """
    # Create a ConfigParser instance
    config = configparser.ConfigParser()
    config.optionxform = str  # Preserve case sensitivity of keys

    # Read the config file
    config.read(file_path)

    # Check if the section exists
    if section_name not in config.sections():
        raise ValueError(f"Section '{section_name}' not found in the config file.")

    # Generate export commands for the selected section
    export_commands = []
    for key, value in config.items(section_name):
        export_commands.append(f"export {key}='{value}'")

    return export_commands

# File path to your appconfig.cfg
file_path = "appconfig.cfg"
section_name = "ABCD"  # Change this to the section you want

# Get the commands for the selected section
try:
    commands = parse_config_and_export(file_path, section_name)
    for command in commands:
        print(command)
except ValueError as e:
    print(e)



[ABCD]
MOUNT_POINT=/app,/log,/tmp
USERNAME=iaas
GREPWORD=tomcat

[DEFG]
MOUNT_POINT=/app,/log,/tmp
USERNAME=tomcat
GREPWORD=tomcat
