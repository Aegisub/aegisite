AegiSite
========

New Aegisub site. Powered by [hugo](https://gohugo.io/) and [doks](https://getdoks.org/).

## Prerequisites

- NodeJS (should be the latest LTS version). Install it from [official site](https://nodejs.org/en/) or use your package manager, such as [Homebrew](https://brew.sh/)

## Run the development server

```bash
npm ci
npm run start
```

Other [commands](https://getdoks.org/docs/prologue/commands/) for common tasks.

## Quick guide

- All contents should be in `content` folder. The `/docs/3.0` contains legacy documentation from the old Aegisub website.
- Assets (such as images) for the documentation should be put into `static` folder. For example if you have `/static/img/3.2/audio_display.png`, you can reference it later in Markdown file like this:

```
![audio_display](/img/3.2/audio_display.png)
```

+ Change **branches** in `.github\workflows\pages.yml`

## Documentation

- [Hugo](https://gohugo.io/documentation/)
- [Doks](https://getdoks.org/)
