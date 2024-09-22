Summary:	Library for creating and editing videos
Name:		libopenshot
Version:	0.3.3
Release:	2
License:	LGPL-3.0+
Group:		Libraries
Source0:	https://github.com/OpenShot/libopenshot/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3fc1f185050bf01b73948944b8e13bc7
URL:		http://www.openshot.org/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5MultimediaWidgets-devel
BuildRequires:	cmake
BuildRequires:	cppzmq-devel
BuildRequires:	doxygen
BuildRequires:	ffmpeg-devel
BuildRequires:	ffmpeg-libs
BuildRequires:	libopenshot-audio-devel >= 0.3
BuildRequires:	libstdc++-devel
BuildRequires:	python3-devel
BuildRequires:	swig
BuildRequires:	unittest-cpp-devel
BuildRequires:	zeromq-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libopenshot.so.*

%description
OpenShot Library (libopenshot) is an open-source project dedicated to
delivering high quality video editing, animation, and playback
solutions to the world. For more information visit
<http://www.openshot.org/>.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python3-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python3-%{name}
The python-%{name} package contains python bindings for applications
that use %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DENABLE_RUBY=NO
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenshot.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenshot.so.26

%files devel
%defattr(644,root,root,755)
%{_includedir}/libopenshot
%attr(755,root,root) %{_libdir}/libopenshot.so

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitedir}/openshot.py
%attr(755,root,root) %{py3_sitedir}/_openshot.so
