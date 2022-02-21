---
title: "Aegisub for Windows Me and 98? Never."
contributors:
- "jfs"
date: 2008-08-19T01:39:00.003+01:00
lastmod: 2008-08-19T01:51:11.303+01:00
weight: 50
tags:
- old-post
- aegisub
- windows
- windows 9x
---
You may wonder why there is no version of Aegisub that works on Windows 95, 98, 98 SE or Me, together knows as Windows 9x. The reason is part technical-practical and part ideological.

The ideological part is short and simple: All of those operating systems are outdated, no longer under support by Microsoft and in general regarded as far inferior to the Windows NT line of systems (2000, XP, Vista). We would rather see people stop using outdated technology.

The technical part mostli lies in Unicode support. All Windows NT versions are native Unicode from the kernel all the way to the user interface. Windows 9x is not. The only way to get some kind of Unicode support on Windows 9x is to use the Microsoft Layer for Unicode library, but even that only gives flaky support at best. We did try building Aegisub against MSLU (unicows.dll) once a long time ago, and failed. Then decided that it wasn't worth the trouble.

True, Aegisub's support for Unicode isn't perfect. There's problems with right-to-left/bidirectional text and probably also several other complex scripts, but it's far better than only supporting one codepage at a time.

Finally, of course, there's the question of number of potential users. In the time this blog has been up (around a month) we've had one sigle hit from a user searching for a Windows Me version. There just isn't a user base large enough to justify the amount of work it would be to create an inferior version.
