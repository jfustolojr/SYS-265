#!/bin/bash
#secure-ssh.sh
#author joseph.fustolo
#creates a new ssh user using $l parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in

declare newuser

while getopts 'u:' flag; do
  case $flag in
    u) new_user=$OPTARG
    ;;
  esac
done

home_dir="/home/${new_user}"
ssh_dir="${home_dir}/.ssh"
auth_keys="${ssh_dir}/authorized_keys"

sudo useradd -m -d ${home_dir} -s /bin/bash ${new_user}
sudo mkdir ${ssh_dir}
sudo cp ../public-keys/id_rsa.pub ${auth_keys}
sudo chmod 700 ${home_dir}
sudo chmod 600 ${auth_keys}
sudo chown -R ${new_user}:${new_user} ${auth_keys}

sudo echo "PermitRootLogin no" >> /etc/ssh/sshd_config
sudo systemctl restart sshd.service
