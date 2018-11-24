# **Pi-hole data display**

**Purpose:** Provide more comprehensive search tools using django.

**Why:** The provided solution from pi-hole.net only allows date filtering 
and crashes when results return too many results. I want to be able to filter by domain, client, and also date.

**Approach:** 

1. First approach was to use a py script as a wrapper to `pihole-FTL.db`.
2. Follow-on approach is to use the django-admin interface.

- To use django-admin, I configure two databases. (See under `settings.py`)

**Basic Requirements:** 
* Python 3.7
* Django 2.1

**Installation:**
* It's intended to be run on the same server running the pihole software.
* For testing purposes, the database is copied to the local directory. If you're using the live db,
change the path in `settings.py` to the correct path. The path should be `/etc/pihole/`

**Known Defects:**

1. The `router.py` file works, but not correctly. Django should not be able to
write in the `pihole-FTL.db`, however it currently can. 
(Honestly I have no idea how `router.py` works)
2. I can not filter by date. I attempted to install `https://github.com/silentsokolov/django-admin-rangefilter`.
However, I couldn't get it to place nice with timestamps or my converted time.

