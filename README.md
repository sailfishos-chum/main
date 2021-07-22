# Sailfish OS Community repositories: Documentation and issues

Sailfish OS Community repositories are providing collection of
applications, tools, and libraries compiled for different combinations
of architectures and Sailfish versions.

Ambition is to become the main repository for software distribution on
Sailfish OS.

When compared to the software distribution via Jolla Store or
OpenRepos, the software is compiled into RPMs in a reproducible way
directly from the source. The source used for the compilation is
available at OBS together with the compiled packages. This is in
contrast with Jolla Store and OpenRepos where all packages are uploaded
in binary form without any control over how the binary was compiled.

By collecting the software in a single automated build system, we can
benefit from collaboration between developers through shared packaging
of required libraries, reduce duplication of the work by keeping the
packages up to date, and get a clear overview of missing software.

The repository is located at OBS:
- https://build.merproject.org/project/show/sailfishos:chum

This repository at GitHub is used for filing general issues and
publishing documentation.

Origin of "chum": see http://en.wikipedia.org/wiki/Chumming


## How to use these repositories: users

At the moment of writing, there is no GUI for selecting packages for
installation and it has to be done through command line tools
(`zypper` or `pkcon`).

To use the repositories on your device, users would have to
- install package `sailfishos-chum`;
- refresh software cache on device (`devel-su zypper ref`),
- install the software (`devel-su zypper in ...`)

As all software is compiled with the vendor set to `chum`, it is easy
to find out which packages are installed from this repository by running

```
rpm -qa --queryformat '%{vendor}:%{name}\n' | grep chum
```


## How to use these repositories: developers

Overall submission model is as follows:

- get the package compiled at OBS.

- submit the package to `sailfishos:chum:testing` using "Submit
  package" action at OBS. Specific version has to be specified in
  submission.

- `sailfishos:chum:testing` maintainers will accept your request and
  check if it compiles in `:testing` repository. If all is fine, the
  package will get promoted to `sailfishos:chum` by maintainers. If
  something is wrong, maintainers will work with you to resolve the
  issues.

There are no major limitations imposed on the submitted software. Main
limitation is that it should not interfere with any software
distributed by Jolla as a part of Sailfish OS. This includes updating
libraries distributed as a part of Sailfish OS.

All types of software is welcome as long as it can be used on Sailfish
OS devices. This includes actively developed SFOS applications,
discontinued SFOS applications, tools and libraries missing on SFOS as
distributed by Jolla. Depending on the type of software, recommended
ways of submission vary, as described below.

After the successful submission, updates are handled by changing
version information at OBS service file in `sailfishos:chum:testing`,
checking that it compiles, and promotion to `sailfishos:chum`.


### Asking for help

If something is not clear or you get stuck in the process, feel free
to ask for help via IRC (#sailfishos),
[Sailfish forum](https://forum.sailfishos.org), or filing
issues over here.

You can ask someone else to package the software as well. Just be
aware that for this effort to work out, we need many to contribute.


### Submitting actively developed applications

If you have the application compiled at OBS already, just use "Submit
package" for the application and all the libraries it requires.

If you have not developed using OBS yet, then you could either ask
maintainers to add your project to OBS directly into
`sailfishos:chum:testing` or, a better long-term solution, make
account at OBS through pinging `lbt` at IRC and configure the package
at OBS.

For actively developed applications, it is expected that the software
is compiled from the main application repository where it is
developed. No forks at GitHub into https://github.com/sailfishos-chum
are expected.


### Submitting abandoned applications

Assuming that the application has not been picked up by some
developer, it is suggested to open an issue in this repository with
the request to add that application into the repository. Include
original GitHub/GitLab repository link with the issue.

The plan is then to make a fork of the application into this GitHub
organization (https://github.com/sailfishos-chum), if needed, update
packaging scripts and then add it to `sailfishos:chum:testing` with
the later promotion to `sailfishos:chum`.


### Submitting Linux tools and libraries

If you want to submit tool or library which is mainly upstream version
(for example Midnight Commander) then it is suggested to proceed by
making repository in this organization and later adding it to OBS. For
that, open an issue in this repository, maintainers will create
repository for you and then you would be able to package the software
as needed.

If you have packaging repository already, it is possible to either
fork it or, if you wish, you could transfer the repository over to
this organization.

As for the packaging approach, it is suggested to use the same
approach as is used for the most of Sailfish OS core packages: adding
upstream as submodule and packaging scripts/patches into the packaging
repository.

## Q&A

- My software requires specific SFOS versions, can I still use Chum
  repositories? Yes, you can. You would just have to disable the
  versions and architectures of SFOS that are not supported in OBS
  package Meta settings. Example: see Pure Maps.

- Can I build differently depending on the Sailfish version?  Yes you
  can.  You can use the RPM macro sailfishos_version to build differently
  depending on the release.  This works the same as for other 
  distributions so your .spec can be cross distro.  See
  https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
  for more information.
  
- Can I use the compiled RPMs of my software to upload it to Jolla
  Store? No, you cannot as compiled RPMs have a vendor set to `chum`,
  which is not allowed in the store. However, it is easy to setup your
  personal repository at OBS, set `sailfishos:chum` to provide the
  required libraries and recompile the packages in your own
  repository. As a result, you will get automated builds for all the
  needed architectures without the vendor flag set in RPM.

- Can I use the compiled RPMs of my software to upload it to
  OpenRepos? While you can do so, it is not recommended as it will
  prevent users from distinguishing whether the software was installed
  from chum repository or came from some other source. For a way to
  compile the packages using OBS, see the response above.

- Are there limitations on what software can be packaged? Yes, in general 
  we only want software that is distributed via an OSI approved license to
  be built and shipped on OBS.  There may be exceptions like some firmware 
  blobs but in general, follow the guiddance at:
  https://en.opensuse.org/openSUSE:Build_Service_application_blacklist
