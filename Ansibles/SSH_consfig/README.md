# Encrypt the file with password
ansible-vault encrypt Ansibles/SSH_consfig/vars/sicretpassword.yml 
# Decrypt the file with password
ansible-vault decrypt Ansibles/SSH_consfig/vars/sicretpassword.yml 
# View encrypted file 
ansible-vault view Ansibles/SSH_consfig/vars/sicretpassword.yml 
# Run playbook with encrypted file
ansible-playbook Ansibles/SSH_consfig/main.yml -K --ask-vault-password
