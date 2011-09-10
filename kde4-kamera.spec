%define		_state		stable
%define		qtver		4.7.3

Summary:	K Desktop Environment - Digital camera support
Summary(pl.UTF-8):	K Desktop Environment - Obs�<82>uga kamer cyfrowych
Name:		kamera
Version:	4.7.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	4f5669536561f1125f9fc3f12c501fd8
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libgphoto2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kamera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kamera is an IO slave and a KControl panel module which allows you to
access folders and images within any digital camera supported by the
upcoming gPhoto2 libraries. If you have a supported camera, you can
start using it with most KDE applications in two easy steps: simply
configure your camera model and port type from a list in KControl,
then start accessing the camera contents with a kamera:/ URL.

%description -l pl.UTF-8
kamera to moduł IO slave oraz panelu KControl umożliwiający dostęp do
folderów i zdjęć w dowolnym aparacie cyfrowym obsługiwanym przez
biblioteki gPhoto2. Jeśli mamy obsługiwany aparat, można zacząć używać
go w większości aplikacji KDE w dwóch krokach: wybrać model i port
aparatu z listy w KControl, a następnie odwoływać się do zawartości
aparatu przez URL kamera:/.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DGWENVIEW_SEMANTICINFO_BACKEND=Nepomuk \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kamera.so
%attr(755,root,root) %{_libdir}/kde4/kio_kamera.so
%{_datadir}/kde4/services/kamera.desktop
%{_datadir}/kde4/services/camera.protocol
%{_kdedocdir}/en/kcontrol/kamera
%{_datadir}/apps/solid/actions/solid_camera.desktop
