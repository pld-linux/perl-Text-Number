#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Number
Summary:	Text::Number Perl module - overloaded class for printing numbers
Summary(pl):	Modu� Perla Text::Number - przeci��ona klasa do wypisywania liczb
Name:		perl-Text-Number
Version:	0.80
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Number Perl module provides a facility for transparently
configuring numbers to print the way you want them to. Calculations
are always executed using the full precision of the number, but
printing is rounded to the number of places of your choosing.


%description -l pl
Modu� perla Text::Number udost�pnia funkcje do przezroczystego
konfigurowania wypisywania liczb w ��dany spos�b. Do oblicze� zawsze
u�ywane s� liczby o maksymalnej precyzji, lecz podczas wypisywania s�
one zaokr�glane do zadanej ilo�ci miejsc dziesi�tnych.

%prep
%setup -q -n %{pnam}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Text/Number.pm
%{_mandir}/man3/*
