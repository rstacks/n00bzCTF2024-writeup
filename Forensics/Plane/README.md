# Plane

## Description

So many plane-related challenges! Why not another one? The flag is the latitude,
longitude of the place this picture is taken from, rounded upto two decimal places.
Example: n00bz{55.51,-20.27}.

## Attachments

[plane.jpg](attachments/plane.jpg)

## Solution

- I ran <code>exiftool plane.jpg</code> to examine the metadata of the provided image. These lines
were of note:

```
GPS Latitude                    : 13 deg 22' 12.00" N
GPS Longitude                   : 13 deg 22' 12.00" W
GPS Position                    : 13 deg 22' 12.00" N, 13 deg 22' 12.00" W
```

- I used [RapidTables](https://www.rapidtables.com/convert/number/degrees-minutes-seconds-to-degrees.html)
to convert the latitude and longitude from degrees, minutes, seconds to decimal degrees. The resulting
coordinates were 13.37, -13.37.

## Flag

n00bz{13.37,-13.37}
