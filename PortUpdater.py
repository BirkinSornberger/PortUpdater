import os
 
#Replace this line with YOUR path to ProtonVPN's client logs
logFile = open("C:/Users/YourUser/AppData/Local/Proton/Proton VPN/Logs/client-logs.txt", "r")
lines = logFile.readlines()
 
portLines = [line for line in lines if "Port pair" in line]
 
latestLine = portLines[-1]
sliceValue = slice(158,163)
 
activePort = (latestLine[sliceValue])
print(activePort)
 
#Install qBitTorrent Cli & point this line to its location
#Read setup instructions for qBitTorrent CLI, as you may need to set user/pass & IP address
os.chdir("C:\\Program Files (x86)\qbittorrent-cli")
os.system("qbt server settings connection --listen-port " + activePort)
