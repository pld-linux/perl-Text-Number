#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Number
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Number Perl module - overloaded class for printing numbers
Summary(pl.UTF-8):	Moduł Perla Text::Number - przeciążona klasa do wypisywania liczb
Name:		perl-Text-Number
Version:	0.80
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2971d31bc21dc22ca418055ab71291aa
URL:		http://search.cpan.org/dist/Text-Number/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Number Perl module provides a facility for transparently
configuring numbers to print the way you want them to. Calculations
are always executed using the full precision of the number, but
printing is rounded to the number of places of your choosing.

%description -l pl.UTF-8
Moduł Perla Text::Number udostępnia funkcje do przezroczystego
konfigurowania wypisywania liczb w żądany sposób. Do obliczeń zawsze
używane są liczby o maksymalnej precyzji, lecz podczas wypisywania są
one zaokrąglane do zadanej ilości miejsc dziesiętnych.

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
