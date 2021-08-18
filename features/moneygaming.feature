Feature: Registration

    Scenario: Fields validation
        Given I am on Homepage
        When I click on "Join Now!"
        Then I am on "sign-up" page
        Then I select title "Mr"
        Then I type "Joe" in "first_name" field
        Then I type "Smith" in "last_name" field
        Then I click on "Accept the Terms and Conditions"
        When I click on "Join Now!" on sign up page
        Then Validate "This field is required" text under DOB"

    Scenario: Validate error when password less than 6 characters
        When I am on "sign-up" page
        Then I type 5 characters password
        When I click on "Join Now!" on sign up page
        Then Validate error "Password must be at least 6 characters long with at least one number and at least one special character"

    Scenario: Validate error when password 6 characters without number
        When I am on "sign-up" page
        Then I type 6 characters password without number
        When I click on "Join Now!" on sign up page
        Then Validate error "Password must be at least 6 characters long with at least one number and at least one special character"

    Scenario: Validate error when password 6 characters with number but no special character
        When I am on "sign-up" page
        Then I type 6 characters password with one number but no special character
        When I click on "Join Now!" on sign up page
        Then Validate error "Password must be at least 6 characters long with at least one number and at least one special character"
