Name:           ros-kinetic-rospy
Version:        1.12.5
Release:        0%{?dist}
Summary:        ROS rospy package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rospy
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       PyYAML
Requires:       numpy
Requires:       python-rospkg
Requires:       ros-kinetic-genpy
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-rosgraph-msgs >= 1.10.3
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin >= 0.5.78

%description
rospy is a pure Python client library for ROS. The rospy client API enables
Python programmers to quickly interface with ROS Topics, Services, and
Parameters. The design of rospy favors implementation speed (i.e. developer
time) over runtime performance so that algorithms can be quickly prototyped and
tested within ROS. It is also ideal for non-critical-path code, such as
configuration and initialization code. Many of the ROS tools are written in
rospy to take advantage of the type introspection capabilities. Many of the ROS
tools, such as rostopic and rosservice, are built on top of rospy.

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
* Fri Sep 30 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

* Fri Jun 03 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

