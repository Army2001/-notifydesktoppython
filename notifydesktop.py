'''Parameters:

title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification'''


from datetime import date
import time
import plyer
from plyer import notification
title="Hi dear ,   Date:{}".format(date.today())
message="Take your medicines \nRemainder From : MedPage Today\n Tblets :Dolo,paracetmol\nTake care :)"
notification.notify(title=title,
                    message=message,
                    app_icon="Graphicloads-Medical-Health-Medicine-box.ico",
                    timeout=50,
                    toast=True)
time.sleep(20)
