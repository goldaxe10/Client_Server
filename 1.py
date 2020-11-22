"""import subprocess
import standsHostName

stands = standsHostName.stands
psexec = 'C:\psexec.exe'
pslist = 'C:\pslist.exe'
run = 0
not_run = 0

for i in stands:
    try:
        status = subprocess.call([pslist, r'\\' + i, '-e', 'defrag'])
        if status == 1: # Если процесс танков не запущен, то запускает, иначе игнорит
            stand = r'\\' + i
            subprocess.call([psexec, stand, '-i', '-s', '-h', '-d', 'defrag', 'C:', '/D'])
            run += 1
        else:
            print ('process defrag ' + i + ' alredy run \n')
            not_run += 1
    except OSError:
        print('Stand ' + i + ' is not find')
        continue
print('='*50,'\n Процессов defrag запущено', str(run), 'на', str(len(stands)), 'стендах')
print('='*50,'\n Процессов defrag уже было ранее запущено', str(not_run), 'на', str(len(stands)), 'стендах')"""
import subprocess
psexec = 'D:\Github\Client_Server\PsExec64.exe'
subprocess.call(
    [psexec, '-i', '-s', '-h', '-d', 'defrag', 'C:', '/D'])