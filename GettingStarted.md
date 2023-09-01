# SailfishOS:Chum - Getting Started with OBS

This document summarises the process of building your first package on the Sailfish&nbsp;OS OBS.
It only skims the surface of OBS and is not a manual.

To start building your packages on OBS you will require an account.
If you are not using the Sailfish&nbsp;OS OBS yet, you shall obtain an account there by contacting the user `lbt` on the IRC channel `#sailfishos`.

When your account is set up, you will have a "Home Project".
This is where you can start creating packages.
The URL for your home project will be:<br />
https://build.sailfishos.org/project/show/home:<username\>

## Creating a package on OBS

OBS projects contain packages which are built against target repositories
(i.e., Sailfish&nbsp;OS versions, not source / git repositories).

### Prerequisites

To build on OBS, the source repository must contain a spec file for building the RPM.
This will generally be the case for projects created using the Sailfish SDK.
The name of the spec file must match the package name and it must be located in the `rpm` top level directory at the source repository.

### Creating a Package

To create your first package, perform the following steps:

1. Click on "Create Package".
2. On the new package page, give the package a name and click "Save Changes".
3. You now need to add files to the package to allow OBS to get the source and build it.
   Create a file on your computer called `_service` with the following content:
    ```
    <services>
        <service name="tar_git">
        <param name="url">URL TO PROJECT</param>
        <param name="branch">master</param>
        <param name="revision"></param>
        </service>
    </services>
    ```
   Specify at least the URL.  If you want to build another branch, change the 
   branch name, and if you want to build a particular revision, specify a git hash
   or git tag in the revision field.
4. Back on OBS, click "Add File" then "Browse" and select the `_service` file you
   just created and click on "Save Changes".
5. If all goes well, OBS will fetch the source code.

## Adding target repositories

Back at the home project on OBS, you will require target repositories to build against.
These can be added using a UI, but it is easier to add them manually.

1. Click "Advanced" and "Meta".
   Note, do not confuse this with the package Meta configuration, even though the names are the same.
2. You will be presented with an XML description of the target repositories.
   Between the `<project> </project>` XML tags, add the following:
    ```
    <repository name="sailfish_latest_i486">
        <path project="sailfishos:latest" repository="latest_i486"/>
        <arch>i586</arch>
    </repository>
    <repository name="sailfish_latest_armv7hl">
        <path project="sailfishos:latest" repository="latest_armv7hl"/>
        <arch>armv8el</arch>
    </repository>
    <repository name="sailfish_latest_aarch64">
        <path project="sailfishos:latest" repository="latest_aarch64"/>
        <arch>aarch64</arch>
    </repository>
    <repository name="sailfish_4.1.0.24_armv7hl">
        <path project="sailfishos:4.1.0.24" repository="latest_armv7hl"/>
        <arch>armv8el</arch>
    </repository>
    <repository name="sailfish_4.1.0.24_aarch64">
        <path project="sailfishos:4.1.0.24" repository="latest_aarch64"/>
        <arch>aarch64</arch>
    </repository>
    <repository name="sailfish_4.1.0.24_i486">
        <path project="sailfishos:4.1.0.24" repository="latest_i486"/>
        <arch>i586</arch>
    </repository>
    ```
   This will create build targets for the 4.1.0 and the "latest" Sailfish&nbsp;OS release versions
   for all three supported architectures.
3. Click "Save Changes", navigate back to the project overview, and you should see
   the build status for each target on the right hand side.
4. You can click on the package name, and then click on the build target status to
   see the current build log.
  
## Submitting your package to SailfishOS:Chum:Testing

Once your builds are working fine, you can submit it for inclusion to the `sailfishos:chum:testing` OBS repository.

1. Navigate to the package, and click "Submit Package".
2. Enter the target project as `sailfishos:chum:testing`.
3. Click on "Ok".

For packages submitted to SailfishOS:Chum, please specify a particular git revision to be built
(hash or tag) and do not use webhooks, so that packages in SailfishOS:Chum are not automatically updated.
For this reason, you may want to set up your home project with builds from your master
branch for personal use, but a specific revision to be submitted to SailfishOS:Chum.

Please ensure that the license specified in the spec file matches that of the source repository
and that it follows one of the formats at https://github.com/sailfishos/rpmlint/blob/master/rpm/sailfish.toml#L151-L458

## Other useful notes

* You can create sub-projects in your home project to group builds together.
* You can add a repository to your device using `ssu ar` in order to install your built packages 
  on your device.
* To re-trigger OBS to download the latest code, click "Trigger services" at the package overview.
* You can configure OBS to not build certain packages against certain repositories, or disable
  certain projects from being published.  It is very flexible.  This is available from the "Repositories"
  tab.
* OBS will resolve dependencies when building a package, if dependency packages are available in 
  either the current project or the build target.
  If you want to build a package in your home project against other packages, which are only available 
  in SailfishOS:Chum (or another repository), then these can be added to the repository configuration
  with code as follows in the project "Meta" configuration:
  ```
  <repository name="sailfish_latest_armv7hl">
    <path project="sailfishos:latest" repository="latest_armv7hl"/>
    <path project="sailfishos:chum" repository="4.1.0.24_armv7hl"/>
    <arch>armv8el</arch>
  </repository>
  ```
