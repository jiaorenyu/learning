#/usr/bin/python
import os
import sys
import time
from commands import getstatusoutput as cmd_exec


sftpDir="/home/data/sftp"

def generateLogLineHtml(users, day, content, filename):
	userStat = ""
	tfp = open(filename, "w")
	for user in users:
		userDir = os.path.join(sftpDir, user, "upload", day)
		user_sum = 0
		files = []
		if not os.path.exists(userDir):
			user_sum = "None"
		else:
			files = os.listdir(userDir)

		for fn in files:
			fn_path = os.path.join(userDir, fn)
			cmd = "zcat %s | wc -l" % fn_path
			status, output = cmd_exec(cmd)
			user_sum += int(output)
		userStat += " \
						<tr> \
							<td>{0}</td> \
							<td>{1}</td> \
						</tr> \n".format(user, user_sum)
		result = content % userStat
	tfp.write(result)
	tfp.close()


if __name__ == "__main__":
	htmlModel=sys.argv[1]
	day=sys.argv[2]
	fp = open(htmlModel, "r")
	htmlModelStr=fp.read()
	fp.close()

		#day = time.strftime("%Y%m%d")
	targetFn = day+".html"
	users=os.listdir(sftpDir)

	generateLogLineHtml(users, day, htmlModelStr, targetFn)
	 
