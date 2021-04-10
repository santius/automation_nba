Feature: Positions
    Scenario Outline: Check team in first position
        Given I open the browser and navigate to the NBA page
        And I go to standings page
        Then I expect the team returned by the api call getFirstPlace to be the one in first place
        Examples:
            | call          |
            | getFirstPlace |