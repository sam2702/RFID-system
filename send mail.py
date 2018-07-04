# your Gmail account 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("singh.santosh2702@gmail.com", "password")

# message to be sent
message = "Clash"

# sending the mail
s.sendmail("singh.santosh2702@gmail.com", "pankajsingh0305@gmail.com", message)

# terminating the session
s.quit()




##arduino=serial.Serial('COM5',9600,timeout=.1)
##data=''
##x=1
##while x:
##    data=arduino.readline()
