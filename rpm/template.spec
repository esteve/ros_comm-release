Name:           ros-kinetic-topic-tools
Version:        1.12.2
Release:        0%{?dist}
Summary:        ROS topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rostime
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-xmlrpcpp
BuildRequires:  ros-kinetic-catkin >= 0.5.78
BuildRequires:  ros-kinetic-cpp-common
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rostime
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-xmlrpcpp

%description
Tools for directing, throttling, selecting, and otherwise messing with ROS
topics at a meta level. None of the programs in this package actually know about
the topics whose streams they are altering; instead, these tools deal with
messages as generic binary blobs. This means they can be applied to any ROS
topic.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jun 03 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

