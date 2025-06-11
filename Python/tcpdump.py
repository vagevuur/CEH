# maak een python programma die chat.py kan afluiteren via tcpdump 
import subprocess
def run_tcpdump(interface='lo0', port=12345):
    # Start tcpdump to capture packets on the specified interface and port
    command = ['tcpdump', '-i', interface, f'port {port}', '-w', 'chat_traffic.pcap']
    try:
        print(f"Starting tcpdump on {interface} for port {port}...")
        subprocess.run(command)
    except KeyboardInterrupt:
        print("Tcpdump stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    # Specify the interface and port to monitor
    interface = 'lo'  # Loopback interface for localhost communication
    port = 12345      # Port used by the chat program
    run_tcpdump(interface, port)
if __name__ == "__main__":
    main()
# This code runs tcpdump to capture network traffic on a specified interface and port.
# It uses the subprocess module to execute the tcpdump command.
# The captured packets are saved to a file named 'chat_traffic.pcap'.
# The program can be stopped by the user using a keyboard interrupt (Ctrl+C).
# The interface is set to 'lo' for capturing localhost communication, and the port is set to 12345, which is the default port used in the chat program.