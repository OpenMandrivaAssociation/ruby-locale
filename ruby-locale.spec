%define name ruby-locale
%define version 2.0.4
%define release %mkrel 1

Summary: Locale handling library
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://gettext.rubyforge.org/
Source0: http://rubyforge.org/frs/download.php/57277/ruby-locale-2.0.4.tar.gz
License: LGPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8.2
BuildRequires: ruby-devel gettext-devel ruby-racc ruby-rake

%description
Ruby-Locale is the pure ruby library which provides basic APIs for 
localization. It aims to support all environments and all kind of i18n/l10n
programs (GUI, WWW, library, etc), and becomes the hub of other i18n/l10n
programs to handle major locale ID standards.

%prep
%setup -q 

%build
ruby setup.rb config 
ruby setup.rb setup

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot
%find_lang %name --all-name 

for f in `find samples %buildroot -name \*.rb`
do
	if head -n1 "$f" | grep '^#!' >/dev/null;
	then
		sed -i 's|/usr/local/bin|/usr/bin|' "$f"
		chmod 0755 "$f"
	else
		chmod 0644 "$f"
	fi
done

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%{ruby_sitelibdir}/locale*

%doc COPYING README.rdoc samples test ChangeLog 

