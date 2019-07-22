
# * --- Daily Briefing ---

from modules import facebook_parser


driver = facebook_parser.open_facebook()
facebook_parser.facebook_authentication(driver)
facebook_parser.get_facebook_notifications(driver)