# wimi-api

Python api to be used by other packages to fetch local external ip address.

## Usage

This package is indirectly used. Mus be installed locally first:

1. Go to the root project folder

2. Run the following command:
```
pip install .
```

Then you are ready to use in another python package. Just import it usign the followin term:
```
from wimiapi.Wimi import Wimi
```

Then, to get the ip:
```
Wimi().get_ip('ipv4')
```

Check the [what-is-my-ip](https://github.com/danilocgsilva/what-is-my-ip) project, that uses this package and just prints the ip fetched in the terminal.
