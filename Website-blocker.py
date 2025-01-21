import platform
import os

# Determine the hosts file path based on the operating system
if platform.system() == "Windows":
    path_to_hosts = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    path_to_hosts = r"/etc/hosts"
else:
    raise OSError("Unsupported operating system")

# Redirect IP and list of websites to block
redirect = "127.0.0.1"
websites = ["www.facebook.com", "www.instagram.com", "www.twitter.com", 
            "www.netflix.com", "www.reddit.com", "www.tiktok.com"]

# Create a backup of the hosts file (optional but recommended)
backup_path = path_to_hosts + ".backup"
if not os.path.exists(backup_path):
    os.system(f"cp {path_to_hosts} {backup_path}" if platform.system() != "Windows" else f"copy {path_to_hosts} {backup_path}")

# Block the websites
with open(path_to_hosts, 'r+') as file:
    content = file.read()
    for site in websites:
        entry = f"{redirect} {site}\n"
        if entry not in content:
            file.write(entry)

print("Websites have been blocked.")
