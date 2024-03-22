## Maintainer's tasks on package submission to SailfishOS:Chum

On initial submission of a package by a package maintainer ("submitter" hereafter), a SailfishOS:Chum
maintainer is tasked to check that …

- the `_service` file contains a specific git tag or commit ID (hash).
  Alternative is source submission via compressed archive.

- the `_service` file does not contain a webhook.

- the license in rpm spec file is [approved by OSI](https://opensource.org/licenses) and
  matches the software license in the source code repository or the submitted archive.
  
- the license tag in rpm spec file is one of
  [github.com/sailfishos/rpmlint/blob/master/rpm/sailfish.toml#L150-L459](https://github.com/sailfishos/rpmlint/blob/master/rpm/sailfish.toml#L150-L459).

- no binary blobs, such as precompiled libraries, applications or other executable files, are part of the package submission.
  Bundled databases or similar are allowed.
  
- the package does not conflict with (e.g. replace) any package from Jolla's repositories for Sailfish&nbsp;OS.

After these checks have been successful, …

- accept the submission of the package to `sailfishos:chum:testing`.

- employ the submitter as a maintainer for the package in `sailfishos:chum:testing`.

- if building the package fails for some versions of SFOS, decide together with the submitter
  whether to disable those build targets or to adjust the package.

- with all compilation issues resolved, promote the package from `sailfishos:chum:testing`
  to `sailfishos:chum`.

- if some SFOS versions or architectures were disabled for a package in `sailfishos:chum:testing`,
  also disable them in `sailfishos:chum`.
