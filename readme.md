#RedAmp Assignment to evaluate Python developer skills upon

###Your task is to implement a command line application that will process and store malicious [IOCs] from all specified data sources on the Internet into a database.
• Technical requirements (bold text) and recommendations:
– Programming language: Python 3 (ideally in Python 3.6 or higher).
– Database: any relational database (ideally PostgreSQL).
– Some unit and integration tests are nice to have, but not required.
• Database schema is not strictly defined, but:
– There must be a separate table for storing IP addresses and another
table for storing URLs.
Let’s consider http://178.62.47.209/banks/ATB/last.html to be URL
and not IP address.
– One line in a given data source (for example one URL) must be stored
as one row in a database table.
Consider a hypothetical use case, that each URL and IP address must
be unique and easily searchable. You cannot store the whole input from
a given data source into one database record.
– There must be a table containing origin of a given data.
For example, if URL http://domain.com was extracted from Open-
Phish, then this URL must be associated with OpenPhish somehow.
• Data sources:
– https://www.badips.com/get/list/any/2
– http://reputation.alienvault.com/reputation.data
– https://openphish.com/feed.txt

• Everything else depends on your imagination. 
Good luck, and most importantly, have fun!

[IOCs]: https://digitalguardian.com/blog/what-are-indicators-compromise
For instance, a single IOC can be one malicious URL. For more information, you may read https://digitalguardian.com/blog/what-are-indicators-compromise (archived @ https://docs.google.com/document/d/1QlBsz_8MfbG2Em6Bv2AoN-TL-WYDXTjhmhATeS5aBWM/edit?usp=sharing )
