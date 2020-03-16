# BBB-Voter
Automatic voter for Big Brother Brasil.

# Getting Started

## Requirements
* Python
* Microsoft Edge

## Usage
* Set the `config.json` file and run `py voter.py`.

### Configuration:
* pollURL = url where the poll is located
* targetPosition = the order of the target. For example, if one is the 2nd on the list, this attribute should be 2.
* credentials = The Globo credentials to login.
* webDriverPath = the path to the Microsoft Edge webdriver. If you want to use another browser, change line 41.
