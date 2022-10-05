#!/bin/bash
#secure-ssh.sh
#author joseph.fustolo
#creates a new ssh user using $l parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in

user = ''

while getopts 'user' flag; do
	case "${flag}" in
		user} user="${OPTARG}" ;;
	esac
done

sudo useradd -m -d /home/$user -s /bin/bash $user
sudo mkdir /home/$user/.ssh
sudo cp ../public-keys/id_rsa.pub /home/$user/.ssh/authorized_keys
sudo chmod 700 /home/$user/.ssh
sudo chmod 600 /home/$user/.ssh/authorized_keys
sudo chown -R $user:$user /home/$user/.ssh

sudo echo "PermitRootLogin no" >> /etc/ssh/sshd_config
sudo systemctl restart sshd.service
