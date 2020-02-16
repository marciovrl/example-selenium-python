@searchItem
Feature: Search item

    Background:
        Given that it is on the homepage of Mercado Livre

    Scenario: Search for existing items in the database
        When I search for "Golf"
        Then I view items according to my search

    Scenario: Search for offers of the week
        When I select "Ofertas" option
        Then I see deals