import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("your username", "riyana26")
server.sendmail(
  "from@dasarilakshmimtech@gmail.com", 
  "to@bhulakshmi.d@cmr.edu.in", 
  "this message is from python")
server.quit()