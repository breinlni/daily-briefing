
# * --- Facebook Parser ---


from paths import facebook, chrome
import chrome_manager
import getpass
import pyautogui
import time


def open_facebook(headless=False):
    return chrome_manager.open_chrome(headless=headless, chrome_driver_path=chrome.CHROME_DRIVER_WINDOWS_PATH, target_url=facebook.FACEBOOK_URL)

 
def facebook_authentication(driver):

    print('Enter Credentials')
    user = input('E-Mail: ')
    password = getpass.getpass('Password: ')

    email_field = driver.find_element_by_xpath(facebook.EMAIL_LOGIN_XPATH)
    password_field = driver.find_element_by_xpath(facebook.PASSWORD_XPATH)

    email_field.send_keys(user)
    password_field.send_keys(password)

    try:
        driver.find_element_by_id('u_0_2').click()
    except:
        try:
            driver.find_element_by_xpath(facebook.SECOND_SUBMIT_XPATH).click()
        except:
            driver.find_element_by_xpath(facebook.THIRD_SUBMIT_XAPTH).click()



def get_facebook_notifications(driver):
    time.sleep(1)
    pyautogui.click(500, 500)
    time.sleep(1)
    driver.find_element_by_xpath(facebook.NOTIFICATIONS_XPATH).click()
    driver.find_element_by_xpath(facebook.ALL_NOTIFICATIONS_XPATH).click()