# Created by Gourav at 5/23/2021
Feature: Verify if Book is add and deleted using Library API
  # Enter feature description here
  @Library
  Scenario: Verify AddBook API functionality
    Given The Book details which need to be added to Library
    When We execute the AddBook API post method
    Then Book is successfully added
    And Status code of response should be 200

  @Library
  Scenario Outline: Verify AddBook API functionality
    Given The Book details with <isbn> and <aisle>
    When We execute the AddBook API post method
    Then Book is successfully added
      Examples:
        | isbn | aisle |
        | aaa | 000 |
        | aab | 001 |
