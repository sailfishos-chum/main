Summary:        SSU configuration for the SailfishOS:Chum community repository
License:        MIT
Name:           sailfishos-chum
Version:        0.5.1
Release:        1
Provides:       sailfishos-chum-repository
Group:          System
URL:            https://github.com/sailfishos-chum/main
Source0:        %{url}/archive/%{version}/main-%{version}.tar.gz
Requires:       ssu
Requires(post): ssu
Requires(postun): ssu
Conflicts:      sailfishos-chum-testing
Conflicts:      sailfishos-chum-gui
Conflicts:      sailfishos-chum-gui-installer
BuildArch:      noarch

%description
The package sailfishos-chum is a helper RPM, which solely provides an
appropriate local repository configuration for utilising the SailfishOS:Chum
community repository with command line tools as pkcon or zypper.

Note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper.  Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum testing repository.
Hence you might rather install the sailfishos-chum-gui RPM (e.g., via the
sailfishos-chum-gui-installer RPM), instead of the sailfishos-chum RPM.

%if "%{?vendor}" == "chum"
PackageName: SailfishOS:Chum repository configuration RPM
Type: generic
Categories:
 - Utilities
 - System
 - PackageManager
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/main/icons/%{name}.svg
Url:
  Homepage: %{url}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif


%package testing
Summary:        SSU configuration for the SailfishOS:Chum TESTING repository
License:        MIT
Provides:       sailfishos-chum-repository
Group:          System
Requires:       ssu
Requires(post): ssu
Requires(postun): ssu
Conflicts:      sailfishos-chum
Conflicts:      sailfishos-chum-gui
Conflicts:      sailfishos-chum-gui-installer
BuildArch:      noarch

%description testing
The package sailfishos-chum-testing is a helper RPM, which solely provides an
appropriate local repository configuration for utilising the SailfishOS:Chum
TESTING repository with command line tools as pkcon or zypper.
Note that the SailfishOS:Chum testing repository is primarily aimed at
software developers.

Also note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper.  Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum testing repository.
Hence you might rather install the sailfishos-chum-gui RPM (e.g., via the
sailfishos-chum-gui-installer RPM), instead of the sailfishos-chum-testing RPM.

%if "%{?vendor}" == "chum"
PackageName: SailfishOS:Chum TESTING repository configuration RPM
Type: generic
Categories:
 - Utilities
 - System
 - PackageManager
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/main/icons/%{name}.svg
Url:
  Homepage: %{url}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif


%prep
%setup -q

%build

%install

%files

%files testing

%post
if ! ssu lr | grep '^ - ' | cut -f 3 -d ' ' | grep -Fq sailfishos-chum
then
  ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(release)_%%(arch)/'
  ssu ur
fi
exit 0

%post testing
if ! ssu lr | grep '^ - ' | cut -f 3 -d ' ' | grep -Fq sailfishos-chum-testing
then
  ssu ar sailfishos-chum-testing 'https://repo.sailfishos.org/obs/sailfishos:/chum:/testing/%%(release)_%%(arch)/'
  ssu ur
fi
exit 0

%postun
if [ "$1" = 0 ]  # Removal
  ssu rr sailfishos-chum
  rm -f /var/cache/ssu/features.ini
  ssu ur
fi
exit 0

%postun testing
if [ "$1" = 0 ]  # Removal
  ssu rr sailfishos-chum-testing
  rm -f /var/cache/ssu/features.ini
  ssu ur
fi
exit 0

# BTW, `ssu`, `rm -f`, `mkdir -p` etc. *always* return with "0" ("success"), hence
# no appended `|| true` needed to satisfy `set -e` for failing commands outside of
# flow control directives (if, while, until etc.).  Furthermore on Fedora Docs it
# is indicated that solely the final exit status of a whole scriptlet is crucial: 
# See https://docs.pagure.org/packaging-guidelines/Packaging%3AScriptlets.html
# or https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
# committed on 18 February 2019 by tibbs ( https://pagure.io/user/tibbs ) in
# https://pagure.io/packaging-committee/c/8d0cec97aedc9b34658d004e3a28123f36404324
# Hence I have the impression, that only the main section of a spec file is
# interpreted in a shell called with the option `-e', but not the scriptlets
# (`%%pre`, `%%post`, `%%preun`, `%%postun`, `%%pretrans`, `%%posttrans`,
# `%%trigger*` and `%%file*`).

%changelog
* Tue Jan 03 2023 olf <Olf0@users.noreply.github.com> - 0.5.1-1
- Add `URL:` in spec file
- `Conflict: -installer` in spec file
- Add SailfishOS:Chum metadata to spec file