from utils.socket import Abstract

smtp = Abstract()
smtp.connect('localhost',25)
print smtp.recv(4096)