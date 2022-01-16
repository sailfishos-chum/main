# SailfishOS:Chum community repository: Documentation and issue tracker

The SailfishOS:Chum community repository provides a collection of
applications, tools and libraries compiled for various hardware
architectures and Sailfish&nbsp;OS release versions.

The ambition is to become the principal software distribution platform
for Sailfish&nbsp;OS.

In contrast to the software distribution model of the Jolla Store or
OpenRepos, to which binary packages are uploaded by developers, at
SailfishOS:Chum software is compiled and packaged into RPMs in a
reproducible manner directly from its source code. The source code used
for compiling and packaging is submitted by developers to OBS (Open
Build Service), which generates multiple RPM files for different
combinations of hardware architectures and Sailfish&nbsp;OS release
versions.<br />
This scheme ensures that the complete source code of all packages at 
SailfishOS:Chum is available and inspectable there, and that all
packages are generated solely from this source code. Hence all software
packages at SailfishOS:Chum are created in a transparent and fully
traceable manner.

By collecting software for Sailfish&nbsp;OS in a single automated build
system, collaboration between developers through common packaging of
shared libraries etc. is fostered, duplication of work for keeping these
common packages up-to-date is eliminated, and it becomes much easier to
determine which pieces of software exist and which are missing at the
Sailfish&nbsp;OS OBS. Additionally this eases tracing multiple and
potentially layered dependencies ("dependency chains") which is crucial
for keeping the software supply chains of complex packages up-to-date.

The SailfishOS:Chum repository is located at the Sailfish&nbsp;OS OBS:
https://build.sailfishos.org/project/show/sailfishos:chum

This repository at GitHub is used for filing general issues and
publishing documentation for SailfishOS:Chum.

