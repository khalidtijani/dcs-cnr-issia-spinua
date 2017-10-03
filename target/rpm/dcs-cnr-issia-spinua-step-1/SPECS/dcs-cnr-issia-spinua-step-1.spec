%define __jar_repack 0
Name: dcs-cnr-issia-spinua-step-1
Version: 1.0.11
Release: 1
Summary: Developer Cloud Sandbox SPINUA application Step 1
License: ${project.inceptionYear}, CNR ISSIA InSAR4Indo SPINUA, GPL
Distribution: CNR ISSIA InSAR4Indo SPINUA ${project.inceptionYear}
Group: air
Packager: Terradue
Provides: dcs-cnr-issia-spinua-step-1
Requires: snap-5.0
autoprov: yes
autoreq: no
Prefix: /application
BuildArch: noarch
BuildRoot: /home/khalidtijani/dcs-cnr-issia-spinua/target/rpm/dcs-cnr-issia-spinua-step-1/buildroot

%description
Developer Cloud Sandbox SPINUA application Step 1

%install
if [ -d $RPM_BUILD_ROOT ];
then
  mv /home/khalidtijani/dcs-cnr-issia-spinua/target/rpm/dcs-cnr-issia-spinua-step-1/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /home/khalidtijani/dcs-cnr-issia-spinua/target/rpm/dcs-cnr-issia-spinua-step-1/tmp-buildroot $RPM_BUILD_ROOT
fi

%files
%defattr(664,root,ciop,775)
 "/application"
%attr(775,root,ciop)  "/application/splitter/run"
