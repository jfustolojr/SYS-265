#!/bin/bash
#secure-ssh.sh
#author joseph.fustolo
#creates a new ssh user using $l parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in
sudo useradd -m -d /home/SSHUser -s /bin/bash SSHUser
sudo mkdir /home/SSHUser/.ssh
ssh-keygen -t rsa -f "/home/SSHUser/.ssh/id_rsa" -P "" -q
cp /home/SSHUser/.ssh/id_rsa.pub .
git add -A
git commit -m "New User with SSH Key"
git push
sudo echo "PermitRootLogin no" >> /etc/ssh/sshd_config
sudo systemctl restart sshd.service
