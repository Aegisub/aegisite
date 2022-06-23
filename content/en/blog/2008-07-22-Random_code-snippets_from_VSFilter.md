---
title: Random code-snippets from VSFilter
contributors:
  - jfs
date: 2008-07-22T15:23:00.004000+01:00
lastmod: 2008-07-22T16:22:17.209000+01:00
weight: 50
tags:
  - old-post
  - vsfilter
  - programming
aliases:
  - /blog/2008/07/random-code-snippets-from-vsfilter.html
---

I've been reading and hacking on the VSFilter code more than is probably healthy, and have over the time found a lot of funny/strange clips of code.

For example, this line in GFN.cpp (Get File Name):

```cpp
CString filename = title + \_T(".nooneexpectsthespanishinquisition");
```

In VSFilter.cpp you can find this gem:

```cpp
/*removeme*/
JajDeGonoszVagyok();
```

Do you know the "opaque box" background style supported? As an alternative to wide outlines? Well here's how it's created:

```cpp
CStringW str;
str.Format(L"m %d %d l %d %d %d %d %d %d",
 -w, -w,
 m\_width+w, -w,
 m\_width+w, m\_ascent+m\_descent+w,
 -w, m\_ascent+m\_descent+w);

m\_pOpaqueBox = new CPolygon(style, str, 0, 0, 0, 1.0/8, 1.0/8, 0);
```

Yup, it creates a drawing object, by a string. While it is a bit clever (the alternative would be much more code) it has some bad problems which you may have seen if you've used it yourself: If for any reason it needs to create multiple boxes, such as when you have multiple lines, the boxes will overlap and a non-zero alpha will make that look really bad.

I wonder how long this line has been sitting there:

```cpp
// TODO: handle collisions == 1 (reversed collisions)
```

Maybe pre-buffering could be more useful if this was actually implemented:

```cpp
STDMETHODIMP\_(bool) CRenderedTextSubtitle::IsAnimated(POSITION pos)
{
 // TODO
 return(true);
}
```

I still find this the weirddest part... there is a CPP file with a stange name. It contains among other things this function:

```cpp
#define LEN1 (countof(str1))
#define LEN11 (countof(str1[0]))
#define LEN2 (countof(str2))
#define LEN3 (countof(str3))

static void dencode()
{
 int i, j;
 for(i = 0; i < LEN1; i++) for(j = 0; j < LEN11; j++) str1[i][j] ^= 0x12;
 for(i = 0; i < LEN2; i++) str2[i] ^= 0x34;
 for(i = 0; i < LEN3; i++) str3[i] ^= 0x56;
}
```

If you think it looks like XOR en/decryption you're right. That's exactly what it is.

It's from the file containing the `void JajDeGonoszVagyok()` function, and it's called "valami.cpp". This file also contains one other strangely named function: `bool HmGyanusVagyTeNekem(IPin* pPin)`

Both of those functions decrypt some strings written as arrays of numbers. These strings are the names of registry keys of other DirectShow filters. The *JajDeGonoszVagyok* function then detects the highest merit of all those filters and makes sure that DirectVobSub itself gets a merit higher than any of those... I think this is the DirectShow version of the "law of the jungle".
