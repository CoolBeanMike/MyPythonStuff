import subprocess


def reboot_server_via_ipmi(host, username, password):
    """
    Reboots a remote server using IPMI over LAN.
    Requires `ipmitool` installed and accessible in the system PATH.
    """
    command = [
        "ipmitool",
        "-I", "lanplus",  # Use IPMI v2 (secure)
        "-H", host,  # Target host
        "-U", username,  # Username
        "-P", password,  # Password
        "chassis", "power", "reset"  # Reboot command
    ]

    try:
        print(f"Rebooting server at {host} via IPMI...")
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)

        if result.returncode == 0:
            print("✅ Reboot command sent successfully.")
            print(result.stdout)
        else:
            print("❌ Failed to send reboot command.")
            print(result.stderr)
    except FileNotFoundError:
        print("Error: `ipmitool` not found. Please install it first.")
    except subprocess.TimeoutExpired:
        print("Error: IPMI command timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with your IPMI credentials
    host = "192.168.1.50"
    username = "admin"
    password = "password"

    reboot_server_via_ipmi(host, username, password)
