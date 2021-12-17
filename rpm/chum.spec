Summary:        Sailfish OS Community repository
License:        MIT
Name:           sailfishos-chum
Version:        1.1.0
Release:        1
Provides:       sailfishos-chum-repository
Group:          System
Source0:        %{name}-%{version}.tar.bz2
Requires:	    ssu
Conflicts:      sailfishos-chum-testing
BuildArch:      noarch

%description
%{summary}.

%package testing
Summary:        Sailfish OS Community repository: Testing repository
License:        MIT
Provides:       sailfishos-chum-repository
Group:          System
Requires:       ssu
Conflicts:      sailfishos-chum
BuildArch:      noarch

%description testing
%{summary}.

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
