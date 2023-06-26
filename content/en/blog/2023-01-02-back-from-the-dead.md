---
title: Back From the Dead
contributors:
  - sepro
date: 2023-01-02T00:00:00+01:00
lastmod: 2023-01-02T00:00:00+01:00
weight: 50
---

It's been quite a while since there have been any official news regarding Aegisub. What has happened since then?

## New Website

After the [old website](https://web.archive.org/web/20201215063947/http://www.aegisub.org/) went down at the end of 2020, the decision was made to switch to a new, modern static site generator. For that, [Hugo](https://gohugo.io/) with the [doks](https://getdoks.org/) theme were chosen. The migration was initially done by inkydragon and later picked up by me.
While the new site does offer many improvements over the old one, there are still things needing work. One of which being the (sometimes very) outdated documentation. 

If you would like to help, you can report issues or make a pull request in the [aegisite repository](https://github.com/Aegisub/aegisite/). Any assistance is appreciated.


## Next Aegisub Release

With 3.2.2 being released in 2014, a new release is also long overdue. The next release won't be 3.3.0 as one might expect, but 3.4.0 to avoid confusion with the [wangqr fork](https://github.com/wangqr/Aegisub). The new version will be based off of the [meson port](/blog/porting-aegisub-to-meson/) in [TypesettingTools/Aegisub](https://github.com/TypesettingTools/Aegisub). While progress is slow, there are only a handful of things remaining until the new release can be made.
