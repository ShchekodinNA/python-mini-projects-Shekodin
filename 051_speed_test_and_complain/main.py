from internet_recive_send import IntrntDtMnpltn


SPEED_TRIGGER_MBps = 333
VK_URL = "https://vk.com/lovit"
VK_LOGIN = "*******"
VK_PSSWRD = "*****"
SPD_TST_URL = "https://www.speedtest.net/"

chrm_dvr_pth = "F:\dev\chromedriver.exe"
class_obj = IntrntDtMnpltn(chrm_dvr_pth=chrm_dvr_pth, vk_login=VK_LOGIN,vk_url=VK_URL,vk_password=VK_PSSWRD)
spd = class_obj.get_internet_speed()
if spd < SPEED_TRIGGER_MBps:
    class_obj.send_comment_into_vk(message="test_msg")
