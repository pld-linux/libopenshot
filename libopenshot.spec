Summary:	Library for creating and editing videos
Name:		libopenshot
Version:	0.1.2
Release:	4
License:	LGPL-3.0+
Group:		Libraries
URL:		http://www.openshot.org/
Source0:	https://launchpad.net/libopenshot/0.1/0.1.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	1491f454af8ef23b6c2f7f3e4ce39291
Patch0:		imagemagick7.patch
Group:		Development/Libraries
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5MultimediaWidgets-devel
BuildRequires:	cmake
BuildRequires:	cppzmq-devel
BuildRequires:	doxygen
BuildRequires:	ffmpeg-devel
BuildRequires:	ffmpeg-libs
BuildRequires:	libopenshot-audio-devel
BuildRequires:	libstdc++-devel
BuildRequires:	python3-devel
BuildRequires:	swig
BuildRequires:	unittest-cpp-devel
BuildRequires:	zeromq-devel

%description
OpenShot Library (libopenshot) is an open-source project dedicated to
delivering high quality video editing, animation, and playback
solutions to the world. For more information visit
<http://www.openshot.org/>.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    -n python3-%{name}
The python-%{name} package contains python bindings for applications
that use %{name}.

%prep
%setup -q -c
%patch0 -p1

%build
install -d build

sed -i -e 's#${_REL_PYTHON_MODULE_PATH}#%{py3_sitedir}#g' src/bindings/python/CMakeLists.txt

cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenshot.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenshot.so.9

%files devel
%defattr(644,root,root,755)
%{_includedir}/libopenshot
%attr(755,root,root) %{_libdir}/libopenshot.so

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitedir}/openshot.py
%attr(755,root,root) %{py3_sitedir}/_openshot.so