For the etymological origin and meanings of the word "chum", see
[en.wikipedia.org:Chumming](https://en.wikipedia.org/wiki/Chumming)
and [en.wiktionary.org:chum](https://en.wiktionary.org/wiki/chum).


## How to use the SailfishOS:Chum repository: User's guide

There are two different ways of using the SailfishOS:Chum repository:
- with the [SailfishOS:Chum GUI application](https://github.com/sailfishos-chum/sailfishos-chum-gui)
- with the usual command line tools for package management, `pkcon` or `zypper`

### How to install the SailfishOS:Chum GUI-client app

The client app (GUI) for SailfishOS:Chum is available for easy installation at [chumrpm.netlify.app](https://chumrpm.netlify.app/) and its individual RPMs are also provided at [the SailfishOS:Chum repository](https://build.sailfishos.org/package/show/sailfishos:chum/sailfishos-chum-gui).

### How to deploy the configuration for command line tools

For using the SailfishOS:Chum repository per command line tools, a `sailfishos-chum` helper RPM is available for easy installation also at [chumrpm.netlify.app](https://chumrpm.netlify.app/) (and additionally at the [SailfishOS:Chum repository](https://build.sailfishos.org/package/show/sailfishos:chum/sailfishos-chum) proper), which solely provides an appropriate local repository configuration for utilising the SailfishOS:Chum repository.

Note that installing the SailfishOS:Chum GUI-client deploys the same local repository configuration, so your device is already set for using the SailfishOS:Chum repository with the usual command line tools for package management, then.

To utilise the SailfishOS:Chum repository using command line tools on your device, you have to …
1. download either of the aforementioned packages `sailfishos-chum` or `sailfishos-chum-gui`.
2. install it using a file manager or as root user by executing `pkcon install-local sailfishos-chum[-gui]-<version>.rpm` or `zypper in sailfishos-chum[-gui]-<version>.rpm`.
3. refresh the software cache on your device as root user per `pkcon refresh` or `zypper ref`.
4. install any software packages you like from the SailfishOS:Chum repository as root user per `pkcon install <package name>` or `zypper in <package name>`.

As all software packages at SailfishOS:Chum have their vendor set to `chum`, it is easy to determine which packages are installed from the SailfishOS:Chum repository by executing:<br />
`rpm -qa --queryformat '%{vendor}:%{name}\n' | fgrep chum`


## How to use the SailfishOS:Chum repository: Developer's guide

There are no major restrictions imposed on software submitted to SailfishOS:Chum.
Although one limitation is that submitted software should not interfere with any software distributed by Jolla as a part of Sailfish&nbsp;OS, which also means that updating libraries distributed per Jolla's repositories must be avoided.
Note that Jolla's repositories provide far more software packages than the ones installed by default.

All kinds of software for Sailfish&nbsp;OS are welcome at SailfishOS:Chum, for example, actively developed SFOS applications, discontinued SFOS applications, tools and libraries missing on SFOS as distributed by Jolla.
Depending on the type of software, the recommended way of submitting software to SailfisOS:Chum varies, as described in the sections below.

The overall process is as follows. 
1. For the initial submission of a software package:
   - Make your software package successfully compile at the Sailfish&nbsp;OS OBS.
   - Submit your package to the SailfishOS:Chum testing repository `sailfishos:chum:testing` by using the "Submit package" action of OBS. A version has to be specified when submitting.
   - The `sailfishos:chum:testing` maintainers will accept or reject your request and check if your software package successfully builds at the SailfishOS:Chum testing repository. If all is fine, the package will be promoted to the main `sailfishos:chum` repository by the SailfishOS:Chum maintainers. If something went wrong, you will be notified to resolve the issue.
2. After a successful initial submission, you will be made maintainer of your software package in the `sailfishos:chum:testing` repository, which allows you to handle updates in a simplified manner:
   - For updating your package, update the source, then change the version information in the OBS service file at `sailfishos:chum:testing`.
   - Check that your software package successfully builds at the SailfishOS:Chum testing repository `sailfishos:chum:testing`.
   - Ultimately use the "Submit package" action to trigger promoting your package from `sailfishos:chum:testing` to `sailfishos:chum`.

As a reference, see the [maintainer's tasks](Maintainer.md) document for a list of checks and balances performed by the SailfishOS:Chum maintainers.

Also note the documentation for the [additional metadata for SailfishOS:Chum](Metadata.md) in rpm spec files.

### Asking for help

If something is not clear or you become stuck in the process, feel free to ask for help via the IRC channel #sailfishos (you may contact `piggz` or `rinigus` there), the [Sailfish&nbsp;OS forum](https://forum.sailfishos.org/search?q=chum), or filing an [issue here at GitHub](https://github.com/sailfishos-chum/main/issues).

For an OBS primer, see the [Getting Started with OBS](GettingStarted.md) document.

You may also ask someone else to package some software for you.
Just be aware that for this to work out, you might need to provide some incentive.

### Submitting actively developed applications

If an application is already compiled at the Sailfish&nbsp;OS OBS, simply use the "Submit package" action for the application and all its dependencies, which are not yet available as part of the SailfishOS:Chum respository or Jolla's repositories.

If you are not using the Sailfish&nbsp;OS OBS yet, you should obtain an account there by contacting the user `lbt` at the IRC channel #sailfishos and then configure your software package at the Sailfish&nbsp;OS OBS; alternatively you may ask the SailfishOS:Chum maintainers to add your software to the SailfishOS:Chum testing repository as a preliminary measure.

For actively developed applications, it is expected that the source code is fetched from the main application repository where it is
developed.
In contrast to the subsequent paragraph, no requests for forking a software as a project under the GitHub organization [sailfishos-chum](https://github.com/sailfishos-chum) are expected for actively developed applications.

### Submitting abandoned applications

If an application has not been picked up by some other developer (please check thoroughly first), it is suggested to open [an issue at this repository](https://github.com/sailfishos-chum/main/issues) requesting to add that application as a project under the GitHub organization [sailfishos-chum](https://github.com/sailfishos-chum). The link to the original git repository at GitHub, GitLab or elsewhere must be included.

The request will be evaluated and a fork of the application into the GitHub organization [sailfishos-chum](https://github.com/sailfishos-chum) might be created. If necessary the packaging scripts will be updated and ultimately the software might be added to the SailfishOS:Chum testing repository with
the perspective of promotion to the SailfishOS:Chum main repository.

### Submitting tools and libraries

If you want to submit a tool or library, which is actively maintained as an upstream version (for example, Midnight Commander), it is suggested to request creating a repository at the GitHub organization [sailfishos-chum](https://github.com/sailfishos-chum) and adding it to the Sailfish&nbsp;OS OBS.
For that, open [an issue at this repository](https://github.com/sailfishos-chum/main/issues), the SailfishOS:Chum maintainers will create a source code repository for you in which you will be able to adapt and package the software as needed for Sailfish&nbsp;OS.

If you already have a source code repository for adapting and packaging the software for Sailfish&nbsp;OS, it can be either forked by the GitHub organization [sailfishos-chum](https://github.com/sailfishos-chum) or, at your choice, transferred to this organization; alternatively you may follow the approach described for [actively developed applications](#submitting-actively-developed-applications).

For adapting and packaging the software for Sailfish&nbsp;OS, perferably use the scheme Jolla employs for [the majority of Sailfish&nbsp;OS packages](https://github.com/sailfishos): Add the upstream source code repository as a submodule and maintain your patches and packaging scripts in your downstream
repository.


## SailfishOS:Chum FAQ

- My software requires specific SFOS versions, can I still use the SailfishOS:Chum repository?
  
  Yes, you can.
  You simply have to disable the unsupported SFOS versions and / or architectures in the OBS Meta settings for your package.
  Take a look at [Pure Maps' OBS Meta settings](https://build.sailfishos.org/package/meta/sailfishos:chum/pure-maps) as an example.

- Can I build differently depending on the Sailfish&nbsp;OS version?
  
  Yes, you can.
  You can use the RPM macro `sailfishos_version` to build differently depending on the release version.
  This works in the same manner as for other Linux distributions, so you can support multiple Linux distributions with a single spec file.
  For details, see [openSUSE:Build_Service_cross_distribution_howto](https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto).
  
- Can I use the RPMs of my software built at SailfishOS:Chum to upload them to the Jolla Store?
  
  No, you cannot, because RPMs built at SailfishOS:Chum have the vendor set to `chum`, which is not allowed at the Jolla Store ("harbour").
  However, it is easy to set up a personal repository at the Sailfish&nbsp;OS OBS, configure `sailfishos:chum` to provide the required dependencies and re-build your packages at your own repository.
  As a result, you will get automated builds for all architectures wanted without the vendor set to `chum` in your RPMs.

- Can I use the RPMs of my software built at SailfishOS:Chum to upload them to OpenRepos or elsewhere?
  
  While you could do that, it is not recommended to re-distribute RPMs from SailfishOS:Chum because they all have the vendor set to `chum`, which will prevent users from distinguishing whether a package was directly installed from the SailfishOS:Chum repository or from some other package repository.<br />
  For a way to automatically build packages at the Sailfis&nbsp;OS OBS utilising SailfishOS:Chum for dependencies, but having the vendor not set to `chum`, see the previous answer.

- Are there limitations on the licensing of the software which is submitted to SailfishOS:Chum?
  
  Yes, in general solely software which is distributed under an [OSI approved license](https://opensource.org/licenses) might be submitted to the Sailfish&nbsp;OS OBS.
  Exceptions may be made in special cases as firmware blobs, but in general this guidance shall be obeyed:
  [openSUSE:Build_Service_application_blacklist](https://en.opensuse.org/openSUSE:Build_Service_application_blacklist)
