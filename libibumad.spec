Summary: OpenFabrics Alliance InfiniBand umad (user MAD) library
Name: libibumad
Version: 1.3.10.2
Release: 1%{?dist}
License: GPLv2 or BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Url: http://www.openfabrics.org
Requires: rdma
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: glibc-static
%ifnarch ia64 %{sparc} s390 s390x
BuildRequires: valgrind-devel
%endif

%description
libibumad provides the user MAD library functions which sit on top of 
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM. 

%package devel
Summary: Development files for the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the libibumad library.

%package static
Summary: Static version of the libibumad library
Group: System Environment/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
Static version of the libibumad library.

%prep
%setup -q

%build
%ifnarch ia64 %{sparc} s390 s390x
%configure --with-valgrind
%else
%configure
%endif
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libibumad*.so.*
%{_mandir}/man3/*
%doc AUTHORS COPYING ChangeLog 

%files devel
%defattr(-,root,root)
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

%files static
%defattr(-,root,root)
%{_libdir}/libibumad.a

%changelog
* Fri Jun 05 2015 Doug Ledford <dledford@redhat.com> - 1.3.10.2-1
- Update to latest upstream release
- Pick up OPA MAD support
- Drop s390 restriction
- Resolves: bz1169962
- Related: bz1186159

* Thu Oct 09 2014 Doug Ledford <dledford@redhat.com> - 1.3.9-1
- Update to latest upstream release (needed by other packages)
- Related: bz1092538

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.8-3
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Doug Ledford <dledford@redhat.com> - 1.3.8-1
- Update to latest upstream version
- Fix Url tag

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Doug Ledford <dledford@redhat.com> - 1.3.7-1
- Update to latest upstream source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 27 2010 Doug Ledford <dledford@redhat.com> - 1.3.4-1
- New upstream release

* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.3.3-2
- ExcludeArch s390(x) as there is no hardware support there

* Thu Dec 03 2009 Doug Ledford <dledford@redhat.com> - 1.3.3-1
- Update to latest upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Doug Ledford <dledford@redhat.com> - 1.3.2-2
- Forgot to remove both instances of the libibcommon requires
- Add build requires on glibc-static

* Mon Jul 20 2009 Doug Ledford <dledford@redhat.com> - 1.3.2-1
- Update to latest upstream version
- Remove requirement on libibcommon since that library is no longer needed
- Fix a problem with man page listing

* Wed Apr 22 2009 Doug Ledford <dledford@redhat.com> - 1.3.1-1
- Update to latest upstream version

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> - 1.2.0-3
- Rebuilt against libtool 2.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 08 2008 Doug Ledford <dledford@redhat.com> - 1.2.0-1
- Initial package for Fedora review process
