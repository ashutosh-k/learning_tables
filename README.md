# Learning tables 1-12

## Prerequisite
**Any debian flavoured OS**(Ubuntu/Linux Mint/Debian)  
[Python 3](https://www.python.org/)  
[virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)

## Assumption
>Name only Alpha accepted  
>Answer only numeric accepted  
>For exit only 'N' is accepted (all other assumed 'Y')  
>Five difficulty level defined (easy1, easy2, medium1, medium2, hard) refer constants.py  
>Learning is started with *easy1* level. After correct answer level is increased and for incorrect level is decreased within bounds.  
>Confidence is calculated for each correct answer (marks associated with difficulty level, refer constants.py)

## Scaling
>Can be made multiligual by just adding corresponding msg.yml  
>Can easily be extended to 20, 30 ...any number multiplication tables by just altering constants.py  
>Difficulty level can easily be modified by just altering constants.py  
>Any two operand mathematical operation can easily be added by adding a class inheriting Question class (same as MultiplierQuestion, refer models.py)

## Enhancements
>Logging can easily be extended to broker-consumer streaming model  
>At scale question generator can easily be replaced with microservice  
>At start of test difficulty level can be memoized of derived from last user interaction, etc.

## Running Program
**Open Bash shell/terminal**
>bash install.sh

## Basic Class Diagram
![Class Diagram](https://lh3.googleusercontent.com/-RJwxLI6QVlg/YFcqnhCPkKI/AAAAAAAABi8/0zhlNVrQ4E0Ptd5H6GwoteivkB0PPY3YgCLcBGAsYHQ/s0/learning_table%2B%25281%2529.png)
