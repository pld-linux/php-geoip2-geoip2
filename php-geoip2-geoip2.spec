%define		pkgname	geoip2
%define		php_min_version 5.4
Summary:	MaxMind GeoIP2 PHP API
Name:		php-geoip2-%{pkgname}
Version:	2.9.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://github.com/maxmind/GeoIP2-php/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	4389d315cd276636c7507b87e2fb21dc
URL:		http://maxmind.github.io/GeoIP2-php/
Requires:	php(core) >= %{php_min_version}
Requires:	php-maxmind-db-reader >= 0.2
Suggests:	GeoLite2-db-City
Suggests:	GeoLite2-db-Country
# Guzzle is needed when using Webservice
Suggests:	php-guzzle-guzzle >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution provides an API for the GeoIP2 web services and the
GeoLite2 databases.

The commercial GeoIP2 databases have not yet been released as a
downloadable product.

%prep
%setup -qn GeoIP2-php-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/GeoIp2
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/GeoIp2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{php_data_dir}/GeoIp2
