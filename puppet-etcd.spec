%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-etcd
%global commit f43e1292a9554766f799cd5a14b67cc19ce5b00e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-etcd
Version:                1.11.0
Release:                1%{?alphatag}%{?dist}
Summary:                Installs and configures etcd
License:                ASL 2.0

URL:                    https://github.com/cristifalcas/puppet-etcd

Source0:                https://github.com/cristifalcas/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs and configures etcd

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/etcd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/etcd/


%files
%{_datadir}/openstack-puppet/modules/etcd/


%changelog
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 1.11.0-1.f43e129git
- Pike update 1.11.0 (f43e1292a9554766f799cd5a14b67cc19ce5b00e)
