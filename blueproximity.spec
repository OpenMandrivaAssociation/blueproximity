Name:		blueproximity
Version:	1.2.5
Release:	%mkrel 1 
Summary:	Detects you via your bluetooth devices and locks/unlocks the screen
BuildArch:	noarch
Group:		Communications
License:	GPLv2+
URL:		https://blueproximity.sourceforge.net/
Source0:	http://downloads.sourceforge.net/blueproximity/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		blueproximity-fix_paths.diff
Patch1:		blueproximity-fix-bash-script.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	desktop-file-utils gettext
Requires:	python-configobj python-pybluez  pygtk2.0-libglade

%description
Add security to your desktop by automatically locking and unlocking 
the screen when you and your phone leave/enter the desk. Think of a 
proximity detector for your mobile phone via bluetooth.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p0 -b .fedorization
%patch1 -p0 -b .fix-bash-script

%build

%install
rm -rf %{buildroot}

# Create Directory Structure
install -d %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps/
install -d %{buildroot}%{_datadir}/%{name}/pixmaps/
install -d %{buildroot}%{_mandir}/man1/

# Install Files
install -p -m 0755 start_proximity.sh %{buildroot}%{_bindir}/%{name}
install -p -m 0755 proximity.py %{buildroot}%{_datadir}/%{name}/
install -p -m 0644 proximity.glade %{buildroot}%{_datadir}/%{name}/
install -p -m 0644 doc/blueproximity.1 %{buildroot}%{_mandir}/man1/

# Install Languages
for i in $(ls LANG/); do
install -d %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
install -p -m 0644 LANG/$i/LC_MESSAGES/* %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
done

# Install Images
for i in $(ls *.svg); do
install -p -m 0644 $i %{buildroot}%{_datadir}/%{name}/pixmaps/
done

# Link in SVG
pushd %{buildroot}%{_datadir}
ln -s ../%{name}/pixmaps/%{name}_base.svg pixmaps/
popd

# Install Menu Item
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Find Languages
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING README doc/manual*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/blueproximity*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_base.svg




%changelog
* Tue Sep 08 2009 Michael Scherer <misc@mandriva.org> 1.2.5-1mdv2010.0
+ Revision: 434052
- submit rpm based on fedora src.rpm
- add missing requires
- fix Group
- fix naming of the fedora patch
- fix requires
- import blueproximity

