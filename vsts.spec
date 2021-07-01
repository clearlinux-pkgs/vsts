#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vsts
Version  : 0.1.25
Release  : 10
URL      : https://files.pythonhosted.org/packages/ce/fa/4405cdb2a6b0476a94b24254cdfb1df7ff43138a91ccc79cd6fc877177af/vsts-0.1.25.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/fa/4405cdb2a6b0476a94b24254cdfb1df7ff43138a91ccc79cd6fc877177af/vsts-0.1.25.tar.gz
Summary  : Python wrapper around the VSTS APIs
Group    : Development/Tools
License  : MIT
Requires: vsts-license = %{version}-%{release}
Requires: vsts-python = %{version}-%{release}
Requires: vsts-python3 = %{version}-%{release}
Requires: msrest
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
No detailed description available

%package license
Summary: license components for the vsts package.
Group: Default

%description license
license components for the vsts package.


%package python
Summary: python components for the vsts package.
Group: Default
Requires: vsts-python3 = %{version}-%{release}

%description python
python components for the vsts package.


%package python3
Summary: python3 components for the vsts package.
Group: Default
Requires: python3-core
Provides: pypi(vsts)
Requires: pypi(msrest)

%description python3
python3 components for the vsts package.


%prep
%setup -q -n vsts-0.1.25
cd %{_builddir}/vsts-0.1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588882728
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vsts
cp %{_builddir}/vsts-0.1.25/LICENSE.txt %{buildroot}/usr/share/package-licenses/vsts/045b430b5279f6dcb6df6a395c921ace206c64a3
cp %{_builddir}/vsts-0.1.25/vsts/licensing/v4_0/models/license.py %{buildroot}/usr/share/package-licenses/vsts/ac68a31d6150c1a30c1076b62cfc133823ab3bba
cp %{_builddir}/vsts-0.1.25/vsts/licensing/v4_1/models/license.py %{buildroot}/usr/share/package-licenses/vsts/ac68a31d6150c1a30c1076b62cfc133823ab3bba
cp %{_builddir}/vsts-0.1.25/vsts/member_entitlement_management/v4_1/models/license_summary_data.py %{buildroot}/usr/share/package-licenses/vsts/301449cdb4397dd93db6d6b4ab96a5ffe378b4f3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vsts/045b430b5279f6dcb6df6a395c921ace206c64a3
/usr/share/package-licenses/vsts/301449cdb4397dd93db6d6b4ab96a5ffe378b4f3
/usr/share/package-licenses/vsts/ac68a31d6150c1a30c1076b62cfc133823ab3bba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
