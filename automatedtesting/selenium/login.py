"""This function is for the testing UI."""
# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


# Start the browser and login with standard_user
def login(user, password):
    """Do the login, adding, and removing product."""
    print('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    print('Browser started successfully.\
            Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user)
    print('User Name successfully entered')
    driver.find_element(By.XPATH, "//input[@id=\
                                  'password']").send_keys(password)
    print('Password successfully entered')
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    print("I\'m " + str(user) + " able to successfully Login")

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    print('Great Work! You are on the right track\n')

    print('Now You can add the products to the cart')

    # number_of_items = [0, 1, 2, 3, 4, 5]
    add_product_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item']")
    for add_product in add_product_list:
        product_name = add_product.find_element_by_class_name('inventory_item_name').text
        add_product.find_element_by_class_name('btn_inventory').click()
        print("I'm able to add \"" + str(product_name) + "\" into the cart")

    cart_value = int(driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").text)

    if cart_value == 6:
        driver.find_element_by_class_name('shopping_cart_link').click()
        assert "https://www.saucedemo.com/cart.html" in driver.current_url
        print("Hey!! I have " + str(cart_value) + " products in my cart")
        remove_product_list = driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        for remove_product in remove_product_list:
            product_name = remove_product.find_element_by_class_name('inventory_item_name').text
            remove_product.find_element_by_class_name('cart_button').click()
            print("I'm able to remove \"" + str(product_name) + "\" from the cart")
        print('I was able to perform both adding and removing products tasks successfully')


login('standard_user', 'secret_sauce')
