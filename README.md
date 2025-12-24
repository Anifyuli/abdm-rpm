# AB Download Manager - RPM Spec

<div align="center">

![AB Download Manager](https://raw.githubusercontent.com/amir1376/ab-download-manager/master/assets/logo/app_logo_with_background.svg)

**RPM packaging for AB Download Manager**

[![Copr build status](https://copr.fedorainfracloud.org/coprs/YOUR_USERNAME/ab-download-manager/package/ab-download-manager/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/YOUR_USERNAME/ab-download-manager/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Fedora](https://img.shields.io/badge/Fedora-41+-blue.svg?logo=fedora&logoColor=white)](https://getfedora.org/)
[![RHEL](https://img.shields.io/badge/RHEL-9+-red.svg?logo=redhat&logoColor=white)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)

</div>

---

## 📋 About

This repository contains the **RPM spec files** for building [AB Download Manager](https://github.com/amir1376/ab-download-manager) packages in Copr.

> **Note**: This is an **unofficial** packaging effort and is not affiliated with the official AB Download Manager project.

## 📦 Installation

### Quick Install from Copr

#### Fedora 41+
```bash
sudo dnf copr enable anifyuliansyah/ab-download-manager
sudo dnf install ab-download-manager
```

#### RHEL/CentOS Stream/Rocky/AlmaLinux 9+
```bash
# Enable EPEL first
sudo dnf install epel-release

# Enable Copr repository
sudo dnf copr enable anifyuliansyah/ab-download-manager
sudo dnf install ab-download-manager
```

### Supported Distributions

| Distribution | Version | Status |
|--------------|---------|--------|
| **Fedora** | 41+ | ✅ Supported |
| **RHEL** | 9+ | ✅ Supported (via EPEL) |
| **CentOS Stream** | 9+ | ✅ Supported |
| **Rocky Linux** | 9+ | ✅ Supported |
| **AlmaLinux** | 9+ | ✅ Supported |

## 🚀 What is AB Download Manager?

AB Download Manager is a modern download manager with features like:

- ⚡ **Multi-threaded Downloads** - Speed up your downloads significantly
- 📅 **Queue Management** - Organize downloads with queues and schedulers
- 🌐 **Browser Extensions** - Seamless integration with Firefox and Chrome
- 🎨 **Modern UI** - Beautiful interface with dark/light themes
- 🔓 **Free & Open Source** - Apache 2.0 licensed

For more info, visit the [official website](https://abdownloadmanager.com).

## 📁 Repository Structure

```
.
├── ab-download-manager.spec    # Main spec file for building RPM
├── abdownloadmanager.desktop   # Desktop entry file
├── LICENSE                      # Apache 2.0 License
└── README.md                    # This file
```

## 🔧 Building Locally

If you want to build the package locally before submitting to Copr:

```bash
# Install build tools
sudo dnf install fedpkg mock

# Clone this repository
git clone https://github.com/YOUR_USERNAME/ab-download-manager-copr.git
cd ab-download-manager-copr

# Build with mock (clean environment)
mock -r fedora-41-x86_64 ab-download-manager.spec

# Or use rpmbuild
rpmdev-setuptree
cp ab-download-manager.spec ~/rpmbuild/SPECS/
cp abdownloadmanager.desktop ~/rpmbuild/SOURCES/
spectool -g -R ~/rpmbuild/SPECS/ab-download-manager.spec
rpmbuild -ba ~/rpmbuild/SPECS/ab-download-manager.spec
```

## 🤝 Contributing

Contributions to improve the packaging are welcome!

### How to Contribute

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b improve-spec`)
3. **Test** your changes with mock or rpmbuild
4. **Commit** your changes (`git commit -am 'Improve spec file'`)
5. **Push** to the branch (`git push origin improve-spec`)
6. **Open** a Pull Request

### Contribution Ideas

- 🐛 Fix packaging bugs
- 📝 Improve documentation
- 🧪 Test on different distributions
- ⚡ Optimize build process
- 📦 Update to newer versions

### Testing Checklist

Before submitting changes, please verify:

- [ ] Spec file passes `rpmlint` without critical errors
- [ ] Package builds successfully in mock
- [ ] Application starts and runs correctly
- [ ] Desktop file is valid (`desktop-file-validate`)
- [ ] All dependencies are correctly specified

## 📄 License

This packaging is licensed under the Apache License 2.0, matching the upstream project.

The original AB Download Manager is developed by [Amir Hossein](https://github.com/amir1376) and is also licensed under Apache 2.0.

## 🔗 Links

- **Copr Repository**: [copr.fedorainfracloud.org/coprs/YOUR_USERNAME/ab-download-manager](https://copr.fedorainfracloud.org/coprs/YOUR_USERNAME/ab-download-manager/)
- **Upstream Project**: [AB Download Manager on GitHub](https://github.com/amir1376/ab-download-manager)
- **Official Website**: [abdownloadmanager.com](https://abdownloadmanager.com)
- **AUR Package** (Reference): [ab-download-manager on AUR](https://aur.archlinux.org/packages/ab-download-manager)

### Community

- **Telegram Discussion**: [Join Group](https://t.me/abdownloadmanager_discussion)
- **Telegram Channel**: [Updates](https://t.me/abdownloadmanager)
- **Report Issues**: [GitHub Issues](../../issues)

## ⚠️ Disclaimer

This is an **unofficial** RPM packaging of AB Download Manager. 

- Not endorsed by the original developer
- Provided as-is without warranty
- For official support, please contact the upstream project

## 🙏 Acknowledgments

- Original software by [Amir Hossein](https://github.com/amir1376) - creator of AB Download Manager
- Build methodology inspired by [AUR package](https://aur.archlinux.org/packages/ab-download-manager)
- Thanks to all contributors and testers

## 📝 Changelog

See [upstream releases](https://github.com/amir1376/ab-download-manager/releases) for application changelog.

For packaging changes, see [commits history](../../commits/main).

---

<div align="center">

**Made with ❤️ for the Fedora/RHEL community**

If this packaging helps you, consider:
- ⭐ **Starring** this repository
- ⭐ **Starring** the [upstream project](https://github.com/amir1376/ab-download-manager)
- 💬 **Sharing** with others who might find it useful

</div>
