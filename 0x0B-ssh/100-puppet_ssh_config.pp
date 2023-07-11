# Configures SSH client to disable accepting password for authentication and
# adds ~/.ssh/school to the  list of ssh keys to check when establishing
# connection.
exec {'modify_ssh_config':
  command  => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config;
   echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell'
}
