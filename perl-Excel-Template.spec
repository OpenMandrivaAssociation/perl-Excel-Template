%define upstream_name    Excel-Template
%define upstream_version 0.34
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.34
Release:	1

Summary:	Templating module that generates Excel
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Excel/Excel-Template-0.34.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Spreadsheet::WriteExcel)
BuildRequires:	perl(Spreadsheet::WriteExcel::Utility)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
This is a module used for templating Excel files. Its genesis came from the
need to use the same datastructure as the HTML::Template manpage, but
provide Excel files instead. The existing modules don't do the trick, as
they require replication of logic that's already been done within the
HTML::Template manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.330.0-2mdv2011.0
+ Revision: 657336
- rebuild for updated spec-helper

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.330.0-1
+ Revision: 639635
- update to new version 0.33

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.320.0-1mdv2011.0
+ Revision: 627063
- import perl-Excel-Template


