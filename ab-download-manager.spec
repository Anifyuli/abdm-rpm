%global debug_package %{nil}
%global jbr_dir jbrsdk_jcef-21.0.9-linux-x64-b895.149

Name:           ab-download-manager
Version:        1.8.4 
Release:        1%{dist}
Summary:        A Download Manager that speeds up your downloads

License:        Apache-2.0
URL:            https://abdownloadmanager.com
Source0:        https://github.com/amir1376/ab-download-manager/archive/refs/tags/v%{version}.tar.gz
Source1:        https://services.gradle.org/distributions/gradle-9.2.1-bin.zip
Source2:        abdownloadmanager.desktop
Source3:        https://cache-redirector.jetbrains.com/intellij-jbr/jbrsdk_jcef-21.0.9-linux-x64-b895.149.tar.gz

ExclusiveArch:  x86_64

Requires:       libXrender
Requires:       libXtst
Requires:       harfbuzz
Requires:       fontconfig
Requires:       gtk3
Requires:       java-21-openjdk-headless

BuildRequires:  git
BuildRequires:  java-21-openjdk-devel
BuildRequires:  unzip
BuildRequires:  desktop-file-utils

%description
AB Download Manager is a desktop app that helps you manage and organize your downloads more efficiently than ever before.

This RPM build is unofficial, and just help installation steps easier and full controlled

%prep
%autosetup -n ab-download-manager-%{version}

# Init dummy git repo
git init
git config user.email "builder@localhost"
git config user.name "RPM Builder"
git add .
git commit -m "RPM build"
git tag v%{version}
git checkout v%{version}

# Extract Gradle
unzip -q %{SOURCE1} -d %{_builddir}
tar -xf %{SOURCE3} -C %{_builddir}

%build
# Add required env var
export JAVA_HOME=%{_builddir}/%{jbr_dir}
export PATH=$JAVA_HOME/bin:$PATH
export SKIP_ANDROID_BUILD=true

./gradlew --no-daemon createReleaseFolderForCi

%install
tar -xf build/ci-release/binaries/ABDownloadManager_*_linux_x64.tar.gz
mkdir -p %{buildroot}/opt/abdownloadmanager
cp -r ABDownloadManager/* %{buildroot}/opt/abdownloadmanager/

# Install icon
install -Dm644 desktop/app/icons/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/abdownloadmanager.png

# Install desktop file
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/abdownloadmanager.desktop

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/abdownloadmanager.desktop

# Create symlink to /usr/bin
mkdir -p %{buildroot}%{_bindir}
ln -s ../../opt/abdownloadmanager/bin/ABDownloadManager \
      %{buildroot}%{_bindir}/abdownloadmanager

%files
/opt/abdownloadmanager/
%{_datadir}/icons/hicolor/512x512/apps/abdownloadmanager.png
%{_datadir}/applications/abdownloadmanager.desktop
%{_bindir}/abdownloadmanager

%changelog
* Thu Jan 08 2026 Anifyuliansyah <anifyuli007@outlook.co.id> 1.8.4-1
- Bump version to 1.8.4

* Thu Dec 25 2025 Anifyuliansyah <anifyuli007@outlook.co.id> 1.8.3-1
- Bump version to 1.8.3

* Thu Dec 25 2025 Anifyuliansyah <anifyuli007@outlook.co.id> 1.8.2-3
- Fix Git tag for proper app versioning

* Wed Dec 24 2025 Anifyuliansyah <anifyuli007@outlook.co.id> 1.8.2-2
- Remove aarch64 support due to toolchain support limit from upstream

* Wed Dec 24 2025 Anifyuliansyah <anifyuli007@outlook.co.id> 1.8.2-1
- Bump version to 1.8.2

* Tue Dec 23 2025 Anifyuliansyah <anifyuli007@outlook.co.id> - 1.8.1-1
- Initial package
