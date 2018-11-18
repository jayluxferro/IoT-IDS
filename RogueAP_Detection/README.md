## Rogue AP Detection 
The rogue AP detection algorithm considers three scenarios.
The default characteristics of the legitimate AP is stored in the sqlite db file `ids.db`. The database file has all scenarios with measured distance from 1 to 30m.

### Scenario 1
Using iwlist parser to detect rogue AP. It assumes the wlan interface used was `wlan1`
```
Usage:
python rogueDetector-0.py [distance]
```

### Scenario 2
Using beacon frame decoding with random channel hopping. Using `mon0` interface.

```
Usage
python rogueDetector-2.py [distance]
```

### Scenario 3
Using beacon frame decoding with iterative channel hopping. Using `mon0` interface.
```
Usage:
python rogueDetector-3.py [distance]
```
