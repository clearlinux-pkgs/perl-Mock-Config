#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mock-Config
Version  : 0.03
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Mock-Config-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Mock-Config-0.03.tar.gz
Summary  : 'temporarily set Config or XSConfig values'
Group    : Development/Tools
License  : Artistic-2.0
BuildRequires : buildreq-cpan

%description
NAME
Mock::Config - temporarily set Config or XSConfig values
VERSION
Version 0.02

%package dev
Summary: dev components for the perl-Mock-Config package.
Group: Development
Provides: perl-Mock-Config-devel = %{version}-%{release}

%description dev
dev components for the perl-Mock-Config package.


%prep
%setup -q -n Mock-Config-0.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Mock/Config.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mock::Config.3
