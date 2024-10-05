from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole

global global_positive_out
global_positive_out = list()
global global_console_status
global_console_status = False
def read_console(console_data):
    global global_console_status
    global_console_status = console_data['busy']
    print(global_console_status)
    if '[+]' in console_data['data']:
        sigdata = console_data['data'].rstrip().split('\n')
        for line in sigdata:
            if '[+]' in line:
                global_positive_out.append(line)
    print(console_data['data'])
client = MsfRpcClient('temppas', port=55553, ssl=False)
console = MsfRpcConsole(client, cb=read_console)
console.execute('use auxiliary/scanner/ftp/ftp_version')
console.execute('set RHOSTS 192.168.4.0/24')
console.execute('set THREADS 20')
console.execute('run')