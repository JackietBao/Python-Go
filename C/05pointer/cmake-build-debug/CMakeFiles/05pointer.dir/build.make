# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\Program Files\CLion 2021.1.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\Program Files\CLion 2021.1.3\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\GitHub\DevOps-SRE\CS\C\05pointer

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/05pointer.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/05pointer.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/05pointer.dir/flags.make

CMakeFiles/05pointer.dir/main.c.obj: CMakeFiles/05pointer.dir/flags.make
CMakeFiles/05pointer.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/05pointer.dir/main.c.obj"
	D:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\05pointer.dir\main.c.obj -c D:\GitHub\DevOps-SRE\CS\C\05pointer\main.c

CMakeFiles/05pointer.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/05pointer.dir/main.c.i"
	D:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\GitHub\DevOps-SRE\CS\C\05pointer\main.c > CMakeFiles\05pointer.dir\main.c.i

CMakeFiles/05pointer.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/05pointer.dir/main.c.s"
	D:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\GitHub\DevOps-SRE\CS\C\05pointer\main.c -o CMakeFiles\05pointer.dir\main.c.s

# Object files for target 05pointer
05pointer_OBJECTS = \
"CMakeFiles/05pointer.dir/main.c.obj"

# External object files for target 05pointer
05pointer_EXTERNAL_OBJECTS =

05pointer.exe: CMakeFiles/05pointer.dir/main.c.obj
05pointer.exe: CMakeFiles/05pointer.dir/build.make
05pointer.exe: CMakeFiles/05pointer.dir/linklibs.rsp
05pointer.exe: CMakeFiles/05pointer.dir/objects1.rsp
05pointer.exe: CMakeFiles/05pointer.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable 05pointer.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\05pointer.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/05pointer.dir/build: 05pointer.exe

.PHONY : CMakeFiles/05pointer.dir/build

CMakeFiles/05pointer.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\05pointer.dir\cmake_clean.cmake
.PHONY : CMakeFiles/05pointer.dir/clean

CMakeFiles/05pointer.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\GitHub\DevOps-SRE\CS\C\05pointer D:\GitHub\DevOps-SRE\CS\C\05pointer D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug D:\GitHub\DevOps-SRE\CS\C\05pointer\cmake-build-debug\CMakeFiles\05pointer.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/05pointer.dir/depend

