Summary:	Small utility to dump info about DRM devices
Name:		drm_info
Version:	2.7.0
Release:	1
License:	MIT
Group:		Applications/System
Source0:	https://gitlab.freedesktop.org/emersion/drm_info/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8d459631b0792791575ea3233ab8ddea
URL:		https://gitlab.freedesktop.org/emersion/drm_info
BuildRequires:	gcc >= 6:4.6
BuildRequires:	json-c-devel >= 0.14
BuildRequires:	libdrm-devel >= 2.4.122
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
Requires:	json-c >= 0.14
Requires:	libdrm >= 2.4.122
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility to dump info about DRM devices.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/drm_info
%{_mandir}/man1/drm_info.1*
