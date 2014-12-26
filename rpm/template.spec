Name:           ros-jade-roswtf
Version:        1.11.10
Release:        0%{?dist}
Summary:        ROS roswtf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roswtf
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-paramiko
Requires:       python-rospkg
Requires:       ros-jade-rosbuild
Requires:       ros-jade-rosgraph
Requires:       ros-jade-roslaunch
Requires:       ros-jade-roslib
Requires:       ros-jade-rosnode
Requires:       ros-jade-rosservice
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-rostest

%description
roswtf is a tool for diagnosing issues with a running ROS system. Think of it as
a FAQ implemented in code.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

