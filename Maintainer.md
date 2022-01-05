# Maintainer's tasks on submission

On initial submission, maintainers are expected to check:

- `_service` file has specific git tag or commit ID. Alternative is
  source submission via compressed archive

- `_service` should not include any webhook

- license in RPM SPEC is open source and matches software license in
  repository or submitted archive
  
- license tag is one of https://github.com/sailfishos/rpmlint/blob/master/rpm/sailfish.toml#L152

- no binary blobs, such as precompiled libraries or applications, are
  submitted as a part of submission. Bundled databases or similar are
  allowed.
  
- Package does not conflict (ie replace) a system (from Jolla) package

After checks,

- accept the submission to `sailfishos:chum:testing`

- make the submitter a maintainer for a package in
  `sailfishos:chum:testing`

- if some versions of SFOS are failing, decide together with the
  submitter whether to disable those builds or adjust the package.

- with all compilation issues resolved, promote package from
  `sailfishos:chum:testing` to `sailfishos:chum`.

- if some SFOS versions were disabled for a package, disable them in
  `sailfishos:chum`
