from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver")

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.maximize_window()
driver.find_element_by_id("ap_email").send_keys("shraddhask27@gmail.com")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Test@1234")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input").click()

driver.find_element_by_id("nav-logo-sprites").click()
driver.implicitly_wait(3)

#Scroll down page or navigate page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.implicitly_wait(2)

#search an item Mobile
driver.find_element_by_id('twotabsearchtextbox').send_keys("Mobiles")
driver.find_element_by_id('nav-search-submit-button').click()

#apply Filter
driver.find_element_by_xpath('//*[@id="p_36/1318505031"]/span/a/span').click()

#choose 2nd item in list
driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()

# Add to cart
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()




#print(driver.title)
time.sleep(20)
driver.quit()