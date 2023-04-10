# Utilities
Utilities for A-Eye Unit

Connect to our server via ssh and a private ssh key

`ssh -i <private key location> <username>@128.104.121.78`

This assumes your pubic key has been added to the server and your private key is exported from putty in the proper format

To transfer files:

`pscp -i <private key location> <source> <destination>`

Example of transfer a file C:\example.txt to our remote machine for user 'ollie'

`pscp -i C:\.ssh\id_rsa.pem C:\example.txt ollie@128.104.121.78:/home/ollie/`

Example to transfer all files from a remote location to a new location:


`pscp -r -i C:\.ssh\id_rsa.pem  ollie@128.104.121.78:/home/ollie/ Q:\\files\\downloads\\`

To forward ports to the remote server (Rrequires your password)
This forwards port 8889 via ssh to the remote server

`ssh -N -f -L localhost:8889:localhost:8889 <username>@128.104.121.78` 

You can then on the remote server start a notebook on that port and use it on your laptop/terminal by going to localhost:8889
The & symbol allows the process to run in the background without tying up a terminal 

`jupyter notebook --no-browser --port=8889 &`

Current reserved ports for Jupyter Notebooks (so we don't interfere):
+ Robert: 8889
+ Mark: 8890
+ Apoorva: 8891
