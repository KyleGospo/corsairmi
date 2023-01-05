Name:           corsairmi
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Minimal program for Linux to read monitoring information out of Corsair RMi and HXi series of PSUs

License:        BSD-3-Clause
URL:            https://github.com/KyleGospo/corsairmi

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  systemd

Requires:       corsairmi-udev

%description
Minimal program for Linux to read monitoring information out of Corsair RMi and HXi series of PSUs. Uses Linux HIDRAW interface. Tested on Corsair RM650i, RM750i and HX1000i.

%define debug_package %{nil}

	
%package udev
Summary:        Udev rules for Logitech receivers
BuildArch:      noarch

	
%description udev
This package contains udev rules which grant users permission to access corsair power supplies.

%prep
{{{ git_dir_setup_macro }}}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m 0755 ./%{name} %{buildroot}/%{_bindir}/
install -m 644 -p 70-corsairmi.rules %{buildroot}/%{_udevrulesdir}/

%posttrans udev
# This is needed to apply permissions to existing devices when the package is
# installed.
# Skip triggering udevd when it is note accessible, e.g. containers or
# rpm-ostree-based systems.
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=hidraw --action=add
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files udev
%license LICENSE
%_udevrulesdir/70-corsairmi.rules

%changelog
{{{ git_dir_changelog }}}