
# price/precision

Number of decimal digits prices contain

```
mshop/price/precision = 
```

* Type: int - Positive number of digits
* Since: 2019.04

Sets the number of decimal digits price values will contain. Internally,
prices are calculated as double values with high precision but these
values will be rounded after calculation to the configured number of digits.


# price/taxflag

Configuration setting if prices are inclusive or exclusive tax

```
mshop/price/taxflag = 
```

* Type: bool - True if gross prices are used, false for net prices
* Since: 2016.02

In Aimeos, prices can be entered either completely with or without tax. The
default is that prices contains tax. You must specifiy the tax rate for each
prices to prevent wrong calculations.
