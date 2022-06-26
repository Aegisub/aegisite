---
title: Porting Aegisub to Meson
contributors:
  - Ryan
date: 2021-01-10T00:00:00-05:00
lastmod: 2021-01-10T00:00:00-05:00
weight: 50
tags:
  - redvice
---

> This blog post is originaly from [Red Vice](https://redvice.org/2021/aegisub-meson-sotu/)

# State of Meson in Aegisub

Over the past couple years, there has been a continual effort to fully port Aegisub and the DependencyControl modules to Meson. At the time of this post, the port is now fully functional, with the exception of MacOS bundles (a later milestone). This post will discuss the goals, rationale, process, current state, and various reflections on Meson and software development as a whole.

To start off, I’d like to thank everyone involved in the process. Four people had a disproportionate impact and deserve particular note:

- [mia](https://github.com/mia-0), for writing the initial Meson build files for Linux
- [line0](https://github.com/line0), for helping with the Windows port and Visual Studio compatibility
- [Myaamori](https://github.com/Myaamori), for handling much of the dependency wrangling on Windows, various Linux fixes, and Visual Studio compatibility
- [myself](https://github.com/CoffeeFlux), for most everything else and project coordination

Additionally, thanks for [FichteFoll](https://github.com/FichteFoll), [Luni-4](https://github.com/Luni-4), and [torque](https://github.com/torque) for your contributions to the project.

# Goals

After Plorkyeran stopped maintaining Aegisub, a variety of people seemed interested in taking up the mantle. However, various build system-related contribution bars were quickly discovered.

For one, the project used a fully separate build system for MacOS/Linux (Autotools + Makefiles + Bash and Python scripts) from Windows (manual Visual Studio solution). Maintaining two separate build systems is extra effort and adds to the potential for bugs. Additionally, while I’m personally fine working with Autotools having spent years in the swamp, this was very clearly not true for many less experienced contributors. From the start a unified, modern build system was a major goal.

Both legacy build systems, but in particular the Windows one, relied on generated files that were either downloaded off Plork’s server, checked in to the build tree, generated on MacOS and copied over to Windows(!), or downloaded from across the internet and arranged in an specific structure inside the build tree(!!). In almost none of these cases was the method to produce this documented anywhere. This meant another goal was to avoid abusing generated files like that, generating them locally when possible and otherwise documenting their creation.

All this made updating dependencies and the build system an incredibly painful, and in some cases near impossible, task. Many of the dependencies were out of date but there was no easy way to remedy that, especially since in some cases the build relied on patched dependencies and failed to link when compiled against upstream. This led to another goal being the ability to build against upstream where possible, or again, to document exclusions properly.

One thing that was unambiguously positive about the legacy Windows build system was that it required almost no setup locally to produce an executable. If your machine had Visual Studio and the Windows SDK, you could run off the build with only a few button presses. This sadly did not extend to the installer, but nonetheless dramatically lowered the bar for smaller codebase contributions.

The final goal was to maintain this ease on Windows and partially extend it to MacOS: you should be able to just install the build tooling, run off a command, and have the build system fetch and build dependencies as necessary. This matters little on Linux, which is designed around the assumption of dynamic linking and a system package manager, but essential on Windows and MacOS, where statically linked binaries are the de-facto method of distribution.

# Why Meson

There are only a handful of build systems that were viable, given the above goals, in particularly the cross-platform unification. The main ones that come to mind are Autotools, MSBuild, CMake, Meson, SCons, Premake, and Bazel. There might be others, but these strike me as the main ones that are popular and powerful enough to be a reasonable option for this project.

Autotools and MSBuild were ruled out for not working well on certain platforms—and please don’t try to tell me that MSYS2 is ‘fine, actually,’. SCons is famously slow, Premake is a syntactically horrible extension of Lua, Bazel is vastly overcomplicated for our needs and its advantages matter little. Both CMake and Meson seem like reasonable options.

There are a few reasons why Meson is particularly appealing. It had already seen significant adoption among open source projects, and in particular multimedia and rendering technologies. This is even more true today than it was at the time, with its heavy adoption by GNOME prompting broader interest.

Meson’s concept of subprojects and wrap files works very nicely with our goal of automatic dependency management on Windows. It seemed clear that the Meson maintainers had run into similar issues in the past and were designing a system to minimize the pain associated with that.

Finally, my perception of the project was and is that it moves faster than CMake in ways that genuinely improved the software for my needs. Every release was accompanied with numerous additions that solved real problems I’d run into, and the issues and IRC seemed fairly responsive to my needs.

The biggest advantage CMake has, on the other hand, is greater adoption. It seems reasonably popular within corporations for medium-sized projects, and so it’s been pretty well tested and is less likely to have bugs in the build system itself. Note that this does _not_ necessarily extend to CMake ports for particular projects, which in my experience are just as buggy as Meson ones if not more.

One other downside of Meson is that Linux distros don’t like the Python requirement to build. They seem to figure this out for other projects though, and it doesn’t really cause _users_ or _developers_ any problems, so I decided I didn’t particularly care. As long as the build doesn’t rely on a bunch of 3rd party Python modules, which are admittedly a dependency nightmare when mixed with system package managers, this isn’t a particularly harsh requirement. Mandating Python also makes it easy to decide what language to use for any additional generator scripts.

# Process

As mentioned above, the Meson work was kicked off with a Linux-only port by mia. It saw little attention for a while, but eventually I decided to pick it up, fix some issues, and extend it to other platforms. This work included writing a feature-complete libass port, since its only existing build system was Autotools.

With help from line0, the Aegisub port eventually reached the point where it was possible, with prebuilt dependencies and some hacks, to generate an executable on all the platforms we care about. I also ported over the DependencyControl modules (ffi-experiments, SubInspector), which previously relied on Autotools + Visual Studio solution, similar to Aegisub.

After all that, both of us got fairly busy with our full-time jobs, and frankly were somewhat demotivated. The next step was automatically building core dependencies on Windows, the most arduous of which were Boost and ICU. For a while there was minimal activity, but eventually Myaamori stepped up and gave an initial shot at a port for these, as game-changing Meson features like the CMake translation module made this a much more reasonable goal.

Myaa’s work was immensely helpful and unblocked the project. We worked together to clean that PR up, merge it, and fix a variety of the remaining issues on Windows. I also fixed other issues with MacOS and Linux, added CI via Github Actions, and implemented automatic Windows installer generation.

As part of all this, numerous bugs were filed against Meson and ports for its dependencies. As it turns out, this project was large and complex enough that it proved to be a pretty decent stress test for Meson! I’ve listed the bugs below with minimal commentary, but you can [skip to the next section](#current-state) if you aren’t interested.

## Bugs

### Meson

*   [#2631](https://github.com/mesonbuild/meson/issues/2631): Boost: Broken detection when cross compiling to Windows hosts
*   [#3123](https://github.com/mesonbuild/meson/issues/3123): wxWidgets dependency does not forward the modules kwarg
*   [#4316](https://github.com/mesonbuild/meson/issues/4316): RFC: Add minimal support for autotools subproject
*   [#4877](https://github.com/mesonbuild/meson/issues/4877): ‘StaticLibrary’ object has no attribute ‘import_filename’
    *   Found as part of the harfbuzz Meson port
    *   Fixed myself with [#5997](https://github.com/mesonbuild/meson/pull/5997)
*   [#7911](https://github.com/mesonbuild/meson/issues/7911): install_headers() should also install headers into intermediate directories
*   [#7986](https://github.com/mesonbuild/meson/issues/7986): CMake subproject: “OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect”
*   [#8020](https://github.com/mesonbuild/meson/issues/8020): extract_all_objects() with custom target results in invalid paths for subproject with Visual Studio backend
*   [#8045](https://github.com/mesonbuild/meson/issues/8045): CMake translation handling macOS frameworks incorrectly
*   [#8046](https://github.com/mesonbuild/meson/issues/8046): CMake module not automatically setting build and MSVC runtime type
*   [#8047](https://github.com/mesonbuild/meson/issues/8047): Subproject links against dynamic library when building both despite -Ddefault_library=static
*   [#8132](https://github.com/mesonbuild/meson/issues/8132): CMake translation missing Objective-C++ files in wxWidgets

Special thanks to [mensinda](https://github.com/mensinda) for prompt replies to all the CMake-specific issues, as most of them were blocking!

### libass

*   [#329](https://github.com/libass/libass/pull/329): rasterizer: add CONFIG_HIGH_DPI
    *   SubInspector relies on a pached libass to remove an optimization that significantly affects the rendered boundary, and this is part of an effort to make that a build flag upstream
    *   Alternative: [#449](https://github.com/libass/libass/pull/449)
*   [#330](https://github.com/libass/libass/pull/330): Port of the build system to meson
*   [#456](https://github.com/libass/libass/pull/456): x86: update x86inc
    *   Uncovered by the Meson port, the x86inc version is old and spews warnings on newer versions of nasm

### HarfBuzz

*   [#2755](https://github.com/harfbuzz/harfbuzz/pull/2755): meson: use meson.current_source_dir() instead of @CURRENT_SOURCE_DIR@
*   [#2775](https://github.com/harfbuzz/harfbuzz/pull/2775): meson: avoid regenerating hb-version.h unnecessarily

### fribidi

*   [#100](https://github.com/fribidi/fribidi/issues/100): Meson linker errors when building statically: unresolved externals
    *   Fixed myself with [#101](https://github.com/fribidi/fribidi/pull/101) and [#102](https://github.com/fribidi/fribidi/pull/102)
*   [#109](https://github.com/fribidi/fribidi/issues/109): symbols are not included when building with optimization
    *   Issue someone else reported that did end up affecting us
    *   Fixed myself with [#110](https://github.com/fribidi/fribidi/pull/110)

### GStreamer FFMpeg port

*   [#22](https://gitlab.freedesktop.org/gstreamer/meson-ports/ffmpeg/-/issues/22): Index error in libavutil/version.py on meson-4.3 branch
    *   Fixed by Myaa with [#54](https://gitlab.freedesktop.org/gstreamer/meson-ports/ffmpeg/-/merge_requests/54)

It’s likely there are additional issues I have forgotten about; this will be updated as appropriate.

# Current state

The DependencyControl modules have all been switched over to Meson as the exclusive build system. All of them can be built with a simple command, though you do need the build environment set up with a compiler, Python, and optionally Moonscript.

The libass Meson port is currently in open PR. It was implemented a long time ago and had gotten stale, so until very recently I’d moved it into draft PR. I rebased it, updated it to reflect some of the changes in Autotools since the initial implementation, and tested it fairly extensively within the Aegisub port itself. It isn’t technically at full parity with Autotools, but it’s close enough that I’ve taken it out of draft since it should be fine to merge.

The Aegisub Meson port has been merged into master! It was blocked until very recently on a handful of Meson bugs that had been fixed in master but were not in a release, but as of 0.56.1 they’re available more broadly.

CI is functional on Windows, Linux, and MacOS. Github Actions is free, reliable, and well-integrated into the greater Github UI, and as a result it’s worked quite well for this purpose. My main complaint is that their documentation is clearly aimed at people familiar with containers and DevOps workflows, and there isn’t a very good ‘cookbook’ available for cross-platform native projects like this. The Windows container also dies when trying to statically link the debug executable, but that’s likely a consequence of the container resource limits and not really a black mark against Actions as a whole.

All the required Windows dependencies will be built locally as subprojects if not available on the system, and there are only a few optional ones left to sort out. Additionally, the Windows installer can be generated with a single command. This involves downloading various binaries off the internet and is admittedly somewhat fragile, but it’s very straightforward and should be easy to update if that becomes necessary. It does have additional dependencies, primarily InnoSetup. However, the installer is built and published automatically on CI for every commit, so the minimal setup required is at least clearly documented.

As mentioned (far) above, `.app` generation on MacOS is still nonfunctional. I don’t think it will be _that_ hard to finish since I already started the work, but Apple’s refusal to document the format and signing requirements make it far more work than it should be. I’m personally disinclined to pay Apple the $100 ransom to let Mac users run my software without opening a terminal, so who knows when I’ll bother adding support for it.

Additionally, localization on Windows and MacOS is broken, both for the app and the installer. I’ve currently just put it behind a flag and left that disabled. I’d like to get to it eventually, but it presents some real complications and seems less pressing than a lot of other problems.

Finally, I still need to PR ffms2 with a build flag to disable the audio gap filling code or just add a patch to our wrapfile. It causes more problems than it solves, but patching that wasn’t exactly a major concern when we couldn’t even generate an executable.

There’s still an unbelievable amount of work needed on both Aegisub itself and the automation scripts. Certain known-buggy Aegisub components should really be rewritten and exposed to Lua. DepCtrl still needs someone to finish the last 10% on the SQLite branch. Video panning is still a huge feature gap. Etc, etc. Who knows what I’ll get to next, but at least it’s now _possible_ to work on Aegisub itself.

After the libass port is merged, I may see again about getting push rights to the main Aegisub repo, since supposedly jfs would like to see it moving again and the Meson port is mostly ready to go. I’m not super concerned about this either way, but it might be nice? We’ll see. If not, I’ll cherry-pick over the valuable/non-broken commits and just work out of TypesettingTools.

# Reflections

## Meson

### Bugs

I wouldn’t be honest if I didn’t address that I ran into quite a few Meson bugs as part of this process. If you’re using it for a sufficiently complicated project, you probably will too. Personally, I think Meson offers enough that the tradeoff was worth it, but the bug list above in the build systtem itself was nontrivial, to say nothing of the various projects using it.

Most of the Meson bugs fit into one of three categories: Visual Studio backend, MacOS, or CMake.

On Windows with MSVC, you can ask Meson to either generate ninja files that invoke the compiler or a proper `.sln` file. The former is definitely much more stable, but the latter is valuable to a lot of Windows devs familiar with the Visual Studio workflow.

Similarly, MacOS appears to get a lot less attention than Windows or Linux, which is just how it goes in open source projects. A number of the project devs don’t even seem to have a MacOS machine.

Finally, the CMake module is fairly new and complicated. With that comes bugs, especially when overlapped with one of the previous two scenarios.

### CMake

Despite the bugs, however, the CMake module is a game-changer. The ability to use any CMake project as a submodule enables a _ton_ of new dependencies to be set up as a submodule and built locally. This is really valuable both for automatic dependency fetching and static linking. It also does so without a major performance impact, as it works by translating the CMake output to Meson. This means you can even view it in the Visual Studio solution, which is honestly crazy. I’m not sure this project would have even finished without it. It’s so good.

### Static linking

Meson has long had issues related to static vs dynamic linking, and while settings like `default_library` exist they are often not propagated correctly or default to dynamic linking when both are built. It would be really nice to have a “LINK STATICALLY OR DIE” flag somewhere, since otherwise I’m forced to go thread `static` arguments through a bunch of subprojects just to be sure.

### Evolution

Even beyond the CMake module, I think Meson has improved significantly as a build system over the course of this port. A lot of that seems to have come from some of the GNOME workloads, which are complicated and forced a re-evaluation of baked-in assumptions. Most releases have included features that were obviously useful to me. The downside is that there have been some deprecations, but most of them are for understandable reasons and enables the project to move faster. I’m personally happy with the tradeoff, but there’s definitely no free lunch.

## Migrations

This was an extremely costly, high-effort project. After starting work full-time, I’ve only ever devoted weekends to this, and that combined with the scope is why it took years.

I wish it had been possible for a more incremental migration. This was not _completely_ abrupt, since a number of Linux users started using builds via Meson, but this didn’t actually uncover that many bugs applicable to other platforms.

There was no real option of a piecemeal migration on Windows/MacOS, or even one that is based heavily off the old build system. So much of the MSVC solution was unclear, undocumented, or just plain magical that there was no way to work on components and check for parity. The platforms most in need of the migration were the hardest ones to complete. A rewrite of this level is usually not worth it, but I really don’t think there was any other choice here.

While I think reproducible builds are overrated[^1], I’ve come out of this with a much greater appreciation of _understandable_ and _maintainable_ builds. I understand the desire to pre-generate files and the lack of desire to document how, but the combination was incredibly painful. It’s not worth it unless you’re sure you will be maintaining the project into perpetuity; you want to avoid forcing an event like this at all costs. Migrations are much less painful if you can handle individual components and compare against a ground truth, temporarily maintaining two systems, but that’s not an option if the original system is sufficiently broken.

## Open source contributions

Most valuable contributions come from a small set of active developers. There are exceptions to this, but by in large drive-by contributions are more effort for the maintainer than just implementing the change themselves. This goes doubly so when there’s no communication with the maintainer beforehand.

This isn’t to blast any particular Aegisub contributor—it’s more an observation across my entire open source portfolio—but it’s definitely a real dynamic. I don’t think this is very surprising for a couple reasons, but after seeing it pointed out in [_Working in Public_](https://www.amazon.com/Working-Public-Making-Maintenance-Software/dp/0578675862) (an excellent book on open source work) it’s been painfully obvious. In addition to almost any codebase requiring a nontrivial contributor ramp-up, the maintainers’ priorities are likely not the same as those of a drive-by contributor, and people familiar with the primary maintainer(s) are much more likely to communicate with them beforehand and ensure alignment.

As a drive-by contributor, that means you should be understanding if your PR isn’t immediately reviewed, and maybe ping it once a month or so in case it falls off the maintainers’ radar. As a maintainer, this means you should seriously evaluate how much time you want to spend on these contributions. They can be a major time sink and not contribute to short-term goals, but they are an investment in both potential future maintainers and the FOSS community as a whole, as the contributors are probably less experienced engineers and almost certainly less experienced in your specialization.

In particular, my observation has been that if someone submits more than one PR (excluding multiple filed at once), that’s better than 95% of contributors and you should put them in the “could be a net positive contributor” bucket and try to get to their future PRs. The Github “Contributor” tag on users is helpful for this, since it’s dependent on there already being a commit in the repo under their handle.[^2]

## ICU

The most difficult dependency on Windows, by far, was ICU. Its build process is incredibly ugly, and replicating that in Meson proved quite difficult. For the full explanation you can check Myaa’s [pull request](https://github.com/TypesettingTools/Aegisub/pull/76), but I’ve attempted to summarize below.

First, the ICU build process involves an intermediary executable called `pkgdata` that takes in an ICU data file and outputs the `icudata` library.

Unfortunately, it sets up an object file manually and invokes the compiler/linker as subprocesses, with compiler information specified in a separate file. Meson sadly does not offer a convenient way to get the current compiler flags, so instead we read them in from an intermediate file via a Python script.

`pkgdata` is also implemented here as a `custom_target`, but Meson does not offer a convenient way to make clear its output is a library object. This will cause linker errors, and a nasty workaround involving wrapper library declarations is required.

Finally, within ICU itself there are a bunch of circular dependencies. The autotools build system solves this by building a stub `icudata` library and later linking with the proper library build, but replicating this in Meson proved difficult. Instead, we just build the libraries twice, first linking against the stub and then against the real library. This is wasteful, but at least it works.


[^1]: And yes, I have a background in computer security. I’m very familiar with the debate, and I still don’t agree that they add any value.

[^2]: This whole section probably belongs in a different essay, but it’s not large enough for its own and this one is already a grab bag anyway, so I’m just putting it here. It was inspired by the fact I had to ignore a bunch of random PRs while working on this recently, okay. At least I’m not pulling a wm4 and putting a video game review in here.
