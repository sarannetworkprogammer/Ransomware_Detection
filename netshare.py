import win32net
import win32netcon

# Define the domain name and the level of information to retrieve
domain = None
level = 101

# Call NetServerEnum
buf = win32net.NetServerEnum(domain, level, 0)

# Print the list of servers
for server in buf:
    print("Server:", server["servername"])