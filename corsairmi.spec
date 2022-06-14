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

%description
Minimal program for Linux to read monitoring information out of Corsair RMi and HXi series of PSUs. Uses Linux HIDRAW interface. Tested on Corsair RM650i, RM750i and HX1000i.

%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ./%{name} %{buildroot}/%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
{{{ git_dir_changelog }}}