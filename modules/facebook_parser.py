
# * --- Facebook Parser ---


from paths import facebook, chrome
import chrome_manager
import getpass


def open_facebook(headless=False):
    return chrome_manager.open_chrome(headless=headless, chrome_driver_path=chrome.CHROME_DRIVER_PATH, target_url=facebook.FACEBOOK_URL)

 
def facebook_authentication(driver):

    print('Enter Credentials')
    user = input('E-Mail: ')
    password = getpass.getpass('Password: ')

    email_field = driver.find_element_by_xpath(facebook.EMAIL_LOGIN_XPATH)
    password_field = driver.find_element_by_xpath(facebook.PASSWORD_XPATH)

    email_field.send_keys(user)
    password_field.send_keys(password)
    driver.find_element_by_xpath(facebook.SUBMIT_XPATH).click()