import platform
import os

# Determine the hosts file path based on the operating system
if platform.system() == "Windows":
    path_to_hosts = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    path_to_hosts = r"/etc/hosts"
else:
    raise OSError("Unsupported operating system")

# List of websites to unblock
websites = ["www.facebook.com", "www.instagram.com", "www.twitter.com", 
            "www.netflix.com", "www.reddit.com", "www.tiktok.com"]

# Create a backup of the hosts file (optional but recommended)
backup_path = path_to_hosts + ".backup"
if not os.path.exists(backup_path):
    os.system(f"cp {path_to_hosts} {backup_path}" if platform.system() != "Windows" else f"copy {path_to_hosts} {backup_path}")

# Unblock the websites
with open(path_to_hosts, 'r+') as file:
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(site in line for site in websites):
            file.write(line)
    file.truncate()

print("Websites have been unblocked.")
