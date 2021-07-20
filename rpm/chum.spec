Summary:        Sailfish OS Community repository
License:        MIT
Name:           sailfishos-chum
Version:        1.0.0
Release:        1
Provides:       sailfishos-chum-repository
Group:          System
Source0:        %{name}-%{version}.tar.bz2
Requires:	ssu
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

%install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ssu/features.d/

cp ssu/sailfishos-chum.ini $RPM_BUILD_ROOT/%{_datadir}/ssu/features.d/
cp ssu/sailfishos-chum-testing.ini $RPM_BUILD_ROOT/%{_datadir}/ssu/features.d/

%post
ssu ur || true

%post testing
ssu ur || true

%postun
ssu ur || true

%postun testing
ssu ur || true

%files
%defattr(-,root,root,-)
%{_datadir}/ssu/features.d/sailfishos-chum.ini

%files testing
%defattr(-,root,root,-)
%{_datadir}/ssu/features.d/sailfishos-chum-testing.ini
