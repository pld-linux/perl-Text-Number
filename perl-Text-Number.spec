#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Number
Summary:	Text::Number Perl module - overloaded class for printing numbers
Summary(pl):	Modu³ Perla Text::Number - przeci±¿ona klasa do wypisywania liczb
Name:		perl-Text-Number
Version:	0.80
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2971d31bc21dc22ca418055ab71291aa
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Number Perl module provides a facility for transparently
configuring numbers to print the way you want them to. Calculations
are always executed using the full precision of the number, but
printing is rounded to the number of places of your choosing.

%description -l pl
Modu³ Perla Text::Number udostêpnia funkcje do przezroczystego
konfigurowania wypisywania liczb w ¿±dany sposób. Do obliczeñ zawsze
u¿ywane s± liczby o maksymalnej precyzji, lecz podczas wypisywania s±
one zaokr±glane do zadanej ilo¶ci miejsc dziesiêtnych.

%prep
%setup -q -n %{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Number.pm
%{_mandir}/man3/*
