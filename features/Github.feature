# Created by Gourav at 5/24/2021
Feature: GItHub API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have GitHub credentials
    When I hit getRepo API of GitHub
    Then Status code of response should be 200
