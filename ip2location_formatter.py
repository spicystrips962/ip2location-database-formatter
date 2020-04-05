from socket import inet_ntoa
from struct import pack

def long2ip(ip):
    return inet_ntoa(pack("!L", ip))

inputfile='' #ip2location database csv here
outputfile='' #file name of your choice
counter=0


f=open(outputfile,'w')

with open(inputfile,'r') as x:
	for line in x:
		z=line.strip().split(",")
		begin=int(z[0].replace('"',''))
		ending=int(z[1].replace('"',''))
		for i in range(begin, ending+1):
			ip=long2ip(i)
			f.write(ip+'\n')
			counter+=1
			if counter%10000==0:
				print('.')

f.close
print('finished.')
