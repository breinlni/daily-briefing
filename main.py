
# * --- Daily Briefing ---


from modules import facebook_parser
import time


driver = facebook_parser.open_facebook()
facebook_parser.facebook_authentication(driver)
time.sleep(10)