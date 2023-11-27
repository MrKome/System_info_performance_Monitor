import psutil
import time
import pyodbc
con = pyodbc.connect('Driver={SQL Server};'
                     'Server=DESKTOP-EDVGE36\SQLEXPRESS;'
                     'Database=System_Information;'
                     'Trusted_Connection=yes;')
cursor = con.cursor()

#Create a never ending loop
while 1==1:
    cpu_usage = psutil.cpu_percent()
    memory_usgae = psutil.virtual_memory()[2] #Giving the appro index of the % value will extract % value only
    
    #Get information of cpu interupts, which are signals to the cpu for the immediate attention
    cpu_interrupts = psutil.cpu_stats()[1]
    #Get cpu calls from system
    cpu_calls = psutil.cpu_stats()[3]
    
    #Get memory used statistics from system
    memory_used = psutil.virtual_memory()[3]
    #Get memory available
    memory_free = psutil.virtual_memory()[4]
    
    #Get internet usage information. First, collect info on how many bytes are sent
    bytes_sent = psutil.net_io_counters()[0]
    #Collect info on how many bytes are received
    bytes_received = psutil.net_io_counters()[1]
    
    #Collect disk uages info
    disk_usage = psutil.disk_usage('/')[3]
    
    #Now that all the information has been gathered, we can insert this into SLQ server database
    #Use the insert SQL command to insert the data into the performance table we created in the SQL server DB
    cursor.execute('insert into Performance values (GETDATE(),'
                   + str(cpu_usage) + ','
                   + str(memory_usgae) + ','
                   + str(cpu_interrupts) + ','
                   + str(cpu_calls) + ','
                   + str(memory_used) + ','
                   + str(memory_free) + ','
                   + str(bytes_sent) + ','
                   + str(bytes_received) + ','
                   + str(disk_usage) + ')'
                   )
    
    #Use the connection.commit function to finalise the insert command and make the SQL server DB accessible 
    #for other applications
    con.commit()
    #Print cpu usage to test the code
    print(memory_usgae)
    time.sleep(1)