Name: tgbot-cpp
Version: 1.1
Release: 2%{?dist}

Summary: C++ library for Telegram bot API
License: MIT
URL: https://github.com/reo7sp/%{name}
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
C++ library for Telegram bot API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
mkdir -p %{_target_platform}
sed -e 's@DESTINATION lib@DESTINATION %{_lib}@g' -i CMakeLists.txt
echo "set_property(TARGET \${PROJECT_NAME} PROPERTY SOVERSION 1)" >> CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=ON \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files
%doc README.md
%license LICENSE
%{_libdir}/libTgBot.so.*

%files devel
%{_includedir}/tgbot
%{_libdir}/libTgBot.so

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1
- Initial SPEC release.
