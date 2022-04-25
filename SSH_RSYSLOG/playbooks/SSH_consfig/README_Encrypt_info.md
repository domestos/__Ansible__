# Encrypt the file with password
ansible-vault encrypt playbooks/SSH_consfig/vars/sicretpassword.yml 
# Decrypt the file with password
ansible-vault decrypt playbooks/SSH_consfig/vars/sicretpassword.yml 
# View encrypted file 
ansible-vault view playbooks/SSH_consfig/vars/sicretpassword.yml 
# Run playbook with encrypted file
ansible-playbook playbooks/SSH_consfig/main.yml -K --ask-vault-password
