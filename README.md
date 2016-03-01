# slack-dm-export

## Usage

 1. Insert your API key in `im.py` and change dates you want to get message history within.
 2. You can get API key from [Slack website](https://api.slack.com/web).
 3. Install Python3 [Slacker](https://pypi.python.org/pypi/slacker) module.

## Syntax
Usage: python3 im.py [-h] [-g] [-s START_DATE] [-e END_DATE]

Slack direct messages, private groups and general channel export
```
optional arguments:
  -h, --help            show this help message and exit
  -g, --groups          Export private groups (by default only #general and 
                                                direct messages exported)
  -s START_DATE, --start START_DATE
                        Start date
  -e END_DATE, --end END_DATE
                        End date
```

### Date format
Date format is YYYY.MM.DD

## Example

    python3 im.py -g --start 2015.04.26 --end 2015.05.13


