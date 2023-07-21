cmake_minimum_required(VERSION 3.15 FATAL_ERROR)


project(TrkHitConverter CXX)

include(GNUInstallDirs)

# Define a default build type can be overriden by passing
# ``-DCMAKE_BUILD_TYPE=<type>`` when invoking CMake
if(NOT CMAKE_CONFIGURATION_TYPES)
  if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE RelWithDebInfo
      CACHE STRING "Choose the type of build, options are: None Release MinSizeRel Debug RelWithDebInfo"
      FORCE
      )
  else()
    set(CMAKE_BUILD_TYPE "${CMAKE_BUILD_TYPE}"
      CACHE STRING "Choose the type of build, options are: None Release MinSizeRel Debug RelWithDebInfo"
      FORCE
      )
  endif()
endif()

# Set up C++ Standard
# ``-DCMAKE_CXX_STANDARD=<standard>`` when invoking CMake
set(CMAKE_CXX_STANDARD 17 CACHE STRING "")

# Prevent CMake falls back to the latest standard the compiler does support
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Disables the use of compiler-specific extensions, hence makes sure the code
# works for a wider range of compilers
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(ILCUTIL COMPONENTS ILCSOFT_CMAKE_MODULES REQUIRED)
include(ilcsoft_default_settings)

find_package( Marlin 1.0 REQUIRED )

set(sources
  src/TrkHitConverterProcessor.cc
)

message(STATUS "marlin include dirs " ${Marlin_INCLUDE_DIRS})

add_library(TrkHitConverter SHARED ${sources})
target_link_libraries(TrkHitConverter PUBLIC ${Marlin_LIBRARIES})
target_include_directories(TrkHitConverter PUBLIC
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
  ${Marlin_INCLUDE_DIRS}
  )

install(TARGETS TrkHitConverter
  EXPORT TrkHitConverterTargets
  DESTINATION ${CMAKE_INSTALL_LIBDIR}
  )
