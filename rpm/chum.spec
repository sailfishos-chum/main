Summary:        SSU configuration for the SailfishOS:Chum community repository
License:        MIT
Name:           sailfishos-chum
Version:        0.3.0
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
%setup -q -n %{name}-%{version}

%build

%install

%files

%files testing

%posttrans
rm -f /var/cache/ssu/features.ini || true
ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(release)_%%(arch)/'
ssu ur || true

%posttrans testing
rm -f /var/cache/ssu/features.ini || true
ssu ar sailfishos-chum-testing 'https://repo.sailfishos.org/obs/sailfishos:/chum:/testing/%%(release)_%%(arch)/'
ssu ur || true

%postun
ssu rr sailfishos-chum || true
rm -f /var/cache/ssu/features.ini || true
ssu ur || true

%postun testing
ssu rr sailfishos-chum-testing || true
rm -f /var/cache/ssu/features.ini || true
ssu ur || true
