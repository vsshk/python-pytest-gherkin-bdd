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
