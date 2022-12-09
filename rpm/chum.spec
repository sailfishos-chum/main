Summary:        SSU configuration for the SailfishOS:Chum community repository
License:        MIT
Name:           sailfishos-chum
Version:        0.5.0
Release:        1
Provides:       sailfishos-chum-repository
Group:          System
Source0:        %{name}-%{version}.tar.bz2
Requires:       ssu
Conflicts:      sailfishos-chum-testing
Conflicts:      sailfishos-chum-gui
BuildArch:      noarch

%description
The package sailfishos-chum is a helper RPM, which solely provides an
appropriate local repository configuration for utilising the SailfishOS:Chum
community repository with command line tools as pkcon or zypper.

Note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper. Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum testing repository.
Hence you might rather install the sailfishos-chum-gui RPM instead of the
sailfishos-chum RPM.

%package testing
Summary:        SSU configuration for the SailfishOS:Chum TESTING repository
License:        MIT
Provides:       sailfishos-chum-repository
Group:          System
Requires:       ssu
Conflicts:      sailfishos-chum
Conflicts:      sailfishos-chum-gui
BuildArch:      noarch

%description testing
The package sailfishos-chum-testing is a helper RPM, which solely provides an
appropriate local repository configuration for utilising the SailfishOS:Chum
TESTING repository with command line tools as pkcon or zypper.
Note that the SailfishOS:Chum testing repository is primarily aimed at
software developers.

Also note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper. Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum testing repository.
Hence you might rather install the sailfishos-chum-gui RPM instead of the
sailfishos-chum-testing RPM.

%prep
%setup -q

%build

%install

%files

%files testing

%post
if echo "$(ssu lr | grep '^ - ' | cut -f 3 -d ' ')" | grep -Fq sailfishos-chum
then
  ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(release)_%%(arch)/'
  ssu ur
fi
exit 0

%post testing
if echo "$(ssu lr | grep '^ - ' | cut -f 3 -d ' ')" | grep -Fq sailfishos-chum-testing
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
# committed on 18 February 2019 by tibbs ( https://pagure.io/user/tibbs ) as
# "8d0cec9 Partially convert to semantic line breaks." in
# https://pagure.io/packaging-committee/c/8d0cec97aedc9b34658d004e3a28123f36404324
