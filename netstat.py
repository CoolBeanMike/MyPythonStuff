import paramiko

# Server connection details
hostname = "your.server.ip.or.hostname"
username = "your_username"
password = "your_password"  # or use key-based auth instead

def run_netstat():
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        print(f"Connecting to {hostname}...")
        ssh.connect(hostname, username=username, password=password)

        # Run netstat command
        stdin, stdout, stderr = ssh.exec_command("netstat -tulnp")

        # Print the command output
        print("\n--- Netstat Output ---")
        for line in stdout:
            print(line.strip())

        # Print any errors
        error = stderr.read().decode().strip()
        if error:
            print("\n--- Errors ---")
            print(error)

        ssh.close()
        print("\nConnection closed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_netstat()
