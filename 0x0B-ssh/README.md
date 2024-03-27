# SSH

In this project, i started working with SSH as a server

## Tasks:
* **0. Use a private key**
  * [0-use_a_private_key](./0-use_a_private_key): Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
  * Only uses ssh single-character flags
  * Dosen't handle the case of private key protected by passphrase
* **1. Create an SSH key pair**
  * [1-create_ssh_key_pair](./1-create_ssh_key_pair): Bash script that creates an RSA key pair.
  * Name of the created private key is school
  * Number of bits in the created key to be created 4096
  * The created key is protected by the passphrase betty
* **2. Client configuration file**
  * [2-ssh_config]: File contains SSH client configuration
  * SSH client configuration is configured to use the private key ~/.ssh/school
  * SSH client configuration is configured to refuse to authenticate using a password
* **3. Let me in!**
  * Add a given ssh key authorized keys
* **4. Client configuration file (w/ Puppet)**
  * [100-puppet_ssh_config.pp](sudo puppet apply 100-puppet_ssh_config.pp): Sets up your client SSH configuration file so that you can connect to a server without typing a password.
  * SSH client configuration is configured to use the private key ~/.ssh/school
  * SSH client configuration is configured to refuse to authenticate using a password
