from pytest_bdd import scenarios, given, then, parsers, when

scenarios('', strict_gherkin=False)

@given("I am on Homepage")
def validate_homepage_url(init_driver):
    if init_driver.current_url == "https://moneygaming.qa.gameaccount.com":
        pass
    else:
        init_driver.get("https://moneygaming.qa.gameaccount.com")

@when(parsers.parse('I click on "Join Now!"'))
def click_on_element_join_now(init_driver):
        init_driver.find_element_by_css_selector('a[href="/sign-up.shtml"]').click()

@then(parsers.parse('I am on "sign-up" page'))
def validate_sign_up_page(init_driver):
    if init_driver.current_url == "https://moneygaming.qa.gameaccount.com/sign-up.shtml":
        pass
    else:
        raise Exception("User wasn't redirected to sign-up page")

@then(parsers.parse('I select title "Mr"'))
def select_title(init_driver):
    init_driver.find_element_by_css_selector('select[name="map(title)"]').click()
    init_driver.find_element_by_css_selector('option[value="Mr"]').click()
    init_driver.find_element_by_css_selector('select[name="map(title)"]').click()

@then(parsers.parse('I type "Joe" in "first_name" field'))
def type_first_name(init_driver):
    init_driver.find_element_by_css_selector('input[name="map(firstName)"]').send_keys('Anatolii')

@then(parsers.parse('I type "Smith" in "last_name" field'))
def type_last_name(init_driver):
    init_driver.find_element_by_css_selector('input[name="map(lastName)"]').send_keys('Strilets')

@then(parsers.parse('I click on "Accept the Terms and Conditions"'))
def click_terms(init_driver):
    init_driver.find_element_by_css_selector('input[name="map(terms)"]').click()

@when(parsers.parse('I click on "Join Now!" on sign up page'))
def click_join_now_signup(init_driver):
    init_driver.find_element_by_css_selector('input[class="promoReg green"]').click()


@then(parsers.parse('Validate "This field is required" text under DOB"'))
def validate_field_is_required(init_driver):
    assert init_driver.find_element_by_css_selector('label[for="dob"]').is_displayed()
    assert "This field is required" == init_driver.find_element_by_css_selector('label[for="dob"]').text
