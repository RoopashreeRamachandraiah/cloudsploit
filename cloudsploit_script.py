import docker
import sys

# Initialize the Docker client
client = docker.from_env()

# Replace 'container_id_or_name' with your container's ID or name
container_id_or_name = sys.argv[1]

# Replace 'container_path_to_file' with the path to the file inside the container
container_path_to_file = "/output.csv"

# Replace 'local_path_to_copy_file' with the local destination path where you want to save the file
local_path_to_copy_file = "./cloud_sploit.csv"

# Use the 'copy' method to export the file from the container
try:
    with open(local_path_to_copy_file, 'wb') as local_file:
        data, stat = client.api.get_archive(container=container_id_or_name, path=container_path_to_file)
        for chunk in data:
            local_file.write(chunk)
    print(f"File '{container_path_to_file}' from container '{container_id_or_name}' has been exported to '{local_path_to_copy_file}'")
except docker.errors.NotFound:
    print(f"Container '{container_id_or_name}' not found.")
except docker.errors.APIError as e:
    print(f"Error exporting file: {e}")

# Close the Docker client
client.close()
