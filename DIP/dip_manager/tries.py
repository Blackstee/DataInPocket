from datetime import datetime

datetime_object = datetime.strptime('May 25, 2019, 6:34PM', '%b %d, %Y, %I:%M%p')
print (datetime_object)