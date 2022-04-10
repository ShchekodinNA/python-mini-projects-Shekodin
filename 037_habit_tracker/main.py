import datetime as dt
import ui
import work_with_pixela as wwp

PIXELA_END_POINT = "https://pixe.la/v1/users"
username = "your_pixela_logib"
token = "your_pixela_token"
headers = {
    "X-USER-TOKEN": token
}
date_now = dt.date.today().strftime("%Y%m%d")
GRAPH_ID = "progmins"

today = dt.datetime.today().strftime("%Y%m%d")
pix_obj = wwp.PixelaWork(username=username, token=token, graph_id=GRAPH_ID)

ui = ui.Ui(pixela_obj=pix_obj, YYYYmmdd=today, ititle="record_time_in_pixela")
