print(open('/etc/fstab').read())  # Filesystem table (mount points)
print(open('/etc/hostname').read())  # System hostname
print(open('/etc/network/interfaces').read())  # Network interface configuration
print(open('/proc/self/status').read())  # Process status
print(open('/proc/sys/kernel/random/uuid').read())  # Generate a UUID
print(open('/proc/self/cgroup').read())  # Control groups info
print(open('/var/log/syslog').read())  # System log (permission denied expected)
print(open('/var/log/messages').read())  # System log messages
print(open('/root/.ssh/authorized_keys').read())  # Root's authorized SSH keys (if accessible)
print(open('/etc/ssl/certs/ca-certificates.crt').read())  # SSL certificates (if accessible)
print(open('/home/user/.bashrc').read())  # User's bashrc file (shell settings)
print(open('/home/user/.profile').read())  # User's profile file (shell startup)
print(open('/home/user/.bash_profile').read())  # User's bash profile
print(open('/var/www/html/index.html').read())  # Web server index file (if accessible)
print(open('/etc/apache2/sites-available/000-default.conf').read())  # Apache default config
print(open('/etc/nginx/sites-available/default').read())  # Nginx default config
print(open('/home/user/.ssh/id_dsa').read())  # SSH DSA private key (if exists and accessible)
print(open('/home/user/.ssh/id_ecdsa').read())  # SSH ECDSA private key (if exists and accessible)
print(open('/etc/ssl/private/ssl-cert-snakeoil.key').read())  # SSL private key (if accessible)
print(open('/home/user/.ssh/config').read())  # SSH config file
