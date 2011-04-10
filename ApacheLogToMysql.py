import MySQLdb 
import time, datetime

class dateTime():
  def __init__(self):
    self

  def convert(self, stringDate):
    date = time.strptime(stringDate, "%d/%b/%Y:%H:%M:%S")
    return time.strftime("%Y-%m-%d %H:%M:%S", date)
    self.name = name

class ApacheLog2Mysql:
 def __init__(self):
  
  try:
	# database configuration
    con = MySQLdb.connect('<address>', '<user>', '<password>')
    con.select_db('<database name>')
    cursor = con.cursor() 

  except MySQLdbError, error:
    print(str(error), "Info")
    exit()
  # path to log files
  serverLogs = ('<log-file-1>','<log-file-2>', <...>)
  dt = dateTime()
  for log in serverLogs:
    numLog = len(open(log).readlines())
    
    
    print log, numLog
    for line in open(log, "r"):
      data = []
      a = line.split('"')
      line = line.split()
      data.append(line[0])
      dataLine = line[3][1:line[3].index(":")] + ':' + line[3][line[3].index(":") + 1:]
      data.append(dt.convert(dataLine))
      data.append(line[4][:-1]) 
      data.append(line[5][1:] + " " + line[6]) 
      data.append(line[8]) 
      data.append(line[9]) 
      data.append(line[10][1:-1]) 
      data.append(a[-2]) 

      try:
        cursor.execute("insert into logapache (ip, date, gmt, request, errorcode, bytes, referel, osa) values (%s, %s, %s, %s, %s, %s, %s, %s)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        con.commit()

      except MySQLdb.Error, error:
        print(str(error), 'Info')
        exit()

  
  cursor.close()
  con.close()

ap = ApacheLog2Mysql()