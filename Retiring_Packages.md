## Retiring packages from SailfishOS:Chum

The team at Jolla/Jollyboys, and the people providing packages at Chum rarely,
but increasingly often find themselves in the situation that a package has been
published at Chum, and a release of Sailfish OS published at a later point
ships the same software.

This causes the issue that Chum is suddenly in violation of the agreement that
no Sailfish OS upstream packages be published on it.

Still, the package is publiched on Chum, other software may depend on it, and
usually it's beneficial to keep it there, and continue to offer it for older OS
releases.

Hence this

### Process for retiring a package:

0. Hopefully, a Chum package maintainer is informed in due time by the Sailfish OS team that retirement is necessary.

1. Investigate differences in packaging. Things like subpackage names etc.
1. Identify the last SailfishOS release where the package may be published on Chum.
1. If there are relevant differences in packaging, for existing, published
   repository versions of the chum package, publish a new revision which aligns
   the chum packaging with the Sailfish OS one. 
   Think about the update case from the Chum verstion to the Sailfish OS version and
   ensure a clean update path is possible.
   Take care of `Obsoletes:`, `Conflicts:` and so on.
1. Optionally (and for `tar_git` packaging only), if the `sailfishos-mirror`
   organization now has a fork or clone repository, point git submodules there
   instead of the original.  1. Edit the .spec file so the package cannot be built
   on conflicting versions.
1. Note that disabling build repos on OBS may seem like a viable strategy, but
   this puts all the work in the hands of the Chum maintainers, and errors may
   lead to unwanted binaries ending up being published.  
   This task is better left to the packager.
 
Strategies that may be used in .spec files to disable building:

**ExclusiveArch: none**


```
%if 0%{?sailfishos_version} >= 50500
ExclusiveArch: none
%endif
```
This works on Sailfish OBS because the macro is defined there. Other build environments may or may not define it.

**Depending/Conflicting with `sailfish-version`**:

All Sailfish OS related build environments should have the  `sailfish-version` package.  
This has the added benefit that you can select whether to disable *building* or *installing* the package on the relevant Sailfish Version.

```
Requires:        sailfish-version < 5.0.0-1.1.1
BuildRequires:   sailfish-version < 5.0.0-1.1.1
```

----

### References:

 - https://github.com/sailfishos-chum/main/issues/118
 - https://github.com/sailfishos/issue-tracker/issues/7
