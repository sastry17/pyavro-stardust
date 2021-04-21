## CAIDA-pyavro-stardust

Source for parsing FT3 and FT4 data on CAIDA UCSD Network Telescope

### References

https://stardust-dev.caida.org/data/flowtuple/
https://stardust-dev.caida.org/docs/data/flowtuple

 * flowtuple data
 * RSDOS attack data --- coming soon

### Installation

```
make install
```

or

```
USE_CYTHON=1 pip install --user .
```

### Examples 

Use the examples in the example folder for counting the records in a flowtuple file

### Analysis for IMC Paper

The flowport.py file is used to parse the FT3 files at the network telescope and get information about attack sources targeting IoT Protocols. 