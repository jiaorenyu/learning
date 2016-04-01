#!/bin/bash

if [ $# -ne 2 ]; then
	echo "usage: ./create_sftp.sh user data_home"
	exit
fi

user=$1
data_home=$2
user_home=/home/$user


echo user:$user data_home:$data_home

useradd -g sftp -s /usr/sbin/nologin -m $user

mkdir $user_home/.ssh
touch $user_home/.ssh/authorized_keys
chown -R $user:sftp $user_home/.ssh
chmod 600 $user_home/.ssh/authorized_keys
chmod 700 $user_home/.ssh

mkdir -p $data_home/$user/upload
chown root:sftp $data_home/$user
chown $user:sftp $data_home/$user/upload
chmod 775 $data_home/$user/upload

echo "
Match User $user
X11Forwarding no
AllowTcpForwarding no
ForceCommand internal-sftp
ChrootDirectory $data_home/$user
" >> /etc/ssh/sshd_config

nohup service sshd restart &
