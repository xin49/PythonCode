# coding: UTF-8
import pysvn, os, datetime
	
def CheckoutMyPrj():
	print 'start checkout remote repository'
	RemoteAdress = [
		'https://192.168.10.188:8443/svn/DragonflyVisionSVN/Products&Projects/DragonflyVisionAssistant/Src/Software/DF_Vision_SDK', 
		'https://192.168.10.188:8443/svn/DragonflyVisionSVN/Products&Projects/DragonflyVisionAssistant/Src/Software/DFVision_Common',
		'https://192.168.10.188:8443/svn/DragonflyVisionSVN/Products&Projects/PRINT上海宝钢菲林比对系统1504003',
		'https://192.168.10.188:8443/svn/DragonflyVisionSVN/Products&Projects/PRINT上海宝钢二片罐检测系统1505006'
	]
	LocalAdress = [
		'D:/SomeLibrary/DFvision/Src/DF_Vision_SDK',
		'D:/SomeLibrary/DFvision/Src/DFVision_Common', 
		'D:/Project/filmcomparision', 
		'D:/Project/cansurfacedetector', 
	]
	Idx = 0;
	AClient=pysvn.Client()
	for i in RemoteAdress:
		Local = LocalAdress[Idx]
		print i.decode('UTF-8')
		print Local.decode('UTF-8')
		Idx += 1
		AClient.checkout(i, Local.decode('UTF-8'))
	print 'end checkout remote repository'

def CommitWeeklyReport():
	print 'Start commit weekly report'
	SvnLog= '提交日期： ' + datetime.date.today().strftime('%Y.%m.%d') + '\n' + '提交人： 宁沪鑫\n' + '提交内容：\n' + '    提交工作周报。'
	print SvnLog.decode('UTF-8')
	AClient=pysvn.Client()
	CommitFilenames = 'D:\namewithoutspaceapp\msys32\home\ouo\document\NHXFiles\2016\工作周报 宁沪鑫.doc'
#CommitFilenames = 'D:\Project\新建文件夹\工作周报 宁沪鑫.doc'
	AClient.checkin(CommitFilenames.decode('UTF-8'), SvnLog.decode('UTF-8'))
	print 'End commit weekly report'

if __name__ == '__main__':
	print'pro start'
#CheckoutMyPrj()
	CommitWeeklyReport()
	os.system('pause')
	print'pro end'

'''
{'COGNEX_LICENSE_FILE': 'C:\\Windows\\System32\\license.dat', 'TMP': 'C:\\Users\
\ouo\\AppData\\Local\\Temp', 'COMPUTERNAME': 'OUO-PC', 'USERDOMAIN': 'ouo-PC', '
PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'VS9
0COMNTOOLS': 'D:\\Program Files\\Microsoft Visual Studio 9.0\\Common7\\Tools\\',
 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'PROCESSOR_IDENTIFIER'
: 'x86 Family 6 Model 58 Stepping 9, GenuineIntel', 'PROGRAMFILES': 'C:\\Program
 Files', 'PROCESSOR_REVISION': '3a09', 'SYSTEMROOT': 'C:\\Windows', 'PATH': 'D:\
\Python27\\lib\\site-packages\\gtk-2.0\\runtime\\bin;C:\\Windows\\system32;C:\\W
indows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.
0\\;C:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;D:\\Program Files
\\TortoiseSVN\\bin;D:\\Python27;D:\\Program Files\\Cognex\\VisionPro\\bin;D:\\Pr
ogram Files\\cmake-3.5.0-win32-x86\\bin;D:\\Python27\\Doc;D:\\Program Files\\Vim
\\vim74;C:\\Users\\ouo\\AppData\\Local\\GitHub\\PortableGit_cf76fc1621ac41ad4fe8
6c420ab5ff403f1808b9\\cmd;C:\\Program Files\\Microsoft SQL Server\\80\\Tools\\Bi
nn\\;D:\\Program Files\\TortoiseSVN\\bin\\;D:\\Program Files\\Subversion\\bin;C:
\\Program Files\\NVIDIA Corporation\\PhysX\\Common;D:\\Program Files\\QuickTime\
\QTSystem\\;D:\\Python27\\Scripts', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
 'LANG': 'zh_CN', 'TEMP': 'C:\\Users\\ouo\\AppData\\Local\\Temp', 'PROCESSOR_ARC
HITECTURE': 'x86', 'APR_ICONV_PATH': 'D:\\Program Files\\Subversion\\iconv', 'AL
LUSERSPROFILE': 'C:\\ProgramData', 'LOCALAPPDATA': 'C:\\Users\\ouo\\AppData\\Loc
al', 'HOMEPATH': '\\Users\\ouo', 'USERNAME': 'ouo', 'LOGONSERVER': '\\\\OUO-PC',
 'PROMPT': '$P$G', 'SESSIONNAME': 'Console', 'PROGRAMDATA': 'C:\\ProgramData', '
VPRO32_ROOT': 'D:\\Program Files\\Cognex\\VisionPro', 'PATHEXT': '.COM;.EXE;.BAT
;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'FP_NO_HOST_CHECK': 'NO', 'WINDIR': 'C
:\\Windows', 'APPDATA': 'C:\\Users\\ouo\\AppData\\Roaming', 'HOMEDRIVE': 'C:', '
SYSTEMDRIVE': 'C:', 'VPRO_ROOT': 'D:\\Program Files\\Cognex\\VisionPro', 'NUMBER
_OF_PROCESSORS': '4', 'PROCESSOR_LEVEL': '6', 'OS': 'Windows_NT', 'PUBLIC': 'C:\
\Users\\Public', 'USERPROFILE': 'C:\\Users\\ouo'}
'''
