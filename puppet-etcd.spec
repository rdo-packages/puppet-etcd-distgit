%{!?upstream_version: %global upstream_version %{commit}}
%global commit 39faa948f68c8e8ac0337ea74c1406da776cd71b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-etcd
Version:                1.12.2
Release:                3%{?alphatag}%{?dist}
Summary:                Installs and configures etcd
License:                ASL 2.0

URL:                    https://github.com/cristifalcas/puppet-etcd

Source0:                https://github.com/cristifalcas/puppet-etcd/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

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
* Thu Oct 3 2019 RDO <dev@lists.rdoproject.org> 1.12.2-3.39faa94git
- Update to post 1.12.2 (39faa948f68c8e8ac0337ea74c1406da776cd71b)


